from db import init_db, init_balance, add, fetch, fetch_by_category, fetch_by_month, get_balance, add_funds
from datetime import datetime
from visualize import pie, bar
from export import save

monthly_budget = 10000

def show(rows):
    total = 0
    for row in rows:
        print(row)
        total += row[1]
    print("\nTotal:", total)

def check_budget_alert(date):
    try:
        y, m, d = map(int, date.split('-'))
        now = datetime(y, m, d)

        total_days = (datetime(y, m % 12 + 1, 1) - datetime(y, m, 1)).days if m != 12 else 31
        passed_days = now.day

        ratio = passed_days / total_days
        expected_limit = monthly_budget * ratio

        month_key = date[:7]
        spent = sum(row[1] for row in fetch_by_month(month_key))

        if spent > expected_limit:
            print(f"\nAlert: You've spent ₹{spent:.0f} — that exceeds ₹{expected_limit:.0f} allowed by day {passed_days}")
    except:
        pass

def run():
    init_db()
    init_balance()

    while True:
        print("\n1. Add Money")
        print("2. Check Balance")
        print("3. Add Expense")
        print("4. View All")
        print("5. View by Category")
        print("6. View by Month")
        print("7. Visualize All")
        print("8. Visualize by Category")
        print("9. Visualize by Month")
        print("10. Export to CSV")
        print("11. Exit")

        opt = input("Select: ")

        if opt == "1":
            amt = float(input("Amount to add: "))
            add_funds(amt)
            print("✓ Money added")

        elif opt == "2":
            print("\nBalance:", get_balance())

        elif opt == "3":
            amt = float(input("Amount: "))
            cat = input("Category: ")
            raw_date = input("Date (YYYY-MM-DD) [leave blank for today]: ").strip()
            date = raw_date if raw_date else datetime.now().strftime("%Y-%m-%d")
            note = input("Note (optional): ")
            success = add(amt, cat, date, note)
            if not success:
                print("\nNot enough balance")
            else:
                check_budget_alert(date)

        elif opt == "4":
            show(fetch())

        elif opt == "5":
            cat = input("Category: ")
            show(fetch_by_category(cat))

        elif opt == "6":
            m = input("Month (YYYY-MM): ")
            show(fetch_by_month(m))

        elif opt == "7":
            data = fetch()
            pie(data)
            bar(data)

        elif opt == "8":
            cat = input("Category: ")
            data = fetch_by_category(cat)
            pie(data)
            bar(data)

        elif opt == "9":
            m = input("Month (YYYY-MM): ")
            data = fetch_by_month(m)
            pie(data)
            bar(data)

        elif opt == "10":
            print("\na. All")
            print("b. By Category")
            print("c. By Month")
            sub = input("Choose: ")

            if sub == "a":
                data = fetch()
                save(data, "all_expenses.csv")

            elif sub == "b":
                cat = input("Category: ")
                data = fetch_by_category(cat)
                save(data, f"{cat}_expenses.csv")

            elif sub == "c":
                m = input("Month (YYYY-MM): ")
                data = fetch_by_month(m)
                save(data, f"{m}_expenses.csv")

            else:
                print("Invalid")

        elif opt == "11":
            break

        else:
            print("Invalid input.")

if __name__ == "__main__":
    run()