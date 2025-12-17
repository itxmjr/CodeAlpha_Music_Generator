from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import logging
import time

from src.generate import MusicGenerator, MoodConfig

# --- Configuration ---
MODEL_PATH = "outputs/models/best_model.pt"
VOCAB_PATH = "outputs/models/vocabulary.json"
OUTPUT_DIR = Path("outputs/generated")

# --- Setup Logging ---
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# --- Initialize App ---
app = FastAPI(title="AI Music Generator")

# Check if model exists
if not Path(MODEL_PATH).exists() or not Path(VOCAB_PATH).exists():
    logger.error("❌ Model files not found! Please run 'python main.py train' first.")

# Initialize the generator globally to load model once
try:
    generator = MusicGenerator(MODEL_PATH, VOCAB_PATH)
    logger.info("✅ Model loaded successfully")
except Exception as e:
    logger.error(f"❌ Failed to load model: {e}")
    generator = None

# Ensure output directory exists
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# --- Routes ---

@app.get("/", response_class=HTMLResponse)
async def read_root():
    """Serve the main HTML page."""
    html_path = Path("static/index.html")
    if html_path.exists():
        return html_path.read_text(encoding="utf-8")
    return "<h1>Error: static/index.html not found</h1>"

@app.get("/generate")
async def generate_music(mood: str = "energetic"):
    """
    Generate music based on mood.
    Returns a MIDI file download.
    """
    if not generator:
        raise HTTPException(status_code=503, detail="Model not initialized. Please check server logs.")
    
    try:
        # Get mood configuration
        config = MoodConfig.get_config(mood)
        logger.info(f"Generating for mood '{mood}': {config}")
        
        # Create unique filename
        filename = f"generated_{mood}_{int(time.time())}.mid"
        output_path = OUTPUT_DIR / filename
        
        # Generate music
        generator.generate_and_save(
            output_path=str(output_path),
            length=300,  # Reasonable length for web generation
            temperature=config["temperature"],
            bpm=config["bpm"]
        )
        
        if not output_path.exists():
             raise HTTPException(status_code=500, detail="Failed to create MIDI file")
             
        # Return file download
        return FileResponse(
            path=output_path,
            filename=filename,
            media_type="audio/midi"
        )
        
    except Exception as e:
        logger.error(f"Generation failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# Mount static files (optional, if you have other assets like css/js)
app.mount("/static", StaticFiles(directory="static"), name="static")
