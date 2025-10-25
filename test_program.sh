#!/bin/bash

#Remove tasks.json if exist
[ -f tasks.json ] && rm tasks.json

# Adding a new task
echo "Add New Task Test"
python3 task-cli.py add "Buy groceries_1"
python3 task-cli.py add "Buy groceries_2"
python3 task-cli.py add "Buy groceries_3"
python3 task-cli.py add "Buy groceries_4"
python3 task-cli.py add "Buy groceries_5"
echo "======================"

# Updating and deleting tasks
sleep 5
echo "Update/Delete Task Test (delete ID=1, update ID=3)"
python3 task-cli.py delete 1
python3 task-cli.py update 3 "Buy groceries_3 (updated version)"
echo "======================"

# Marking a task as in progress or done
sleep 5
echo "mark-done/mark-in-progress function Test (mark-done ID=4, mark-in-progress ID=5)"
python3 task-cli.py mark-in-progress 5
python3 task-cli.py mark-done 4
echo "======================"

# Listing all tasks
echo "list all tasks function Test"
python3 task-cli.py list
echo "======================"

# Listing tasks by status
echo "list all tasks in done/todo/in-progress status function Test"
echo "done tasks below: "
python3 task-cli.py list done
echo "-+-+-+-+-+-+-+-+"
echo "todo tasks below: "
python3 task-cli.py list todo
echo "-+-+-+-+-+-+-+-+"
echo "in-progress tasks below: "
python3 task-cli.py list in-progress