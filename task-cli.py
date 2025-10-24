"""
File: task-cli.py
Name: Zhi-Xiu Lin
-------------------------------
This is a project used to track and manage user's tasks.
In this task, you will build a simple command line interface (CLI) to track:
1. what you need to do?
2. what you have done?
3. what you are currently working on?
-------------------------------
Note.
- Please refer to README.md for the usage
"""
"""
Add, Update, and Delete tasks
Mark a task as in progress or done
List all tasks
List all tasks that are done
List all tasks that are not done
List all tasks that are in progress
"""
import json
import os
import sys

# Define the file name of json file
TASK_FILE = "tasks.json"


def load_tasks():
    """
    Input: None
    :return: python list (w/ or w/o dictionaries in the list)
    """
    # Check if the TASK_FILE exist
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    """
    Save tasks data to json file
    :param tasks: (list) consists of many dictionaries
    :return: none
    """
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def add_task(content):
    """
    Load current task data, add new task and give it an ID
    :param content: (str) the content of new task
    :return: none
    """
    tasks = load_tasks()
    new_id = tasks[-1]["id"] + 1 if tasks else 1
    tasks.append({"id": new_id, "content": content, "completed": False})
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_id})")


def update_task(task_id, new_content):
    """
    Updating task content
    :param task_id: (int) the ID of task
    :param new_content: (str) the content of the task
    :return: none
    """
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["content"] = new_content
            save_tasks(tasks)
            print(f"Task (ID: {task_id}) updated.")
            return
    # Exception handling
    print(f"Task (ID: {task_id}) not found.")


def delete_task(task_id):
    tasks = load_tasks()
    new_tasks = [task for task in tasks if task["id"] != task_id]
    if len(new_tasks) == len(tasks):
        print(f"Task {task_id} not found.")
    else:
        save_tasks(new_tasks)
        print(f"Task {task_id} deleted.")
    # Updating and deleting tasks
    # task-cli delete 1


def complete_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            save_tasks(tasks)
            print(f"Task {task_id} marked as completed.")
            return
    print(f"Task {task_id} not found.")


def main():
    """
    some comment here
    """
    if len(sys.argv) < 3:
        print("Usage: task-cli.py [add|update|delete|complete] [args]")
        return

    command = sys.argv[1]
    if command == "add":
        content = " ".join(sys.argv[2:])
        add_task(content)
    elif command == "update":
        if len(sys.argv) < 4:
            print("Usage: task-cli.py update <id> <new content>")
            return
        task_id = int(sys.argv[2])
        new_content = " ".join(sys.argv[3:])
        update_task(task_id, new_content)
    elif command == "delete":
        task_id = int(sys.argv[2])
        delete_task(task_id)
    elif command == "complete":
        task_id = int(sys.argv[2])
        complete_task(task_id)
    else:
        print(f"Unknown command: {command}")


if __name__ == "__main__":
    main()

"""
Usage:
python3 task-cli.py add "Buy groceries"
python3 task-cli.py update 1 "Buy groceries and cook dinner"
python3 task-cli.py complete 1
python3 task-cli.py delete 1
"""
"""
# Marking a task as in progress or done
task-cli mark-in-progress 1
task-cli mark-done 1

# Listing all tasks
task-cli list

# Listing tasks by status
task-cli list done
task-cli list todo
task-cli list in-progress

"""