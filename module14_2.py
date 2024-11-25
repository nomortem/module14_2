import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()


cursor.execute('''
DELETE FROM Users WHERE id = 6
''')

cursor.execute("SELECT COUNT(*) FROM users")
total_users = cursor.fetchone()[0]

cursor.execute("SELECT SUM(balance) FROM users")
all_balances = cursor.fetchone()[0]

if total_users > 0:
    average_balance = all_balances / total_users
else:
    average_balance = 0

print(average_balance)

connection.commit()
connection.close()