#!/bin/bash

#Remove expenses.json if exist
[ -f expenses.json ] && rm expenses.json

# Add function test
echo "##### Add function test ####"
python3 expense-tracker.py add --amount 12.34 --description "test add function1" --date "2024/12/09"
python3 expense-tracker.py add --description "test add function2" --amount 56.78
python3 expense-tracker.py add --amount 1.5 --description "test add function3" --date "2025/06/30"
python3 expense-tracker.py add --amount 3.5 --description "test add function4" --date "2025/06/15"
python3 expense-tracker.py add --amount 3.5 --description "test add function5" --date "2025/06/15"
echo "# Add function test - to test if no argument input"
python3 expense-tracker.py add --amount 56.78
python3 expense-tracker.py add --description "test add function2" 
echo "[Current list]:"
python3 expense-tracker.py list

# Delete function test
echo "===================================================================================="
echo "##### Delete function test ####"
python3 expense-tracker.py delete --id 4
echo "# Delete function test - to test if no id found"
python3 expense-tracker.py delete --id 4
echo "[Current list]:"
python3 expense-tracker.py list

# Update function test
echo "===================================================================================="
echo "##### Update function test ####"
python3 expense-tracker.py update --id 3
python3 expense-tracker.py update --id 3 --description "Update function test" --amount 91.01 --date "2025/06/20"
echo "# Update function test - to test if no id found"
python3 expense-tracker.py update --id 4 
echo "[Current list]:"
python3 expense-tracker.py list

# Summary function test
echo "===================================================================================="
echo "##### Summary function test ####"
echo "# Summary function test - total summary"
python3 expense-tracker.py summary
echo "# Summary function test - 2024 summary"
python3 expense-tracker.py summary --year 2024
echo "# Summary function test - 2025/06 summary"
python3 expense-tracker.py summary --year 2025 --month 6
echo "# Summary function test - wrong input"
python3 expense-tracker.py summary --month 6
echo "[Current list]:"
python3 expense-tracker.py list