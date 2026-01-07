import mysql.connector
from mysql.connector import Error
def create_con ():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Ww13318343897',
            database='t1',
            port=3306,
            charset='utf8mb4'
        )
        
        if connection.is_connected():
            print("connected successfully!",end = '')
            return connection
            
    except Error as e:
        print(f"connected failed: {e}")
        return None

# def insert_entry(connection):
# def look_up():
# def delete_entry():
# def manipulate_entry():
connection = create_con()
