# 📘 AI Classroom Manager Agent – Triple Interface Edition  
*(CLI + Flask Web App + Streamlit Dashboard)*

Built by **Muhammad Shoaib** for the **Agentic AI / AIDD** journey.  
This project is a complete **AI-powered classroom assistant** that helps teachers plan, assess, and communicate faster, using the same brain across **three worlds**:

1. 🧾 **CLI** – fast terminal tool for power users  
2. 🌐 **Flask Web UI** – classic teacher-friendly web interface  
3. 📊 **Streamlit App** – modern dashboard for quick demos & live sharing  

All three share one core logic file: `features.py`.

---

## 🔍 1. Project Overview

**Project name:** AI Classroom Manager Agent  
**Category:** Education / Teacher Productivity  
**Tech focus:** OpenAI-style API (OpenRouter / OpenAI), Python 3.12, Flask, Streamlit.

**Goal:**  
Reduce teacher workload by auto-generating:

- Timetables  
- Lesson plans  
- Tests / worksheets  
- Parent SMS messages  
- Behaviour / observation notes  
- Emergency 20-minute backup lessons  
- Progress heatmaps (text-based)

Everything is designed for **Pakistani school context** (grades, subjects, behaviour notes, exam style).

---

## 🧠 2. Core Features (Shared Brain in `features.py`)

`features.py` contains the main AI behaviours, reused by CLI, Flask, and Streamlit.

1. **Timetable Generator**  
   - Input: classes, days, periods per day  
   - Output: text tables per class, avoiding clashes conceptually

2. **Lesson Plan Generator**  
   - Uses **Bloom’s Taxonomy style** lesson plans  
   - Includes: Objectives, Materials, Warm-up, Main Activity, Assessment, Homework

3. **Test / Worksheet Generator**  
   - MCQs / short questions style  
   - Can mark correct answer where appropriate

4. **Parent Message Generator**  
   - Short, polite, SMS-length messages  
   - Tone configurable (e.g., polite, firm, appreciative)

5. **Behaviour / Observation Note**  
   - Formal behaviour note for school records  
   - Includes summary, issue, positive traits and recommendation

6. **Emergency 20-Minute Lesson Plan**  
   - Quick backup when a teacher has no prep time  
   - One main activity, one exit question

7. **Progress Heatmap**  
   - Text-based bar visualisation with `█` and `▒`  
   - Short summary of class performance

---

## 🏗️ 3. Architecture – Three Interfaces, One Brain

