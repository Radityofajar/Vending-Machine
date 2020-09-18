import sqlite3
conn = sqlite3.connect("database.db")

cur = conn.cursor()
cur.execute("SELECT harga FROM database")
stok = cur.fetchall()

print("harga :", stok[9])

cur.close()
conn.commit()
conn.close()