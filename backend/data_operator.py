import sqlite3
import time

# http://127.0.0.1:5000/putNewData?humidity=110&temperature=220&pressure=1017.3&ph=6&light=660
def insert_env_data(humidity, temperature, pressure, ph, light):
    conn = sqlite3.Connection('data/project.db')
    cursor = conn.cursor()
    sql = "INSERT INTO environment VALUES('{}', '{}', '{}', '{}', '{}', '{}')".format(humidity, temperature, pressure, ph, light, time.time())
    cursor.execute(sql)
    print(" Insert Successfully! ")
    conn.commit()
    conn.close()

def get_all_env_data():
    pass


def user_login(username, password):
    conn = sqlite3.Connection('data/project.db')
    cursor = conn.cursor()
    
    sql = "SELECT password FROM user WHERE id = '{}'".format(username)
    cursor.execute(sql)
    result = cursor.fetchone()
    if result is None:
        return False
    if password == result[0]:
        return True
    else:
        return False

def user_register(username, password):
    conn = sqlite3.Connection('data/project.db')
    cursor = conn.cursor()
    try:
        sql = "INSERT INTO user VALUES('{}', '{}', '0')".format(username, password)
        cursor.execute(sql)
        conn.commit()
    except:
        return False
    finally:
        return True