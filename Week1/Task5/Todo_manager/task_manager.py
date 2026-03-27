import json
import os
from datetime import datetime

class Task:
    def __init__(self, task_id: int, title: str, priority: str, due_date: str):
        self.task_id   = task_id
        self.title     = title
        self.priority  = priority          # "High" | "Medium" | "Low"
        self.due_date  = due_date          # "YYYY-MM-DD" string
        self.completed = False
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M")

    def mark_complete(self):
        self.completed = True

    def to_dict(self) -> dict:
        return {
            "task_id":    self.task_id,
            "title":      self.title,
            "priority":   self.priority,
            "due_date":   self.due_date,
            "completed":  self.completed,
            "created_at": self.created_at,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        task = cls(
            task_id  = data["task_id"],
            title    = data["title"],
            priority = data["priority"],
            due_date = data["due_date"],
        )
        task.completed  = data.get("completed", False)
        task.created_at = data.get("created_at", "N/A")
        return task

    def __repr__(self) -> str:
        status = "✔" if self.completed else "✘"
        return f"[{status}] ({self.task_id}) {self.title} | {self.priority} | Due: {self.due_date}"

class TaskManager:
    def __init__(self, filepath: str = "tasks.json"):
        self.filepath = filepath
        self.tasks: list[Task] = []
        self._load_tasks()

    def _load_tasks(self):
        if not os.path.exists(self.filepath):
            self.tasks = []
            return

        try:
            with open(self.filepath, "r") as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(item) for item in data]
        except (json.JSONDecodeError, KeyError) as e:
            print(f"Warning: Could not load tasks ({e}). Starting fresh.")
            self.tasks = []

    def _save_tasks(self):
        try:
            with open(self.filepath, "w") as f:
                json.dump([task.to_dict() for task in self.tasks], f, indent=4)
        except OSError as e:
            raise OSError(f"Failed to save tasks: {e}")

    def _generate_id(self) -> int:
        if not self.tasks:
            return 1
        return max(task.task_id for task in self.tasks) + 1

    def _find_task(self, task_id: int) -> Task | None:
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None

    def add_task(self, title: str, priority: str, due_date: str) -> Task:
        title = title.strip()
        if not title:
            raise ValueError("Task title cannot be empty.")

        validate_priority(priority)
        validate_date(due_date)

        new_task = Task(
            task_id  = self._generate_id(),
            title    = title,
            priority = priority,
            due_date = due_date,
        )
        self.tasks.append(new_task)
        self._save_tasks()
        return new_task

    def complete_task(self, task_id: int) -> Task:
        task = self._find_task(task_id)
        if task is None:
            raise ValueError(f"No task found with ID {task_id}.")
        if task.completed:
            raise ValueError(f"Task '{task.title}' is already completed.")

        task.mark_complete()
        self._save_tasks()
        return task

    def delete_task(self, task_id: int) -> str:
        task = self._find_task(task_id)
        if task is None:
            raise ValueError(f"No task found with ID {task_id}.")

        self.tasks.remove(task)
        self._save_tasks()
        return task.title

    def get_all_tasks(self) -> list[Task]:
        return self.tasks

    def get_filtered_tasks(self, status: str = "All", priority: str = "All") -> list[Task]:
        result = self.tasks

        if status == "Pending":
            result = [t for t in result if not t.completed]
        elif status == "Completed":
            result = [t for t in result if t.completed]

        if priority != "All":
            result = [t for t in result if t.priority == priority]

        return result

    def get_summary(self) -> dict:
        total     = len(self.tasks)
        completed = sum(1 for t in self.tasks if t.completed)
        pending   = total - completed
        return {"total": total, "completed": completed, "pending": pending}

def validate_priority(priority: str):
    allowed = {"High", "Medium", "Low"}
    if priority not in allowed:
        raise ValueError(f"Priority must be one of {allowed}. Got: '{priority}'")

def validate_date(date_str: str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError(f"Due date must be in YYYY-MM-DD format. Got: '{date_str}'")


def format_task_row(task: Task) -> dict:
    return {
        "ID":        task.task_id,
        "Title":     task.title,
        "Priority":  task.priority,
        "Due Date":  task.due_date,
        "Status":    "Done" if task.completed else "🕐 Pending",
        "Created":   task.created_at,
    }
