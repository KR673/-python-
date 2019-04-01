#-*- coding:utf-8 –*-
#
#众生平等，2019升职加薪
#
#windows写入数据到文件需要
import sys
import importlib

importlib.reload(sys)
# 导入faker包生成数据
# 想要生成的数据字段到官方文档找
# https://faker.readthedocs.io/en/master/locales/zh_CN.html#faker-providers-company
from faker import Faker
# 设置中国地区偏好数据
fake = Faker(locale='zh-CN')
target = open("F:\\datas\\person.csv", 'a')

# 随机生成一千条数据写入到csv
for i in range(10000):
    print(i)
    # 姓名，身份证，手机号码，工作岗位，电子邮箱，信用卡，公司名称
    if i == 0:
        data = "table_id" + ',' + "ssn" + ',' + 'mobile' + ',' + 'job' + ',' + 'email' + ',' + 'id_number' +  ',' + 'birthday' + ',' + 'company' + ',' + 'url'
        target.writelines(str(data)+'\n')
    data = str(i + 1) + ',' + fake.name() + ',' +fake.ssn() +  ','+fake.phone_number()+ ','+fake.job()+ ','+fake.email()+','+fake.credit_card_number(card_type=None)+','+fake.company() + ',' + fake.date() + ',' + fake.url()
    target.writelines(str(data)+'\n')
target.close()
#print(fake.name() + ',' +fake.ssn() +  ','+fake.phone_number()+ ','+fake.job()+ ','+fake.email()+','+fake.credit_card_number(card_type=None)+','+fake.company()+'\n')

#print(fake.name() + ',' +fake.ssn() +  ','+fake.phone_number()+ ','+fake.job()+ ','+fake.email()+','+fake.credit_card_number(card_type=None)+','+fake.company()+'\n')