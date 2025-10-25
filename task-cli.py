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
    new_id = tasks[-1]["Task Id"] + 1 if tasks else 1
    tasks.append({"Task Id": new_id, "Content": content, "Status": "todo"})
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
        if task["Task Id"] == task_id:
            task["Content"] = new_content
            save_tasks(tasks)
            print(f"Task (ID: {task_id}) updated.")
            return
    # Exception handling
    print(f"Task (ID: {task_id}) not found.")


def delete_task(task_id):
    """
    Delete task which id is "task_id"
    :param task_id: (int) the task id to be deleted
    :return: none
    """
    tasks = load_tasks()
    new_tasks = [task for task in tasks if task["Task Id"] != task_id]
    if len(new_tasks) == len(tasks):  # Exception handling
        print(f"Task (ID: {task_id}) not found.")
    else:
        save_tasks(new_tasks)
        print(f"Task (ID: {task_id}) deleted.")


def mark_done(task_id):
    """
    Mark task status to "done"
    :param task_id: (int) the task id to be marked done
    :return: none
    """
    tasks = load_tasks()
    for task in tasks:
        if task["Task Id"] == task_id:
            task["Status"] = "done"
            save_tasks(tasks)
            print(f"Task (ID: {task_id}) marked as done.")
            return
    print(f"Task (ID: {task_id}) not found.")


def mark_in_progress(task_id):
    """
    Mark task status to "In progress"
    :param task_id: (int) the task id to be marked in-progress
    :return: none
    """
    tasks = load_tasks()
    for task in tasks:
        if task["Task Id"] == task_id:
            task["Status"] = "in-progress"
            save_tasks(tasks)
            print(f"Task (ID: {task_id}) marked as in-progress.")
            return
    print(f"Task (ID: {task_id}) not found.")


def list_tasks(status):
    """
    list all tasks in certain status (contain all tasks)
    :param status: (str) tasks in which status to be listed.
    :return: none
    """
    tasks = load_tasks()
    if status == "all":
        for task in tasks:
            print(f"Task ID: {task['Task Id']}, Content: {task['Content']}, Status: {task['Status']}")
    else:  # list certain status tasks
        for task in tasks:
            if task['Status'] == status:
                print(f"Task ID: {task['Task Id']}, Content: {task['Content']}, Status: {task['Status']}")


def main():
    """
    some comment here
    """
    # if len(sys.argv) < 3: # TODO
    #     print("Usage: task-cli.py [add|update|delete|mark-in-progress|mark-done] [args]")
    #     return

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
    elif command == "mark-done":
        task_id = int(sys.argv[2])
        mark_done(task_id)
    elif command == "mark-in-progress":
        task_id = int(sys.argv[2])
        mark_in_progress(task_id)
    elif command == "list":
        if len(sys.argv) == 2:
            list_tasks("all")
        elif len(sys.argv) == 3:
            list_tasks(str(sys.argv[2]))
        else:
            print(f"Argument Count Error (Command: {command})")  # list command arg count error
    else:
        print(f"Unknown command: {command}")


if __name__ == "__main__":
    main()

# add exception handling to make sure arg count correct
