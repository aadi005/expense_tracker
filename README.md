# Personal Expense Tracker (CLI)

Aadi's Python-based personal finance tool — track expenses, manage balance, set monthly budgets, and get real-time visual and financial insights, all from your terminal.

---

## Features

- Add & filter expenses by category or month
- Add funds and track current balance
- Visualize spending using pie & bar charts (Matplotlib)
- Budget alerts (time-weighted monthly analysis)
- Export to CSV with totals
- Clean and minimal CLI interface

---

## Tech Stack

- Python 3.9+
- SQLite (built-in)
- Matplotlib

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone git@github.com:aadi005/expense_tracker.git
cd expense_tracker
```

### 2. Install required packages

```bash
python install_requirements.py
```

### 3. Run the app

```bash
python main.py
```

---

## Example Flow

```bash
1. Add Money             → 10000
2. Add Expense           → 3500 (Food)
3. View by Month         → November 2024
4. Visualize All         → Pie and Bar Charts
5. Export to CSV         → all_expenses.csv
6. Budget Alert          → Triggered if daily threshold exceeded
```

---

## Directory Structure

```
expense_tracker/
├── main.py                # CLI interface
├── db.py                  # SQLite operations and balance logic
├── visualize.py           # Matplotlib charts
├── export.py              # CSV exporter
├── install_requirements.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Example .gitignore

```
__pycache__/
*.pyc
*.db
.env
.idea/
.vscode/
```

---

## Author

Aaditya Goel

---

## License

This project is open-source and free to use.
