import mysql.connector
from mysql.connector import errorcode

if __name__ == '__main__':
    try:
        config = {
            'user': 'root',
            'password': '1shuiyouwen21',
            'database': 'python_practice',
            'use_unicode': 'True',
        }
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        cursor.execute('create table user(id varchar(20) primary key,name varchar(20))')
        cursor.execute('insert into user (id,name) values (%s,%s)', ['1', 'Michael'])
        rowcount = cursor.rowcount
        print('rowcount' + str(rowcount))
        conn.commit()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('用户名或密码错误')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print('数据库不存在')
        else:
            print(err)
    else:
        cursor.close()
        conn.close()
