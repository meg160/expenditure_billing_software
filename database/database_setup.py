import sqlite3
from models.models import ExpenditureRecord

def add_expenditure(record):
    conn = sqlite3.connect('expenditure.db')
    cursor = conn.cursor()

    cursor.execute('INSERT INTO expenditures (date, amount, category, customer_id) VALUES (?, ?, ?, ?)',
                   (record.date, record.amount, record.category, record.customer_id))

    conn.commit()
    conn.close()

if __name__ == '__main__':
    record = ExpenditureRecord('2024-08-01', 100.0, 'Office Supplies', 1)
    add_expenditure(record)