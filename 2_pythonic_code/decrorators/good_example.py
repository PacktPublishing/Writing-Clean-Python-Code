import mysql.connector

conn = mysql.connector.connect(
    host="192.168.99.102",
    user="root",
    passwd="test",
    database="user_db",
    port="3308"
)


def query(func):
    def run(connection, *args, **kwargs):
        cursor = connection.cursor()
        result = False
        try:
            result = func(cursor, *args, **kwargs)
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
        finally:
            cursor.close()
        return result

    return run


@query
def find_all(cursor):
    return cursor.execute("SELECT * FROM users")


@query
def find_one_by_id(cursor, user_id):
    return cursor.execute("SELECT * FROM users where id='%'", user_id)

@query
def find_one_by_name(cursor, name):
    return cursor.execute("SELECT * FROM users where name='%'", name)


users = find_all(conn)
user_1 = find_one_by_id(conn, 1)
user_pete = find_one_by_name(conn, 'pete')

"""
Something went wrong: 1146 (42S02): Table 'user_db.users' doesn't exist
Something went wrong: 1146 (42S02): Table 'user_db.users' doesn't exist
Something went wrong: 1146 (42S02): Table 'user_db.users' doesn't exist
"""