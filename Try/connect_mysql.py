import pymysql

con = pymysql.Connect(host="localhost",port=3306,user="root",passwd="",db="db",charset="utf8")
print("check:",con)