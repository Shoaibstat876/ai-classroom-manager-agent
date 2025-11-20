📘 AI Classroom Manager Agent — Master Edition
An Intelligent Teaching Assistant for Modern Classrooms
🏫 Project Overview

AI Classroom Manager Agent is a multi-interface educational AI assistant designed to support teachers in Pakistan and worldwide by automating essential classroom workflows.
It intelligently generates lesson plans, timetables, tests, parent messages, behaviour notes, emergency lesson plans, and progress heatmaps — all powered by advanced Large Language Models (OpenRouter / Gemini / OpenAI-compatible).

This project includes three complete worlds:

🚀 CLI Version (Text-based terminal app)

🌐 Flask Web App (Fully designed UI)

🎨 Streamlit Version (Quick interactive dashboard)

The project demonstrates mastery of:

AI integration

Software architecture

API usage

Full-stack development

Prompt engineering

Python development

UI/UX design

🧠 Key Features
✔ Generate Weekly Timetables

Avoid teacher clashes and provide clean, readable class schedules.

✔ Full Lesson Plan Generator

Bloom’s-taxonomy-based plans with objectives, warm-up, materials, main activity, assessment & homework.

✔ Automatic Test / Worksheet Generator

MCQs, short questions, long questions — age-appropriate and curriculum-aligned.

✔ Parent Message Generator

Polite, short, professional SMS-style notes for academic or behaviour-related issues.

✔ Behaviour & Observation Notes

Professional notes for school records, including teacher recommendations.

✔ Emergency Lesson Plans

Quick 20-minute backup plans for unexpected situations.

✔ Text-Based Progress Heatmap

Beautiful progress chart using bars (███▒▒▒▒).

🏗 Tech Stack
Layer	Technology
AI Model	Gemini / OpenRouter (OpenAI-compatible)
Backend	Python 3.12
API Client	openai + OpenRouter endpoint
Web UI	Flask + Bootstrap
Dashboard UI	Streamlit
CLI	Pure Python
Environment	.env + python-dotenv
Version Control	Git & GitHub
📂 Project Structure
ai-classroom-manager/
│
├── main.py                # CLI app
├── app.py                 # Flask app
├── streamlit_app.py       # Streamlit UI
├── config.py              # API configuration
├── features.py            # All AI features and logic
│
├── templates/             # Flask HTML templates
│   ├── base.html
│   ├── index.html
│   └── ...
│
├── static/                # CSS files for Flask
│   └── style.css
│
└── screenshots/           # All project UI screenshots
    ├── cli.png
    ├── flask_a.png
    ├── flask_b.png
    └── streamlit.png

🖥 1 — CLI Version

Run:

python main.py

Screenshot

(add your screenshot using this path)

![CLI](screenshots/cli.png)

🌐 2 — Flask Web App (Full UI Version)

Run:

python app.py


App opens at:

http://127.0.0.1:5000/

Screenshots
![Flask UI 1](screenshots/flask_a.png)
![Flask UI 2](screenshots/flask_b.png)

🎨 3 — Streamlit Web App

Start with:

streamlit run streamlit_app.py


App runs at:

http://localhost:8502

Screenshot
![Streamlit](screenshots/streamlit.png)

🔑 Environment Setup

Create and activate a virtual environment:

python -m venv .venv
.\.venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt


Create a .env file:

GEMINI_API_KEY=your_key_here
OPENROUTER_API_KEY=your_key_here

🧪 Tested AI Models

This project fully supports:

Google Gemini 2.0 Flash

Google Gemma 2

OpenAI GPT-4.1 / GPT-4o Mini (via OpenRouter)

DeepSeek V3 (via OpenRouter)

Any OpenAI-compatible model

📦 Why This Project Is Special

✔ Built with three real production-style interfaces
✔ Demonstrates clean code architecture
✔ Uses modular functions for each AI feature
✔ Fully documented project
✔ Perfect for teachers, students, schools, AI demos
✔ Showcases full-stack + AI engineering skills
✔ Includes screenshots, UI, CLI, and backend

This is not a small script —
This is a complete educational AI product.

✨ Credits

Built with ❤️ by Muhammad Shoaib
AI Engineer • Teacher • Innovator

🏁 License

This project is for educational and academic purposes.
You may modify it for personal or school use.