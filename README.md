# Python Excel Automation

A Python automation tool that combines multiple Excel files
into one report and removes duplicate rows.

## Features

- Merge multiple `.xlsx` files
- Remove duplicate rows
- Track the source file for each row
- Create output directories automatically
- Handle missing input directories and files

## Technology Stack

- Python
- Pandas
- OpenPyXL

## Installation

```bash
git clone https://github.com/ssubhale/python-excel-automation.git
cd python-excel-automation

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

## Usage

1. Create an `input` folder in the project directory.
2. Place your `.xlsx` files inside `input/`.
3. Run:

```bash
python main.py
```

4. Find the merged report at:

`output/merged_report.xlsx`

## Example Use Case

Combine daily sales spreadsheets from multiple branches
into one consolidated report.

## Future Improvements

- Add CSV support
- Add automated tests
- Add data validation and summary reports
-
