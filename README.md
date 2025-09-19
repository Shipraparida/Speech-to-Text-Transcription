<div align="center">

# 🗣️ SPEECH-TO-TEXT TRANSCRIPTION

A Python-based tool for converting audio recordings into text using the `SpeechRecognition` library.  
This project demonstrates how to transcribe spoken language into written form, enabling applications such as meeting note automation, accessibility tools, and hands-free command systems.  

</div>

---

## 🧾 Table of Contents

- [About the Project](#about-the-project)  
- [Features](#features)  
- [Demo](#demo)  
- [Installation](#installation)  
- [Output](#output)
- [Dataset](#dataset) 

---

## About the Project

This repository provides a simple yet effective pipeline for **speech-to-text conversion**:

1. **Audio Input** – Captures speech from microphone or pre-recorded audio files.  
2. **Transcription** – Uses Google Speech Recognition API via the `SpeechRecognition` library.  
3. **Output** – Returns the spoken words in plain text format, ready to use in applications.  

Perfect for students, developers, and researchers interested in **Natural Language Processing (NLP)** and **voice-enabled systems**.

---

## Features

- 🎤 **Live audio capture** via microphone  
- 🎧 **Transcribe audio recordings** (`.wav`, `.mp3`, etc.)  
- 📝 **Convert speech into editable text**  
- 🌐 Uses **Google Speech Recognition API** (requires internet)  
- ⚡ Lightweight and easy to integrate into larger projects  

---

## Demo

Run live transcription from microphone:

```bash
python speech_to_text.py
```
---

## Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/YourUsername/Speech_to_Text.git
   cd Speech_to_Text

   ```
2. **Install dependencies**
   ```bash
   pip install SpeechRecognition
   pip install pyaudio
   ```
3. **On Windows,  if pyaudio fails to install, then:**
   ```bash
   pip install pipwin
   pipwin install pyaudio
   ```

---

## Output
```bash
Adjusting for background noise... Please wait
Start speaking! (Press Ctrl+C to stop)
You said: Hello, this is a test.
```
---

## 📊 Dataset

The dataset is available on [Kaggle](https://www.kaggle.com/code/cdeotte/25-million-images-0-99757-mnist/input) 
---

