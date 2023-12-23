# 🚀 Project Management - Flask 📊

This Flask project is dedicated to creating a project management application with a robust backend architecture, developed in the form of an API. The main goal is to be able to connect any kind of Front End App (React, Vue.js), mobile (Android / iOS), and desktop apps (Electron, ...).

### Tasks

- [x] **Basic Structure**: Establish the fundamental structure for the project.
- [x] **Some Routes**: Develop initial routes for the project.
- [ ] **Create Controllers**: Implement controllers for projects, tasks, and settings.
- [ ] **Implement Database**: Set up the database using SQLite.

```

├── README.md
├── app.py
└── core
    ├── projects
    │   ├── __init__.py
    │   └── routes.py
    ├── settings
    │   ├── __init__.py
    │   └── routes.py
    └── tasks
        ├── __init__.py
        └── routes.py

```

### Commands

    python3 -m venv venv
    source venv/bin/activate

    flask run --port 8000 --debug
    
    deactivate

### Packages

- pip install Flask
- pip install Flask Flask-SQLAlchemy

