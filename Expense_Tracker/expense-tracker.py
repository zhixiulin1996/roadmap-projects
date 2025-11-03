"""
File: expense-tracker.py
Name: Zhi-Xiu Lin
-------------------------------
This program is a simple expense tracker to manage your finances. 
The application allows users to add, delete, update and view their expenses.
Also, this application also provides a summary of the expenses.
-------------------------------
Note.
- Please refer to README.md for the usage
"""
import argparse
import json
import os
from datetime import datetime,date

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

def add_expense(description, amount, date_in=""):
    """
    Add an expense record to application
    :param description: (str) the description of the added expense
    :param amount: (float) the price of added expense
    :param date: (str) the date of added expense in "yyyy/mm/dd" form
    :return: none
    """
    expenses = load_expenses()
    new_id = 1 if not expenses else expenses[-1]['id'] + 1
    amount = round(amount, 2) # round to 2 decimal
    if date_in:
        dt = datetime.strptime(date_in, "%Y/%m/%d").date().isoformat()
    else:
        dt = date.today().isoformat() # to ISO 8601 format string
    expenses.append({'id': new_id,
        'date': dt,
        'description': description,
        'amount': amount
    })
    save_expenses(expenses)
    print(f"Expense added successfully (ID: {new_id})")

def update_expense(expense_id, description=None, amount=None, date_in=None):
    """
    Update an expense record to application
    :param expense_id: (int) expense id to be updated
    :param description: (str) the description of the updated expense
    :param amount: (float) the price of updated expense
    :param date: (str) the date of updated expense in "yyyy/mm/dd" form
    :return: none
    """
    expenses = load_expenses()
    updated = False
    if date_in:
        dt = datetime.strptime(date_in, "%Y/%m/%d").date().isoformat()

    for e in expenses:
        if e['id'] == expense_id:
            updated = True
            e["date"] = dt if date_in else e['date']
            e['description'] = description if description else e['description']
            e['amount']= round(amount,2) if amount else e['amount'] # round to 2 decimal
            print(f"Expense updated successfully")
            save_expenses(expenses)
            return
    if not updated:
        print("Expense not found")


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
    """
    delete an expense 
    :param expense_id: (int) expense id to be deleted
    :return: none
    """
    expenses = load_expenses()
    new_expenses = [e for e in expenses if e['id'] != expense_id]
    if len(new_expenses) < len(expenses):
        save_expenses(new_expenses)
        print("Expense deleted successfully")
    else:
        print("Expense not found")

def summary(year=None,month=None):
    """
    Summary total expense of the tracker, or user can specify the year and month summary 
    :param year: (int) year that user wants to summary expense
    :param month: (int) month that user wants to summary expense
    :return: none
    """
    expenses = load_expenses()
    total = 0
    d = {1:"Jan",2:"Feb",3:"Mar",4:"Apr",5:"May",6:"Jun",7:"Jul",8:"Aug",9:"Sep",10:"Oct",11:"Nov",12:"Dec"}
    
    # Data operation
    for e in expenses:
        if year:
            if month: # summary year month
                if int(e['date'].split('-')[0]) == year and int(e['date'].split('-')[1]) ==month:
                    total += e['amount']
            else: # summary year
                if int(e['date'].split('-')[0]) == year:
                    total += e['amount']
        else: #only summary command
            total += e['amount']
    
    # Inform User the summary result
    if not year and month:
        print("Invalid Usage. Please refer to [--help].")
    elif month and month not in [i for i in range(1,13)]:
        print("Month should be an interger between 1 and 12.")
    else:
        if year:
            if month: # summary year month
                print(f"Total expenses for {year}/{d[month]}: ${round(total,2)}")
            else: # summary year
                print(f"Total expenses for {year}: ${round(total,2)}")
        else: #only summary command
            print(f"Total expenses: ${round(total,2)}")

        
def build_parser():
    """
    Build and return the command-line argument parser for the expense-tracker application.
    This function sets up a main parser with subcommands to handle various expense-related operations:
    - add: Add a new expense record with description, amount, and optional date.
    - update: Update an existing expense record by ID, with optional new description, amount, or date.
    - list: Display all recorded expenses.
    - delete: Remove an expense record by ID.
    - summary: Show total expenses, either overall, by year, or by specific year/month.

    :return: An argparse.ArgumentParser object configured with all supported subcommands and arguments.
    """
    # New main parser
    parser = argparse.ArgumentParser(prog="expense-tracker")
    subparsers = parser.add_subparsers(dest="command") #subparser name ="command"(i.e. parser.command will contain command below)

    # Add function
    add_parser = subparsers.add_parser("add",help="Add a new expense record")
    add_parser.add_argument("--date",metavar="[yyyy/mm/dd]",help='Date of expense in "yyyy/mm/dd" form. If not provided, will be today by default')
    add_parser.add_argument("--description", required=True,metavar="[description]",help="Short description of the expense (e.g. Lunch, Taxi)")
    add_parser.add_argument("--amount", type=float, required=True,metavar="[price]",help="Amount spent in dollars (e.g. 12.5)")

    # Update function
    update_parser = subparsers.add_parser("update",help="Update an expense record")
    update_parser.add_argument("--id", type=int,metavar="[id_number]", required=True, help="The expense ID you want to update")
    update_parser.add_argument("--date",metavar="[yyyy/mm/dd]",help='Date of expense in "yyyy/mm/dd" form. (If not provided, will not be changed)')
    update_parser.add_argument("--description",metavar="[description]",help="Short description of the expense (e.g. Lunch, Taxi)(If not provided, will not be changed)")
    update_parser.add_argument("--amount", type=float, metavar="[price]",help="Amount spent in dollars (e.g. 12.5)(If not provided, will not be changed)")

    # list function
    subparsers.add_parser("list",help="List all expenses")

    # delete function
    delete_parser = subparsers.add_parser("delete", help="Delete an expense")
    delete_parser.add_argument("--id", type=int,metavar="[id_number]", required=True, help="The expense ID you want to delete")

    # Summary function
    summary_parser = subparsers.add_parser("summary",help="Summary total expense for [total] or [year] or [year/month]")
    summary_parser.add_argument("--year", type=int, metavar="[yyyy]",help='Year you want to summary expense.')
    summary_parser.add_argument("--month", type=int, metavar="[mm]",help='Month you want to summary expense.(SHOULD use with --year)')

    return parser


def main():
    """
    Entry point for the expense-tracker command-line application.

    This function builds the argument parser, parses user input from the command line,
    and dispatches the appropriate function based on the selected subcommand.

    Please refer to build_parser() for supported commands.(If no valid command is provided, the help message will be displayed.)
    """
    
    # build parser and parse user command
    parser = build_parser()
    args = parser.parse_args()

    # Judge command and run corresponding function
    if args.command == "add":
        add_expense(args.description, args.amount, args.date)
    elif args.command == "list":
        list_expenses()
    elif args.command == "delete":
        delete_expense(args.id)
    elif args.command == "summary":
        summary(args.year,args.month)
    elif args.command == "update":
        update_expense(args.id, args.description, args.amount, args.date)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
