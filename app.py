import sqlite3
conn = sqlite3.connect('library.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS books
(Bookid INTEGER PRIMARY KEY, Bookname Text, Author Text,Price INTEGER)''')
cursor.execute("INSERT INTO books (Bookname, Author, Price) VALUES (?, ?, ?)", ('Introduction to C programming', "Reema Thareja", 50))
conn.commit()
cursor.execute("SELECT * FROM books")
rows = cursor.fetchall()
for row in rows:
 print(row)
conn.close()