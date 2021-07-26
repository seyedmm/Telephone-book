import sqlite3


def connect():
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS numbers(id INTEGER PRIMARY KEY, name TEXT, email VARCHAR, phone INTEGER)")
    conn.commit()
    conn.close()

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def add_number(name, email, phone):
    try:
        conn = sqlite3.connect('db.sqlite3')
        cur = conn.cursor()
        cur.execute("INSERT INTO numbers(name, email, phone) VALUES(?,?,?)", (name, email, phone))
        conn.commit()
        conn.close()
        return True
    except:
        return False
    
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def view():
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    cur.execute("SELECT * FROM numbers")
    rows = cur.fetchall()
    conn.close()
    return rows

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def delete(id):
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    cur.execute("DELETE FROM numbers WHERE id=?", (id))
    conn.commit()
    conn.close()

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def search_by_name(name):
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    cur.execute("SELECT * FROM numbers WHERE name=?", (name,))
    rows = cur.fetchall()
    conn.close()
    return rows

def search_by_id(id):
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    cur.execute("SELECT * FROM numbers WHERE id=?", (id,))
    rows = cur.fetchall()
    conn.close()
    return rows

def search_by_email(email):
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    cur.execute("SELECT * FROM numbers WHERE email=?", (email,))
    rows = cur.fetchall()
    conn.close()
    return rows

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

class Editor:
    def __init__(self, id):
        self.id = id


    def edit_name(self, name):
        conn = sqlite3.connect('db.sqlite3')
        cur = conn.cursor()
        cur.execute("UPDATE numbers SET name=? WHERE id=?", (name, self.id))
        conn.commit()
        conn.close()

    def edit_email(self, email):
        conn = sqlite3.connect('db.sqlite3')
        cur = conn.cursor()
        cur.execute("UPDATE numbers SET email=? WHERE id=?", (email, self.id))
        conn.commit()
        conn.close()

    def edit_phone(self, phone):
        conn = sqlite3.connect('db.sqlite3')
        cur = conn.cursor()
        cur.execute("UPDATE numbers SET phone=? WHERE id=?", (phone, id))
        conn.commit()
        conn.close()

    def edit_all(self, name, email, phone):
        conn = sqlite3.connect('db.sqlite3')
        cur = conn.cursor()
        cur.execute("UPDATE numbers SET name=?, email=?, phone=? WHERE id=?", (name, email, phone, self.id))
        conn.commit()
        conn.close()

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


connect()