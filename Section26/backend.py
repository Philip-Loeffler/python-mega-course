import sqlite3

class Database:

    # this is the initalization of the object, in other languages its a constructor
    # when you pass the object instance to these functions, you need to have the self parameter in there
    # when you initalize the object in the front end, it is sending that argument to the self here
    # init function accepting the db arguement from the fb
    # the init method is called when you initialize an instance of the object
    def __init__(self, db):
        conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
        self.conn.commit()

    def insert(self,title, author,year,isbn):
        self.cur.execute("INSERT INTO books VALUES (NULL, ?,?,?,?)" (title,author,year,isbn))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()
        return rows

    def search(self,title="", author="", year="", isbn=""):
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author,year,isbn))
        rows = self.cur.fetchall()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM book WHERE id=?",(id,))
        self.conn.commit()

    def update(self,id,title, author, year):
        cur.execute("UPDATE book SET title=?m author=?, year=?, isbn=? WHERE id=?",(id, title,author,year,isbn))
        self.conn.commit()


    # this one is called when the sript is exited
    def __del__(self)
        self.conn.close()