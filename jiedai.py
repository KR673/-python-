import sys
import importlib
from faker import Faker
import random
import pymysql

importlib.reload(sys)

fake = Faker(locale='zh-CN')

conn = pymysql.connect(host="localhost", user="root", password="123456", database="scrapy_data", charset="utf8")
cursor = conn.cursor()
for x in range(0, 500):
    for i in range(0, 1000):
        print(str(x) + '-' + str(i))
        sql = 'insert into fx_jiedailiebiao (invite_id,jiHui_id,customer_name,sex,exam_id,mendian_id,appointment_time_start,appointment_time_end,appointment_remark \
        ,appointment_user_group_id,reception_user_group_id,reception_status,reception_info,mobile,tuiGuangxinxilog_id) values ({},{},"{}",{},"{}","{}","{}","{}","{}",{},{},{},"{}","{}",{})' \
        .format(fake.numerify(), fake.numerify(), str(fake.name()), int(random.uniform(0,1)), ','.join([str(x) + '' for x in range(1, int(random.uniform(2, 15)))]),fake.numerify(),fake.past_datetime(), fake.future_datetime(),\
        fake.sentences(),fake.numerify(), fake.numerify(), int(random.uniform(0, 2)), fake.sentences(), fake.phone_number(), fake.numerify())
        cursor.execute(sql)
    conn.commit()

cursor.close()