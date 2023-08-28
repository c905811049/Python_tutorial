import cx_Oracle
import platform
print(platform.architecture())

con = cx_Oracle.connect("scott/123456@192.168.74.128:1521/ORCL.oracle")
print("sql连接:",con)
