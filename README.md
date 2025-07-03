# AI-Powered Resume Generator

## Overview
The AI-Powered Resume Generator is a web application that helps users create professional, ATS-compatible resumes using AI.  
It leverages **OpenAI GPT models** to dynamically generate resume content based on user-provided details, offers multiple template designs, and allows the generated resume to be downloaded as a PDF.

---

## Features
- **AI-Powered Content Generation**: Uses OpenAI GPT to create professional resume content dynamically.
- **Multiple Templates**: Choose from 3 visually distinct resume designs.
- **PDF Download**: Generate and download resumes in PDF format.
- **User-Friendly Interface**: Simple web form for user input.

---

## Folder Structure
```plaintext
resume-generator/
├── backend/
│   ├── __init__.py           # Backend initialization
│   ├── app.py                # Main Flask app
│   ├── generator.py          # AI-powered resume generation logic
│   ├── templates.py          # Resume templates (PDF generation)
├── frontend/
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css      # Styling for the UI
│   │   └── js/
│   │ 
