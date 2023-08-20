import sqlite3

connection = sqlite3.connect('database.db', check_same_thread=False)
sql = connection.cursor()
sql.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT, num TEXT, loc TEXT);')

def register(id, name, num, loc):
    sql.execute('INSERT INTO users VALUES(?, ?, ?, ?);', (id, name, num, loc))
    connection.commit()

def checker(id):
    check = sql.execute('SELECT id FROM users WHERE id=?;', (id,))
    if check.fetchone():
        return True
    else:
        return False

def name(id):
    name = (sql.execute(f'SELECT name FROM users WHERE id={id};').fetchall())
    return name