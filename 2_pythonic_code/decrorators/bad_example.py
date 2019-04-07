import mysql.connector

conn = mysql.connector.connect(
  host="192.168.99.102",
  user="root",
  passwd="test",
  database="user_db",
  port="3308"
)


def find_all():
    query = "SELECT * FROM users"
    try:
        cursor = conn.cursor()
        rows = cursor.execute(query)
        cursor.close()
        return rows
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))


def find_one_by_id(user_id):
    query = "SELECT * FROM users where id='%'"
    try:
        cursor = conn.cursor()
        row = cursor.execute(query, user_id)
        cursor.close()
        return row
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))


def find_one_by_name(name):
    query = "SELECT * FROM users where name='%'"
    try:
        cursor = conn.cursor()
        row = cursor.execute(query, name)
        cursor.close()
        return row
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))


users = find_all()
user_1 = find_one_by_id(1)
user_pete = find_one_by_name('pete')

"""
Something went wrong: 1146 (42S02): Table 'user_db.users' doesn't exist
Something went wrong: 1146 (42S02): Table 'user_db.users' doesn't exist
Something went wrong: 1146 (42S02): Table 'user_db.users' doesn't exist
"""