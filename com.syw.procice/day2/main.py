import uuid
import mysql.connector
from mysql.connector import errorcode


def generate_code(num):
    codes = []
    for i in range(num):
        codes.append([str(uuid.uuid1())])
    return codes


def save_in_db(codes):
    create_table_sql = 'create table if not exists codes(id int(5) primary key not null auto_increment,' \
                       'code varchar(50) not null)'
    try:
        config = {
            'user': 'root',
            'password': '123456',
            'database': 'python_practice',
            'use_unicode': 'True',
        }
        connect = mysql.connector.connect(**config)
        cursor = connect.cursor()
        cursor.execute(create_table_sql)
        insert_sql = "insert into codes (code) VALUES (%s)"
        cursor.executemany(insert_sql, codes)
        connect.commit()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('用户名或密码错误')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print('数据库不存在')
        else:
            print(err)
    else:
        cursor.close()
        connect.close()


if __name__ == '__main__':
    codes = generate_code(200)
    save_in_db(codes)
