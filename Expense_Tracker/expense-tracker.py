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
    tasks.append({"id": new_id,
                  "description": content,
                  "status": "todo",
                  "createdAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                  "updatedAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
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
            task["description"] = new_content
            task['updatedAt'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_tasks(tasks)
            print(f"Task (ID: {task_id}) updated.")
            return
    # Exception handling (ID error)
    print(f"Task (ID: {task_id}) not found.")


def delete_task(task_id):
    """
    Delete task which id is "task_id"
    :param task_id: (int) the task id to be deleted
    :return: none
    """
    tasks = load_tasks()
    new_tasks = [task for task in tasks if task["id"] != task_id]
    if len(new_tasks) == len(tasks):  # Exception handling (ID error)
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
        if task["id"] == task_id:
            task["status"] = "done"
            task['updatedAt'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_tasks(tasks)
            print(f"Task (ID: {task_id}) marked as done.")
            return
    print(f"Task (ID: {task_id}) not found.")  # Exception handling (ID error)


def mark_in_progress(task_id):
    """
    Mark task status to "In progress"
    :param task_id: (int) the task id to be marked in-progress
    :return: none
    """
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "in-progress"
            task['updatedAt'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_tasks(tasks)
            print(f"Task (ID: {task_id}) marked as in-progress.")
            return
    print(f"Task (ID: {task_id}) not found.")  # Exception handling (ID error)


def list_tasks(status):
    """
    list all tasks in certain status (contain all tasks)
    :param status: (str) tasks in which status to be listed.
    :return: none
    """
    found = False
    tasks = load_tasks()
    if status == "all":
        for task in tasks:
            print(
                f"Task ID: {task['id']}, Description: {task['description']}, Status: {task['status']}, Create DateTime: {task['createdAt']}, Update DateTime: {task['updatedAt']}")
            found = True
        if not found:
            print("There is no task in the list.")
    elif status in ("done", "todo", "in-progress"):  # list certain status tasks
        for task in tasks:
            if task['status'] == status:
                print(
                    f"Task ID: {task['id']}, Description: {task['description']}, Status: {task['status']}, Create DateTime: {task['createdAt']}, Update DateTime: {task['updatedAt']}")
                found = True
        if not found:
            print(f'There is no task in "{status}" status.')
    else:
        print(f'No such status: "{status}".')


def main():
    """
    Main function to judge command and do the corresponding tasks
    """
    command = sys.argv[1]
    # Add function
    if command == "add":
        if len(sys.argv) == 3:
            content = " ".join(sys.argv[2:])
            add_task(content)
        else:  # Exception handling
            print(f"Syntax Error for command '{command}'")
    # Update function
    elif command == "update":
        if len(sys.argv) == 4:
            task_id = int(sys.argv[2])
            new_content = " ".join(sys.argv[3:])
            update_task(task_id, new_content)
        else:  # Exception handling
            print(f"Syntax Error for command '{command}'")
    # Delete function
    elif command == "delete":
        if len(sys.argv) == 3:
            task_id = int(sys.argv[2])
            delete_task(task_id)
        else:  # Exception handling
            print(f"Syntax Error for command '{command}'")
    # Mark-done function
    elif command == "mark-done":
        if len(sys.argv) == 3:
            task_id = int(sys.argv[2])
            mark_done(task_id)
        else:  # Exception handling
            print(f"Syntax Error for command '{command}'")
    # Mark-in-progress function
    elif command == "mark-in-progress":
        if len(sys.argv) == 3:
            task_id = int(sys.argv[2])
            mark_in_progress(task_id)
        else:  # Exception handling
            print(f"Syntax Error for command '{command}'")
    # list function
    elif command == "list":
        if len(sys.argv) == 2:
            list_tasks("all")
        elif len(sys.argv) == 3:
            list_tasks(str(sys.argv[2]))
        else:
            print(f"Argument Count Error (Command: {command})")  # list command arg count error
    else:
        print(f'Unknown command: "{command}".')


if __name__ == "__main__":
    main()

#################################
"""
File: expense-tracker.py
Name: Zhi-Xiu Lin
-------------------------------
#todo: comment here
-------------------------------
Note.
- Please refer to README.md for the usage
"""
import argparse
import json
import os
import datetime

# Define the file name of json file
DATA_FILE = 'expenses.json'

def load_expenses():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def save_expenses(expenses):
    with open(DATA_FILE, 'w') as f:
        json.dump(expenses, f, indent=2)

def add_expense(description, amount):
    expenses = load_expenses()
    new_id = 1 if not expenses else expenses[-1]['id'] + 1
    today = datetime.date.today().isoformat()
    expenses.append({
        'id': new_id,
        'date': today,
        'description': description,
        'amount': amount
    })
    save_expenses(expenses)
    print(f"Expense added successfully (ID: {new_id})")

def list_expenses():
    expenses = load_expenses()
    print(f"{'ID':<4} {'Date':<12} {'Description':<12} {'Amount'}")
    for e in expenses:
        print(f"{e['id']:<4} {e['date']:<12} {e['description']:<12} ${e['amount']}")

def delete_expense(expense_id):
    expenses = load_expenses()
    new_expenses = [e for e in expenses if e['id'] != expense_id]
    if len(new_expenses) < len(expenses):
        save_expenses(new_expenses)
        print("Expense deleted successfully")
    else:
        print("Expense not found")

def summary(month=None):
    expenses = load_expenses()
    total = 0
    for e in expenses:
        if month:
            if int(e['date'].split('-')[1]) == month:
                total += e['amount']
        else:
            total += e['amount']
    if month:
        print(f"Total expenses for August: ${total}")
    else:
        print(f"Total expenses: ${total}")

def main():
    parser = argparse.ArgumentParser(prog="expense-tracker")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("--description", required=True)
    add_parser.add_argument("--amount", type=float, required=True)

    subparsers.add_parser("list")

    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("--id", type=int, required=True)

    summary_parser = subparsers.add_parser("summary")
    summary_parser.add_argument("--month", type=int)

    args = parser.parse_args()

    if args.command == "add":
        add_expense(args.description, args.amount)
    elif args.command == "list":
        list_expenses()
    elif args.command == "delete":
        delete_expense(args.id)
    elif args.command == "summary":
        summary(args.month)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
"""
$ python expense_tracker.py add --description "Lunch" --amount 20
$ python expense_tracker.py list
$ python expense_tracker.py summary
$ python expense_tracker.py delete --id 1
$ python expense_tracker.py summary --month 8
"""
