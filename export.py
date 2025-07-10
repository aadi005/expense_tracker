import csv

def save(rows, filename):
    total = sum(row[1] for row in rows)

    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['ID', 'Amount', 'Category', 'Date', 'Note'])
        writer.writerows(rows)
        writer.writerow(['', 'Total', total, '', ''])

    print("\n✓ Exported to", filename)
