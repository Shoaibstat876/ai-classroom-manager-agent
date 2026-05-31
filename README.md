# AI Classroom Manager Agent

AI Classroom Manager Agent is an AI-powered educational automation tool built with **Python**, **Flask**, **Streamlit**, and **OpenRouter/Gemini-compatible APIs**.

The project helps teachers generate classroom resources such as timetables, lesson plans, worksheets, parent messages, behaviour notes, emergency lesson plans, and progress summaries. It includes multiple interfaces that share the same core AI logic.

## Live Demo

[View Streamlit App](https://ai-classroom-manager-agent-fcekwbbfn5sob7xbzcta4f.streamlit.app/)

## Project Overview

AI Classroom Manager Agent was created to support teachers with common classroom planning and communication tasks.

The project is designed as a multi-interface AI application with:

* Command-line interface
* Flask web interface
* Streamlit web interface
* Shared AI feature logic
* OpenRouter / OpenAI-compatible API configuration
* Modular Python structure

The main goal of this project was to practice AI application development, prompt-based automation, API integration, and multi-interface software design.

## Key Features

### Timetable Generator

Generates a weekly timetable for multiple classes and periods.

### Lesson Plan Generator

Creates structured lesson plans with learning objectives, warm-up activities, main activities, assessment ideas, and homework.

### Test / Worksheet Generator

Generates classroom test or worksheet content with different question types.

### Parent Message Generator

Creates professional parent messages in different tones such as polite, strict, or friendly.

### Behaviour Note Generator

Generates formal behaviour or observation notes for student discipline or academic performance.

### Emergency Lesson Plan Generator

Creates quick backup lesson plans for emergency or surprise classes.

### Progress Heatmap

Generates text-based progress summaries and percentage-style heatmaps.

## Interfaces

This project includes three interface options:

### 1. CLI Version

A terminal-based interface for running classroom automation features from the command line.

### 2. Flask Web App

A web-based interface using Flask, HTML templates, and CSS.

### 3. Streamlit App

A lightweight interactive web interface deployed with Streamlit.

## Tech Stack

* Python
* Flask
* Streamlit
* Jinja2
* HTML
* CSS
* OpenRouter / OpenAI-compatible client
* Gemini-compatible model access
* python-dotenv

## Project Structure

```bash
ai-classroom-manager/
├── app.py
├── main.py
├── streamlit_app.py
├── config.py
├── features.py
├── requirements.txt
├── templates/
│   ├── base.html
│   └── index.html
├── static/
│   └── style.css
├── screenshots/
│   ├── cli world.png
│   ├── flask world screen A.png
│   ├── flask world screen B.png
│   └── streamlit screenshot.png
└── README.md
```

## Installation and Setup

Clone the repository:

```bash
git clone https://github.com/Shoaibstat876/ai-classroom-manager-agent.git
```

Go to the project folder:

```bash
cd ai-classroom-manager-agent/ai-classroom-manager
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment on Windows:

```bash
.\.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file inside the project folder:

```env
AI_PROVIDER=openrouter
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

For OpenAI instead of OpenRouter, use:

```env
AI_PROVIDER=openai
OPENAI_API_KEY=your_openai_api_key_here
```

## Running the Project

### Run the CLI Version

```bash
python main.py
```

### Run the Flask Web App

```bash
python app.py
```

Then open:

```bash
http://127.0.0.1:5000/
```

### Run the Streamlit App

```bash
streamlit run streamlit_app.py
```

Then open:

```bash
http://localhost:8501/
```

## Screenshots

### CLI Version

![CLI](screenshots/cli world.png)

### Flask Web Interface

![Flask A](screenshots/flask world screen A.png)

![Flask B](screenshots/flask world screen B.png)

### Streamlit Interface

![Streamlit](screenshots/streamlit screenshot.png)

## What I Practiced

* Python application structure
* AI API integration
* Prompt-based automation
* Flask web development
* Streamlit app development
* CLI application design
* Shared business logic across multiple interfaces
* Environment variable handling
* Modular project organization
* Classroom workflow automation

## Security Notes

API keys are not stored directly in the code.

The project uses environment variables through a `.env` file. The `.env` file should stay local and should not be committed to GitHub.

Example:

```env
OPENROUTER_API_KEY=your_api_key_here
```

## Current Status

This is a functional AI classroom automation project with CLI, Flask, and Streamlit interfaces.

It is suitable as a portfolio project to demonstrate Python, AI API integration, prompt engineering, and educational workflow automation. It is not a production school management system yet.

## Future Improvements

* Add user authentication
* Add database storage
* Add saved classroom profiles
* Add export to PDF or DOCX
* Improve timetable conflict handling
* Add role-based teacher/admin views
* Add better UI design for the Flask version
* Add automated tests for core features
* Add deployment documentation for Flask
* Add structured logging and error handling

## Author

**Muhammad Shoaib Abdul Shakoor**

Focused on AI automation, full-stack development, backend APIs, frontend interfaces, and practical AI-native applications.

## License

This project is open for learning, demonstration, and portfolio purposes.