```text
ai-classroom-manager/
│
├── config.py          # API client + model configuration (OpenRouter / OpenAI)
├── features.py        # Core AI features (all 7 tools)
├── main.py            # CLI interface (terminal app)
├── app.py             # Flask web interface (HTML templates + CSS)
├── streamlit_app.py   # Streamlit dashboard
│
├── templates/         # Flask HTML templates
│   ├── base.html
│   └── index.html
│
├── static/
│   └── style.css      # Custom Bootstrap-inspired styling for Flask UI
│
├── screenshots/       # Project screenshots used in README
│   ├── cli world.png
│   ├── flask world screen A.png
│   ├── flask world screen B.png
│   └── streamlit screenshot.png
│
└── .env               # Local environment variables (never committed)


All three interfaces call functions from features.py.

config.py decides whether you are using OpenRouter or OpenAI and sets the client + DEFAULT_MODEL.

🧩 4. Tech Stack

Language: Python 3.12

Core Libraries:

openai (OpenAI-compatible client, works for OpenAI & OpenRouter)

python-dotenv (load API keys from .env)

Web frameworks:

Flask (classic web app)

Streamlit (data-app/dashboard style)

Frontend (Flask):

HTML / Jinja2 templates

Basic Bootstrap-style layout via custom style.css

🔑 5. Configuration & API Keys

The project uses a single config.py file to configure the model and provider.

.env file (not committed to GitHub)

Create .env in ai-classroom-manager/:

# Choose which provider to use: "openrouter" or "openai"
AI_PROVIDER=openrouter

# If using OpenRouter
OPENROUTER_API_KEY=your_openrouter_key_here

# If using OpenAI directly
OPENAI_API_KEY=your_openai_key_here

config.py (simplified idea)

Reads AI_PROVIDER from .env

If openrouter → uses OpenRouter base URL + OPENROUTER_API_KEY

If openai → uses official OpenAI client + OPENAI_API_KEY

Sets a sensible default model, for example:

gpt-4.1-mini (OpenAI) or

google/gemini-2.0-flash-001 (OpenRouter, if available)

You can adjust the model string inside config.py to match your account.

🚀 6. Getting Started (Local Setup)
6.1 Clone the repository
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>/ai-classroom-manager

6.2 Create & activate virtual environment (Windows PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate

6.3 Install dependencies
pip install -r requirements.txt


If you don’t have a requirements.txt yet, you can generate one with:

pip freeze > requirements.txt

6.4 Add .env

Create .env as shown in section 5 and add your API key(s).

🧾 7. Using the CLI Interface

The CLI is handled by main.py.

From inside ai-classroom-manager/:

python main.py


You’ll see a menu like:

=== AI Classroom Manager Agent (CLI) ===
1. Generate Timetable
2. Generate Lesson Plan
3. Generate Test / Worksheet
4. Generate Parent Message
5. Generate Behaviour / Observation Note
6. Emergency 20-minute Lesson Plan
7. Progress Heatmap
0. Exit


Choose an option (1–7).

Answer the questions in the terminal.

The generated AI text appears directly in the console (you can copy it for WhatsApp, Word, or school records).

🌐 8. Using the Flask Web Interface

The Flask app lives in app.py and uses templates/ + static/style.css.

Run:

python app.py


Visit in your browser:

http://127.0.0.1:5000

Flask UI Highlights

Left sidebar with all classroom tools:

Timetable, Lesson Plan, Test / Worksheet, Parent Message, Behaviour Note, Emergency Plan, Progress Heatmap

Main area with:

Friendly headers like “Welcome, Teacher”

Clean forms with placeholders

Result boxes in blue (Generated …) for easy copy-paste

Footer credit:

“Powered by OpenRouter · Gemini / OpenAI · Built by Muhammad Shoaib”

CSS is handled via static/style.css and designed to look clean and teacher-friendly.

📊 9. Using the Streamlit Dashboard

The Streamlit version lives in streamlit_app.py.
It uses the same features.py functions as the CLI and Flask app.

Run:

streamlit run streamlit_app.py


Visit in your browser:

http://localhost:8502

Streamlit UI Highlights

Sidebar radio menu with the same features:

Generate Timetable / Lesson Plan / Test / Parent Message / Behaviour Note / Emergency Plan / Progress Heatmap

Clean card layout with:

Inputs on top

Generated result in a green success box at the bottom

Top banner text:

“Your personal teaching assistant — powered by OpenRouter / OpenAI (same brain as your CLI & Flask app).”

This version is ideal for live demos and can be deployed to Streamlit Cloud for public links.

🖼️ 10. Screenshots

All screenshots are stored under screenshots/ so GitHub can render them directly.

CLI View

Flask Web UI – Main Layout

Streamlit Dashboard

🌍 11. Possible Deployments (Next Steps)

Some ideas for future improvement and hosting:

Streamlit Cloud – one-click deploy of streamlit_app.py for a public URL

Flask hosting – deploy app.py on:

Render / Railway / PythonAnywhere

Add database:

Store heatmaps, behaviour notes, and parent messages for each student

Add authentication:

Simple teacher login to protect student data

🙌 12. Credits & Acknowledgements

Author: Muhammad Shoaib

Purpose: Built as part of Agentic AI / AIDD course work and real classroom needs.

Special focus: Pakistani school context, teacher workload, exam-style outputs.

If you find this useful, feel free to ⭐ the repository or adapt it for your own school.