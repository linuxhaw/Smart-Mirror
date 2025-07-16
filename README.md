# 👗 AI-Powered Female Outfit Recommendation System

This project is an AI-based system that analyzes outfit images and recommends fashion styles using a combination of object detection, image classification, and large language models.

Built with **Streamlit** for a simple and interactive web interface, it leverages cutting-edge tools such as **YOLOv9**, **Hugging Face models**, **Gemini Pro (Google GenAI)**, **LangChain**, **Roboflow**, and **BLIP** for accurate and intelligent fashion recommendations.

---

## ✨ Key Features

- 🔍 **Object Detection** using **YOLOv9**  
  Detects clothing items and segments them from the image input.

- 🖼️ **Image Classification** with **Hugging Face** models & **BLIP**  
  Analyzes detected clothing to classify styles, categories, and contexts.

- 🤖 **AI-Based Recommendations**  
  Uses **Gemini Pro (Google GenAI)** via **LangChain** to generate smart and context-aware outfit suggestions.

- 🧪 **Dataset Management** via **Roboflow**  
  Efficiently handles datasets for model training and optimization.

- 🌐 **Streamlit UI**  
  Simple and clean frontend for uploading images and viewing recommendations in real-time.

---

## 🧠 Tech Stack

| Component        | Technology Used                      |
|------------------|--------------------------------------|
| Object Detection | YOLOv9 (Custom Trained via Roboflow) |
| Image Analysis   | Hugging Face, BLIP                   |
| AI Logic         | Gemini Pro, LangChain                |
| Frontend         | Streamlit                            |
| Dataset          | Roboflow                             |

---

## 🚀 How to Run

1. **Clone this repository**
   ```bash
   git clone [[https://github.com/your-username/your-repo-name](https://github.com/linuxhaw/Smart-Mirror.git](https://github.com/linuxhaw/Smart-Mirror.git)
   cd your-repo-name

pip install -r requirements.txt

streamlit run app.py

├── app.py                    # Main Streamlit app
├── yolo/                     # YOLOv9 model & detection logic
├── genai/                    # Gemini & LangChain integration
├── classify/                 # Hugging Face / BLIP classification
├── utils/                    # Utility functions
├── data/                     # Sample input/output
└── requirements.txt          # Python dependencies
