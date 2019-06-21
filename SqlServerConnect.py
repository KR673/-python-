from pymssql import *
# pip install pymssql
 
# server    数据库服务器名称或IP
# user      用户名
# password  密码
# database  数据库名称
 
server = "192.168.1.5"
user = "sa"
password = "P@sswordForSA"
database = "ZhongYeLearn"
conn = connect(server, user, password, database)
cursor = conn.cursor()
cursor.execute("select * from ActivityMayEighteenth")
row=cursor.fetchone()

while row:
    print("TableId=%d, PrizeExpect=%s, Target=%s" % (row[0], row[1], row[2]))
    row = cursor.fetchone()

cursor.close()