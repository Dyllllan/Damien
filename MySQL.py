import mysql.connector
from mysql.connector import Error
import requests as rq
import  re
def create_con ():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Ww13318343897',
            database='project',
            port=3306,
            charset='utf8mb4'
        )
        
        if connection.is_connected():
            print("connected successfully!") 
            return connection
            
    except Error as e:
        print(f"connected failed: {e}")
        return None

def insert_entry(id:int,url:str,name:str):
    connection = create_con()
    cursor = connection.cursor()
    result = "insert into data1 values(%d,'%s','%s')"%(id,url,name)#mysql'string arguments require '' (单引号)
    #print(result)
    cursor.execute(result)
    connection.commit()
    connection.close()
# def look_up():
def delete_entry():
    connection = create_con()
    cursor = connection.cursor()
    cursor.execute("delete from data1")
    connection.commit()
    connection.close()
# def manipulate_entry():
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
}

response = rq.get("https://pic.netbian.com/",headers=header)
response.encoding = response.apparent_encoding
parr = re.compile('src="(/u.*?)".alt="(.*?)"') # 匹配图片链接和图片名字
image = re.findall(parr,response.text)
id = 1
for i in image:
    insert_entry(id,i[0],i[1])
    id = id + 1
#delete_entry()