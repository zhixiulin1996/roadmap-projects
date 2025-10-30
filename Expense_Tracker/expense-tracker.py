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
    """
    Input: None
    :return: python list (w/ or w/o dictionaries in the list)
    """
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def save_expenses(expenses):
    """
    Save expense data to json file
    :param expenses: (list) consists of many dictionaries
    :return: none
    """
    with open(DATA_FILE, 'w') as f:
        json.dump(expenses, f, indent=2)

def add_expense(description, amount):
    """
    Add an expense record to application
    :param description: (str) the description of the added expense
    :param amount: (float) the price of added expense
    :return: none
    """
    expenses = load_expenses()
    new_id = 1 if not expenses else expenses[-1]['id'] + 1
    today = datetime.date.today().isoformat() # to ISO 8601 format string
    expenses.append({
        'id': new_id,
        'date': today,
        'description': description,
        'amount': amount
    })
    save_expenses(expenses)
    print(f"Expense added successfully (ID: {new_id})")

def list_expenses():
    """
    list all expenses in the application
    :return: none
    """
    expenses = load_expenses()
    # print title name and define column width
    print(f"{'ID':<4} {'Date':<12} {'Description':<12} {'Amount'}")
    # iterate through the tracker and print
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
def build_parser():
    # todo: add comment
    # You can add command here
    # New main parser
    parser = argparse.ArgumentParser(prog="expense-tracker")
    subparsers = parser.add_subparsers(dest="command") #subparser name ="command"(i.e. parser.command will contain command below)

    # Add function
    add_parser = subparsers.add_parser("add",help="Add a new expense record")
    add_parser.add_argument("--description", required=True,metavar="[description]",help="Short description of the expense (e.g. Lunch, Taxi)")
    add_parser.add_argument("--amount", type=float, required=True,metavar="[price]",help="Amount spent in dollars (e.g. 12.5)")

    # list function
    subparsers.add_parser("list",help="List all expenses")

    # delete function
    delete_parser = subparsers.add_parser("delete", help="Delete an expense")
    delete_parser.add_argument("--id", type=int,metavar="[id_number]", required=True, help="The expense ID you want to delete")

    # Summary function
    summary_parser = subparsers.add_parser("summary")#todo: help
    summary_parser.add_argument("--month", type=int)#todo: help, metavar

    return parser


def main():
    # todo: comment here
    # build parser and parse user command
    parser = build_parser()
    args = parser.parse_args()

    # Judge command and run corresponding function
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
