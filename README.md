# TODO List

## Description

Build a simple task management application with tags that helps users organize their daily activities.

## Installation

Python3 must be already installed.
```shell
git clone https://github.com/tarasmosiichuk01-ship-it/todo-list
cd todo-list
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open your browser at http://127.0.0.1:8000

---

## Features

The application should allow users to:
- Add new tasks and tags
- Mark tasks as completed and undo
- Delete & update tasks and tags from the list
- View all current tasks
