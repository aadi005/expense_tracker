import matplotlib.pyplot as plt
from collections import defaultdict
import random

def pick_colors(keys):
    colors = {}
    for k in keys:
        colors[k] = "#" + ''.join(random.choices("0123456789ABCDEF", k=6))
    return colors

def pie(data):
    total = defaultdict(float)
    for _, amt, cat, _, _ in data:
        total[cat] += amt

    labels = list(total.keys())
    values = list(total.values())
    colors = pick_colors(labels)

    plt.pie(values, labels=labels, autopct='%1.1f%%', colors=[colors[k] for k in labels])
    plt.title("Spending by Category")
    plt.show()

def bar(data):
    daily = defaultdict(float)
    for _, amt, _, date, _ in data:
        daily[date] += amt

    days = sorted(daily)
    values = [daily[d] for d in days]

    plt.bar(days, values, color='skyblue')
    plt.xticks(rotation=45)
    plt.title("Daily Expenses")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.tight_layout()
    plt.show()
