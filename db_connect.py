import mysql.connector
from mysql.connector import Error

db_name = 'library_db'
host = 'localhost'
user = 'root'
password = '12@Wsxdr56'


try: 
    conn = mysql.connector.connect(
        database = db_name,
        host = host,
        user = user,
        password = password,
        
        
    )
    if conn.is_connected():
        print("Connections to MySQL databsse successful!")

    cursor = conn.cursor() #creating a cursor to act as a middle man between python and MySQL

    quary = "SELECT * FROM customer;"

    cursor.execute(quary)

    for row in cursor.fecthall():
        print(row)

except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if conn and conn.is_connected():
        cursor.close()
        conn.close()
        print("MySQL connection is closed")
