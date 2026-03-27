import streamlit as st
from datetime import date
from task_manager import TaskManager, format_task_row

st.set_page_config(
    page_title="To-Do Task Manager",
    page_icon="📝",
    layout="centered",
)

if "manager" not in st.session_state:
    st.session_state.manager = TaskManager("tasks.json")

manager: TaskManager = st.session_state.manager

st.title("Personal To-Do Task Manager")
st.caption("A simple task manager — add, track, and complete your tasks.")
st.divider()

summary = manager.get_summary()
col1, col2, col3 = st.columns(3)
col1.metric("Total Tasks",     summary["total"])
col2.metric("Pending",         summary["pending"])
col3.metric("Completed",        summary["completed"])
st.divider()

st.subheader("Add a New Task")

with st.form("add_task_form", clear_on_submit=True):
    title    = st.text_input("Task Title", placeholder="e.g. Complete fellowship assignment")
    priority = st.selectbox("Priority", ["High", "Medium", "Low"])
    due_date = st.date_input("Due Date", min_value=date.today())
    submitted = st.form_submit_button("Add Task")

if submitted:
    try:
        task = manager.add_task(
            title    = title,
            priority = priority,
            due_date = str(due_date),
        )
        st.success(f"Task added: **{task.title}** (ID: {task.task_id})")
        st.rerun()
    except ValueError as e:
        st.error(f"{e}")

st.divider()

st.subheader("Your Tasks")

filter_col1, filter_col2 = st.columns(2)
with filter_col1:
    status_filter   = st.selectbox("Filter by Status",   ["All", "Pending", "Completed"])
with filter_col2:
    priority_filter = st.selectbox("Filter by Priority", ["All", "High", "Medium", "Low"])

filtered_tasks = manager.get_filtered_tasks(
    status   = status_filter,
    priority = priority_filter,
)

if not filtered_tasks:
    st.info("No tasks found. Add one above!")
else:
    rows = [format_task_row(t) for t in filtered_tasks]
    st.dataframe(rows, use_container_width=True, hide_index=True)

st.divider()

st.subheader("Mark Task as Completed")

pending_tasks = manager.get_filtered_tasks(status="Pending")

if not pending_tasks:
    st.info("No pending tasks to complete.")
else:
    task_options = {f"[{t.task_id}] {t.title}": t.task_id for t in pending_tasks}
    selected = st.selectbox("Select a pending task", list(task_options.keys()))

    if st.button("Mark as Completed ✔"):
        try:
            task = manager.complete_task(task_options[selected])
            st.success(f"🎉 Task **'{task.title}'** marked as completed!")
            st.rerun()
        except ValueError as e:
            st.error(f"{e}")

st.divider()

st.subheader("Delete a Task")

all_tasks = manager.get_all_tasks()

if not all_tasks:
    st.info("No tasks to delete.")
else:
    delete_options = {f"[{t.task_id}] {t.title}": t.task_id for t in all_tasks}
    to_delete = st.selectbox("Select a task to delete", list(delete_options.keys()))

    if st.button("Delete Task"):
        try:
            title = manager.delete_task(delete_options[to_delete])
            st.success(f"Task **'{title}'** has been deleted.")
            st.rerun()
        except ValueError as e:
            st.error(f"{e}")

st.divider()
st.caption("To-Do Task Manager | AI/ML Fellowship Mini Project 1")
