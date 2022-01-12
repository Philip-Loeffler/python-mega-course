import sqlite3

# 1. connect to db
# 2. create a cursor object
# 3. write sql query
# 4. commit changes
# 5. close db connection

def create_table():
    # if you dont have a db, this line of code will handle it
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    # create the table
    # the if not exists means when this program runs, if this table was created, it wont break seeing the table try and create again
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    # insert data
    conn.commit()
    conn.close()

def insert(item, quantity, price):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    # insert data
    cur.execute("INSERT INTO store VALUES(?,?,?)", (item, quantity, price))
    conn.commit()
    conn.close()

insert("water glass", 10, 5)

def view():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

print(view())