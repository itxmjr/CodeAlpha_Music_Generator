# Use Python 3.10
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
# Using pip directly to simplify the Docker build for HF Spaces
RUN pip install --no-cache-dir torch numpy music21 tqdm matplotlib fastapi uvicorn python-multipart

# Create necessary directories
RUN mkdir -p outputs/models outputs/generated

# Expose the standard Hugging Face Spaces port
EXPOSE 7860

# Run the application
CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "7860"]
