# AI-Assisted Lecture Note Generator (Final Year Project Core Prototype)

A full-stack Django web application designed to ingest meeting or lecture audio files, process them through an automated AI pipeline, and output structured Markdown lecture summaries, key takeaways, and raw transcripts.

## 🚀 Quick Start Guide

1. **Create and activate a Python virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   pip install django
   ```

3. **Apply database migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create a superuser (optional, for Django admin):**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the application:**
   Open your browser and navigate to `http://127.0.0.1:8000/`. Register a new account, log in, and start uploading lecture recordings!
