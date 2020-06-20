import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

user = (1, 'Amar Singh', 'amar##00934')
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)

users = [
    (2, 'Ganesh Yadav', 'chauhan@123'),
    (3, 'Prateek', 'Anabell_223'),
    (4, 'Neha Brar', 'Annefrank@9393'),
    (5, 'Ayushi Jain', '00xct1995')

]
cursor.executemany(insert_query, users)

select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)

connection.commit()


connection.close()
