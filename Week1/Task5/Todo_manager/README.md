#  Personal To-Do Task Manager
**AI/ML Fellowship — Mini Project 1**

A simple task management application built with Python and Streamlit.

##  How to Run

# 1. Clone / navigate to the project folder
cd todo_manager

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py

## Project Structure

todo_manager/
│
├── app.py            # Streamlit single-page UI
├── task_manager.py   # Core OOP logic + file handling
├── tasks.json        # Auto-created JSON data store
├── requirements.txt  # Python dependencies
└── README.md         # This file

## Concepts Demonstrated

| Concept           | Where                                      |
|-------------------|--------------------------------------------|
| Functions         | `validate_priority`, `validate_date`, `format_task_row`, `_generate_id`, etc. |
| OOP               | `Task` class, `TaskManager` class          |
| File Handling     | `_load_tasks()`, `_save_tasks()` with JSON |
| Error Handling    | `try/except` blocks throughout             |
| Streamlit UI      | `app.py` — single-page interface           |

## Features

-  Add tasks with title, priority, and due date
-  View all tasks in a clean table
-  Filter by status (Pending / Completed) and priority
-  Mark tasks as completed
-  Delete tasks
-  Summary metrics (Total / Pending / Completed)
-  Persistent JSON storage
