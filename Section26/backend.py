import sqlite3

class Database:

    # this is the initalization of the object, in other languages its a constructor
    # when you pass the object instance to these functions, you need to have the self parameter in there
    # when you initalize the object in the front end, it is sending that argument to the self here
    # init function accepting the db arguement from the fb
    def __init__(self, db):
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
        conn.commit()
        conn.close()

    def insert(self,title, author,year,isbn):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO books VALUES (NULL, ?,?,?,?)" (title,author,year,isbn))
        conn.commit()
        conn.close()

    def view(self):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM book")
        rows = cur.fetchall()
        conn.close()
        return rows

    def search(self,title="", author="", year="", isbn=""):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author,year,isbn))
        rows = cur.fetchall()
        conn.close()
        return rows

    def delete(self,id):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM book WHERE id=?",(id,))
        conn.commit()
        conn.close()

    def update(self,id,title, author, year):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("UPDATE book SET title=?m author=?, year=?, isbn=? WHERE id=?",(id, title,author,year,isbn))
        conn.commit()
        conn.close()

