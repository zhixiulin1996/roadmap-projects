# Task-Tracker-CLI
## Basic Intorduction
Task tracker is a project used to track and manage your tasks. In this task, you will build a simple command line interface (CLI) to track what you need to do, what you have done, and what you are currently working on.
(This project is the idea of roadmap.sh (URL: https://roadmap.sh/projects/task-tracker))
## Functions
The application will run from the command line and store your tasks in a JSON file. Functions are listed as below:

1. Add, Update, and Delete tasks
2. Mark a task as in progress or done
3. List all tasks
4. List all tasks that are done
5. List all tasks that are not done
6. List all tasks that are in progress

## Usage
The commands for this application are listed as below:

1. Add task (`python3 task-cli.py add "content"`)
2. Update task (`python3 task-cli.py update [id] "new_content"`)
3. Delete task (`python3 task-cli.py delete [id]`)
4. Mark task as done/in-progress (`python3 task-cli.py mark-done/mark-in-progress [id]`)
5. List all tasks (`python3 task-cli.py list`)
6. List all tasks which are in todo/in-progress/done status (`python3 task-cli.py list todo/in-progress/done`)

## Notes

1. You can refer to <b><u>test_program.sh</u></b> for these command usage.
2. These command is for Linux OS, if your OS is Windows please use `python task-cli.py [command] [argv]`
