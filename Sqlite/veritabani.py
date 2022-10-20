import sqlite3

con = sqlite3.connect("kütüphane.db")

cursor = con.cursor()

con.close()