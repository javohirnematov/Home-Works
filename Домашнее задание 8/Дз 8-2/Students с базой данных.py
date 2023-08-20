import sqlite3
connection = sqlite3.connect('mydatabase.db')
sql = connection.cursor()
sql.execute('CREATE TABLE IF NOT EXISTS students (id INTEGER, name TEXT, age INTEGER, grade TEXT);')
sql.execute('INSERT INTO students(id, name, age, grade) VALUES (101, "Java", 32, "5");')
sql.execute('INSERT INTO students(id, name, age, grade) VALUES (102, "Alex", 30, "5");')
sql.execute('INSERT INTO students(id, name, age, grade) VALUES (103, "Anton", 34, "4");')
sql.execute('INSERT INTO students(id, name, age, grade) VALUES (104, "Lena", 32, "4");')
sql.execute('INSERT INTO students(id, name, age, grade) VALUES (105, "Kseniya", 29, "3");')
sql.connection.commit()

def get_student_by_name(name):
    print(sql.execute(f'SELECT * FROM students WHERE name = "{name}";').fetchall())
def update_student_grade(name, grade):
    sql.execute(f'UPDATE students SET grade = "{grade}" WHERE name = "{name}";')
    print(f'Оценка студента {name} изменена на {grade}.')
    connection.commit()
def delete_student(name):
    sql.execute(f'DELETE FROM students WHERE name = "{name}";')
    print(f'Данные студента {name} удалены.')
    connection.commit()

while True:
    name = input('Введите имя студента: ')
    admin = int(input('1 - Получить информацию о студенте, '
                      '2 - Изменить оценку студента,'
                      '3 - Удалить данные студента: '))
    if admin == 1:
        get_student_by_name(name)
    elif admin == 2:
        grade = input(f'Введите новую оценку студенту {name}: ')
        update_student_grade(name, grade)
    elif admin == 3:
        delete_student(name)
    else:
         print('Неверный запрос')