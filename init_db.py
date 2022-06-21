import sqlite3

connection = sqlite3.connect(r'\Users\avaug\Downloads\sqlite-tools-win32-x86-3380500\sqlite-tools-win32-x86-3380500\ticket.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO tickets (firstname, lastname, issuetype) VALUES (?, ?, ?)",
            ('Joe', 'Snuffy', 'Account_issue')
            )

cur.execute("INSERT INTO tickets (firstname, lastname, issuetype) VALUES (?, ?, ?)",
            ('Joe', 'Snuffy', 'Email_issue')
            )

connection.commit()
connection.close()