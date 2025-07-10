import sqlite3

db = "expenses.db"

def init_db():
    con = sqlite3.connect(db)
    cur = con.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL,
            note TEXT
        )
    ''')

    con.commit()
    con.close()

def init_balance():
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS balance (id INTEGER PRIMARY KEY, amount REAL)')
    cur.execute('SELECT * FROM balance WHERE id = 1')
    if not cur.fetchone():
        cur.execute('INSERT INTO balance (id, amount) VALUES (1, 0)')
    con.commit()
    con.close()

def get_balance():
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute('SELECT amount FROM balance WHERE id = 1')
    amt = cur.fetchone()[0]
    con.close()
    return amt

def add_funds(amount):
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute('UPDATE balance SET amount = amount + ? WHERE id = 1', (amount,))
    con.commit()
    con.close()



def add(amount, category, date, note):
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute('SELECT amount FROM balance WHERE id = 1')
    current = cur.fetchone()[0]
    if amount > current:
        con.close()
        return False  # not enough balance
    cur.execute('UPDATE balance SET amount = amount - ? WHERE id = 1', (amount,))
    cur.execute('''
        INSERT INTO expenses (amount, category, date, note)
        VALUES (?, ?, ?, ?)
    ''', (amount, category, date, note))
    con.commit()
    con.close()
    return True


def fetch(start=None, end=None):
    con = sqlite3.connect(db)
    cur = con.cursor()

    if start and end:
        cur.execute('SELECT * FROM expenses WHERE date BETWEEN ? AND ?', (start, end))
    else:
        cur.execute('SELECT * FROM expenses')

    rows = cur.fetchall()
    con.close()
    return rows

def fetch_by_category(category):
    con = sqlite3.connect(db)
    cur = con.cursor()

    cur.execute('SELECT * FROM expenses WHERE category = ?', (category,))
    rows = cur.fetchall()
    con.close()
    return rows

def fetch_by_month(yyyy_mm):
    con = sqlite3.connect(db)
    cur = con.cursor()

    cur.execute('SELECT * FROM expenses WHERE strftime("%Y-%m", date) = ?', (yyyy_mm,))
    rows = cur.fetchall()
    con.close()
    return rows
