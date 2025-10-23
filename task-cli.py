import sys, os, json

TASK_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task(content):
    tasks = load_tasks()
    new_id = tasks[-1]["id"] + 1 if tasks else 1
    tasks.append({"id": new_id, "content": content, "completed": False})
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_id})")

def update_task(task_id, new_content):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["content"] = new_content
            save_tasks(tasks)
            print(f"Task {task_id} updated.")
            return
    print(f"Task {task_id} not found.")

def delete_task(task_id):
    tasks = load_tasks()
    new_tasks = [task for task in tasks if task["id"] != task_id]
    if len(new_tasks) == len(tasks):
        print(f"Task {task_id} not found.")
    else:
        save_tasks(new_tasks)
        print(f"Task {task_id} deleted.")

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
test
"""
