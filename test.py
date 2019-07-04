import sys
import importlib
import pymysql

# 设置编码格式
importlib.reload(sys)

# 安装pymsql  pip install pymsql
# server    数据库服务器名称或IP
# user      用户名
# password  密码
# database  数据库名称
conn = pymysql.connect(host="localhost", user="root", password="123456", database="sys", charset="utf8")
cursor = conn.cursor()
# 执行语句
cursor.execute("select * from table_test")
row=cursor.fetchone()
target = open("F:\\datas\\person.csv", 'a+', encoding='utf-8')
while row:
    data =  '{},{},{}'.format(row[0], row[1], row[2]).encode('gbk')
    print(data)
    target.writelines(str(data)+'\n')
    row = cursor.fetchone()
target.close()
cursor.close()