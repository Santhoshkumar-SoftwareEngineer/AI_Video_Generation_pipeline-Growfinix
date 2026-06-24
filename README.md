# 🎬 Automated AI Video Generation Pipeline

## 📌 Overview

The **Automated AI Video Generation Pipeline** is a Python-based application that generates short cinematic videos from text prompts. Users can enter a prompt, generate an AI image, convert it into an animated video, preview the output, and download the generated MP4 file through a Streamlit web interface.

This project was developed as part of the **Growfinix AI Internship**.

---

## 🚀 Features

* Text-to-video generation workflow
* AI image generation from text prompts
* Automatic MP4 video creation
* Timestamp-based video filenames
* Streamlit web interface
* Image preview
* Video preview
* Download generated videos
* Adjustable FPS settings
* Adjustable video duration
* Multiple animation styles
* Prompt history saving
* Error handling

---

## 🛠️ Tech Stack

* Python
* Streamlit
* OpenCV
* Pillow
* Requests
* NumPy
* Pollinations AI

---

## 📂 Project Structure

```text
AI_Video_Generation_Pipeline
│
├── assets/
├── videos/
├── image_generator.py
├── video_generator.py
├── main.py
├── streamlit_app.py
├── requirements.txt
├── README.md
├── .gitignore
└── history.txt
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/Swetha-K-SoftwareEngineer-AI-DS/AI_Video_Generation_Pipeline-Growfinix
```

### Navigate to the Project Directory

```bash
cd AI_Video_Generation_Pipeline
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run streamlit_app.py
```

---

## 📸 Workflow

```text
User Prompt
      ↓
AI Image Generation
      ↓
Animated Video Creation
      ↓
MP4 Output
      ↓
Preview and Download
```

---

## 🎥 Example Prompt

```text
slow-motion fireworks and gold glitter effects over 3D golden text
```

---

## 📷 Screenshots

### Home Page

(Add screenshot here)

### Generated Image

(Add screenshot here)

### Video Preview

(Add screenshot here)

---

## 📦 Output

Generated videos are automatically saved inside:

```text
videos/
```

Example:

```text
generated_video_20260623_191653.mp4
```

---

## 📋 Requirements

* Python 3.10+
* Internet connection
* Streamlit

---

## 👩‍💻 Author

S.Santhosh kumar

AI & Data Science Enthusiast

GitHub: https://github.com/Swetha-K-SoftwareEngineer-AI-DS

---

## ⭐ Project

Developed for the **Growfinix AI Internship**.