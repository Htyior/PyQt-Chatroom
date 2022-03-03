import sqlite3

class DB_function:
    def __init__(self):
        pass

    # Creating the Database
    def db_create(self):
        con = sqlite3.connect('C:/Users/Hoss/Learning_Python/Learn/Qt/Qt_project/lib/Database.db')
        return con
    
    # Login action: check if username and password are right
    def login_db(self, con, name, password):
        password = "('" + password + "',)"
        cursorObj = con.execute(f"SELECT password FROM users WHERE username = '{name}'")
        for row in cursorObj:
            if str(row) == str(password):
                return True
            else:
                return False

    # Searching for username: Chaeck if username exist
    def db_search(self, con, username):
        cursorObj = con.execute(f"SELECT EXISTS(SELECT 1 FROM users WHERE username='{username}')")
        for row in cursorObj:
            if str(row) == "(0,)":
                return False
            elif str(row) == "(1,)":
                return True

