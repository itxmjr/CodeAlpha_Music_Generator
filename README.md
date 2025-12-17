# 🎵 CodeAlpha Music Generator

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95+-009688.svg?style=for-the-badge&logo=fastapi&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)

A powerful AI-based music composition tool built with Python and PyTorch, featuring a modern web interface. This project uses LSTM neural networks to create unique musical pieces and offers a sleek, mood-based generation UI.

## ✨ Features

- **Mood-Based Generation**: Select from moods like "Energetic", "Melancholic", or "Cyberpunk" to shape the music.
- **Modern Web Interface**: Beautiful, glassmorphic UI built with HTML5 and TailwindCSS.
- **Deep Learning Core**: Utilizes robust LSTM neural networks to understand and predict musical patterns.
- **Real-Time Generation**: Powered by FastAPI for quick, asynchronous music creation.
- **MIDI Export**: Instantly download your creations as standard MIDI files.

## 🚀 Demo

*(Add a screenshot of your new UI here)*

## 🛠️ Tech Stack

- **[FastAPI](https://fastapi.tiangolo.com/)**: High-performance backend API.
- **[PyTorch](https://pytorch.org/)**: Deep learning framework for the LSTM model.
- **[music21](https://web.mit.edu/music21/)**: Toolkit for MIDI processing.
- **[TailwindCSS](https://tailwindcss.com/)**: Styling for the modern web interface.
- **[Docker](https://www.docker.com/)**: Containerization for easy deployment.

## 📦 Installation

Ensure you have Python 3.10 or higher installed.

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/itxmjr/CodeAlpha_Music_Generator.git
    cd CodeAlpha_Music_Generator
    ```

2.  **Install Dependencies**
    Using `uv` (recommended):
    ```bash
    uv sync
    ```
    Or using `pip`:
    ```bash
    pip install -r requirements.txt  # If requirements.txt exists
    # OR
    pip install torch numpy music21 tqdm matplotlib fastapi uvicorn python-multipart
    ```

## 🎮 Usage

You can run the project either as a Web App or a CLI tool.

### 🌐 Web App (Recommended)
Start the web server:
```bash
uv run uvicorn src.api:app --host 0.0.0.0 --port 8000
```
Open [http://localhost:8000](http://localhost:8000) in your browser. Select a mood and click **Generate**!

### 💻 Command Line Interface
1.  **Train the Model** (Required first time):
    ```bash
    python main.py train
    ```
2.  **Generate Music**:
    ```bash
    python main.py generate
    ```

## 🐳 Deployment (Docker / HF Spaces)

This app is ready for deployment on Hugging Face Spaces or any Docker-compatible platform.

1.  **Build Docker Image**
    ```bash
    docker build -t music-app .
    ```
2.  **Run Container**
    ```bash
    docker run -p 7860:7860 music-app
    ```

## 📂 Project Structure

```
CodeAlpha_Music_Generator/
├── data/midi/           # Training data (ignored by git)
├── static/
│   └── index.html       # Web App Frontend
├── src/
│   ├── api.py           # FastAPI Backend
│   ├── generate.py      # Generation Logic & Mood Config
│   ├── model.py         # LSTM Model Architecture
│   ├── train.py         # Training Loop
│   └── ...
├── outputs/             # Generated files & Saved Models
├── Dockerfile           # Deployment Configuration
├── main.py              # CLI Entry Point
└── README.md            # Documentation
```

## 🤝 Contributing

Contributions are welcome!

1.  Fork the repository.
2.  Create your feature branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the branch (`git push origin feature/AmazingFeature`).
5.  Open a Pull Request.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">
  <sub>Built with ❤️ by M Jawad ur Rehman using PyTorch, FastAPI, and Python.</sub>
</div>