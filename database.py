import sqlite3
import hashlib

class DATABASE:
    def __init__(self):
        self.conn = sqlite3.connect("userData.db", check_same_thread=False)
        self.cur = self.conn.cursor()
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS userData (
                id INTEGER PRIMARY KEY,
                username VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL
            )
        """)
        self.conn.commit()

    def sign_up(self, name, password):
        self.cur.execute("SELECT username FROM userData WHERE username = ?", (name,))
        vari = self.cur.fetchone()
        if self.cur.fetchone() is None:
            password_hash = hashlib.sha256(password.encode()).hexdigest()
            self.cur.execute("INSERT INTO userData (username, password) VALUES (?, ?)", (name, password_hash))
            self.conn.commit()
            return True
        else:
            return False

    def log_in(self, username, password):
        hash_password = hashlib.sha256(password.encode()).hexdigest()
        self.cur.execute(f"SELECT username FROM userData WHERE username = '{username}' AND password = '{hash_password}'") #This line is an vulnerability.
        varri = self.cur.fetchone()
        if varri != None:
            return True
        else:
            return False
        


    def __del__(self):
        self.conn.close()
