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
            FOREIGN KEY (dostyp_id) REFERENCES Dostyp(id)
        )
    '''
    cursor.execute(sql)
    conn.commit()
    sql = '''
        CREATE TABLE IF NOT EXISTS file (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            reason VARCHAR(1000) NOT NULL,
            notes VARCHAR(1000) NOT NULL,
            photo VARCHAR(1000) NOT NULL,
            tickets VARCHAR(1000) NOT NULL
            tickets VARCHAR(1000) NOT NULL,
        )
    '''
    cursor.execute(sql)
    conn.commit()
    conn.close()
def get_users():
    conn = sqlite3.connect("fcb.db")
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Dostyp")
    cursor.execute("SELECT * FROM User")
    users = cursor.fetchall()
    conn.close()
    return users

def auth_user(login, password):
    conn = sqlite3.connect("fcb.db")
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()


def add_citizens(name,surname, patronymic,is_wanted):
    conn = sqlite3.connect("fcb.db")
    cursor=conn.cursor()
    
    cursor.execute(
        "INSERT INTO file(reason,notes,photo,tickets)VALUES(?,?,?,?)",
        ('', '','','')
    )

    new_file_id = cursor.lastrowid
    cursor.execute(
        "INSERT INTO Citizens (name,surname, patronymic,is_wanted,file_id) VALUES (?,?,?,?,?)",
        (name,surname, patronymic,is_wanted,new_file_id)
    )

    #??????????????



    
def is_user_exists(login):
    conn = sqlite3.connect("fcb.db")
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM User WHERE login = ?", (login,))
    user = cursor.fetchone()

if __name__ == "__main__":
    create_db()
    add_citizens("tIMUR", "sHUPOAWLDKAWLJKD", "HZ", 1)
users = get_users()
    add_user("21", "21")
    add_user("user", "user")
    users = get_users()