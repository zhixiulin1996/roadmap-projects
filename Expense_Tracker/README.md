# Expense Tracker CLI
A simple command-line tool to help you record, update, delete, and summarize your daily expenses. All data is stored locally in a JSON file, making it lightweight and easy to use.The project idea is inspired by [roadmap.sh](https://roadmap.sh/projects/expense-tracker).
---
## Features
- Add new expense records with description, amount, and optional date(in yyyy/mm/dd form)
- Update existing records by ID
- Delete expenses
- List all recorded expenses
- Summarize total spending by [toatl],by [year] or by [year/month]
- Stores data in a structured JSON file
- Includes an example shell script (`example.sh`) to demonstrate usage
---
## Requirements
- Python 3.7+
- Modules:
  - `argparse`
  - `json`
  - `datetime`
  - `os`
---
## Usage
Run the CLI tool using:
```bash
python expense_tracker.py [command] [options]
```
### Available Commands
|Command|Description|
|---|---|
|`add`|	Add a new expense record|
|`update`|	Update an existing expense by ID|
|`delete`|	Delete an expense by ID|
|`list` |List all expenses|
|`summary`|Show total expenses (overall, yearly, monthly)|

### Examples
You can also run the included example.sh to see sample usage:
```bash
bash example.sh
```
Or use commands manually:

1. Add an expense
```bash
python expense_tracker.py add --description "Lunch" --amount 12.5 --date 2025/11/03
```
2. Update an expense
```bash
python expense_tracker.py update --id 3 --amount 15.0
```
3. Delete an expense
```bash
python expense_tracker.py delete --id 3
```
4. List all expenses
```bash
python expense_tracker.py list
```
5. Summarize expenses
```bash
python expense_tracker.py summary --year 2025 --month 11
```
## Data Storage
All expense records are saved in a local file named `expenses.json`. Each record includes:

```json
{
  "id": 1,
  "date": "2025-11-03",
  "description": "Lunch",
  "amount": 12.5
}
```
## Testing
You can modify `example.sh` to test different scenarios or integrate with other scripts.

## License
This project is open-source and free to use for personal or educational purposes.
