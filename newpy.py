import requests as rq
import  re
import pymysql as mysql
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
}
response = rq.get("https://pic.netbian.com/",headers=header)
response.encoding = response.apparent_encoding
print(response.text)