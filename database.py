import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

def create_db():
    conn = sqlite3.connect("todo.db")
    conn = sqlite3.connect("fcb.db")
    cursor = conn.cursor()

    sql = '''
        CREATE TABLE IF NOT EXISTS Dostyp (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            level VARCHAR(1000) NOT NULL,
            level VARCHAR(1000) NOT NULL
        )
    '''
    cursor.execute(sql)

    # Добавление 3 уровней доступа (Первый, Второй, Третий)
    cursor.execute("INSERT INTO Dostyp(level) VALUES('Первый уровень')")
    cursor.execute("INSERT INTO Dostyp(level) VALUES('Второй уровень')")
    cursor.execute("INSERT INTO Dostyp(level) VALUES('Третий уровень')")

    sql = '''
        CREATE TABLE IF NOT EXISTS gos_persona (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,

@@ -27,7 +32,7 @@ def create_db():
        )
    '''
    cursor.execute(sql)
    conn.commit()
    

    sql = '''
        CREATE TABLE IF NOT EXISTS file (
        def create_db():
        reason VARCHAR(1000) NOT NULL,
        notes VARCHAR(1000) NOT NULL,
        photo VARCHAR(1000) NOT NULL,
        tickets VARCHAR(1000) NOT NULL,
        tickets VARCHAR(1000) NOT NULL
        )
        ''' 
    cursor.execute(sql)

def create_db():
    cursor.execute(sql)


    conn.commit()

    conn.close()

def get_users():
    conn = sqlite3.connect("todo.db")
    conn = sqlite3.connect("fcb.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM User")
    cursor.execute("SELECT * FROM Dostyp")
    users = cursor.fetchall()
    conn.close()
    return users

def auth_user(login, password):
    conn = sqlite3.connect("todo.db")
    conn = sqlite3.connect("fcb.db")
    cursor = conn.cursor()

    cursor.execute()
    def auth_user(login, password):
    else:
        return -1

def add_user(login, password):
    conn = sqlite3.connect("todo.db")
def add_citizens(name,surname, patronymic,is_wanted):
    conn = sqlite3.connect("fcb.db")
    cursor = conn.cursor()
    hashed_password = generate_password_hash(password)
6
    cursor.execute(
        "INSERT INTO file(reason,notes,photo,tickets)VALUES(?,?,?,?)",
        ('', '','','')
    )

    new_file_id = cursor.lastrowid

