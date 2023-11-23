import pymysql

def get_conn():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='950310',
        database='python_mysql',
        charset='utf8mb4'
    )

def query_data(sql):
    conn = get_conn()
    try:
        cursor = conn.cursor((pymysql.cursors.DictCursor))
        cursor.execute(sql)
        return cursor.fetchall()
    finally:
        conn.close()

def insert_or_update_data(sql):
    conn = get_conn()
    try:
        cursor = conn.cursor(())
        cursor.execute(sql)
        conn.commit()
    finally:
        conn.close()
if __name__ == "__main__":
    # sql = "insert user(name,sex,age,email) values('Rose','woman',30,'rose@gmail.com')"
    # insert_or_update_data(sql)

    sql = "select * from user"
    datas = query_data(sql)
    import pprint
    pprint.pprint(datas)