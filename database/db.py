import sqlite3

class DataBase:
    def __init__(self, chatid):
        db = sqlite3.connect('database/groups.db')
        cursor = db.cursor()
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS group_{chatid} (
            u_id TEXT,
            u_name TEXT,
            u_role TEXT,
            u_position TEXT
        )""")
    def adduser(self, chatid, userid, username):
        db = sqlite3.connect('database/groups.db')
        cursor = db.cursor()
        self.chatid = chatid
        self.userid = userid
        self.username = username
        cursor.execute(f"SELECT u_id FROM group_{chatid} WHERE u_id = {self.userid}")
        check = cursor.fetchall()
        if not check:
            cursor.execute(f"INSERT INTO group_{chatid} VALUES (?, ?, ?, ?)", (self.userid, self.username, "Мирный", "None"))
            db.commit()
        else:
            pass