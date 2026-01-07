import requests as rq
import pymysql as mysql
response = rq.get("https://www.baidu.com/")
print(response)