import pymysql
import time
import requests
import sys
import importlib
import random
import json
import chardet
import emoji

# 设置编码格式
importlib.reload(sys)

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'referer':'https://segmentfault.com/channel/backend',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'cookie':'_ga=GA1.2.487065633.1556271755; PHPSESSID=web2~5f10ctctle4aq5k73qjmou1mrv; _gid=GA1.2.1849009673.1561617507; Hm_lvt_e23800c454aa573c0ccb16b52665ac26=1561645540,1561726742,1561777871,1561791586; Hm_lpvt_e23800c454aa573c0ccb16b52665ac26=1561792751; _gat=1'
}

def get_data(offset=int(time.time()*1000)):
    url = 'https://segmentfault.com/api/timelines/channel/1490000006201495?offset=' + str(offset) + '&_=f0c83a647ed7db68b19d5d2fedb312e0'
    response = requests.get(url=url, headers=headers)
    data = json.loads(response.text)
    return data

def input_data():
    conn = pymysql.connect(host="localhost", user="root", password="123456", database="scrapy_data", charset="utf8")
    cursor = conn.cursor()
    # 执行语句
    cursor.execute("select * from table_test")
    row=cursor.fetchone()
    cursor.close()

offset = int(time.time()*1000)
i = 1

if __name__ == "__main__":
    conn = pymysql.connect(host="localhost", user="root", password="123456", database="sys", charset="utf8")
    cursor = conn.cursor()
    while 1:
        data = get_data(offset)
        sql = 'INSERT INTO `scrapy_data`.`segment_fault`( `title`, `create_data`, `url`, `votes`) VALUES (%s, %s, %s, %s);'

        for x in data['data']:
            print(emoji.demojize(x['title']))
            sql = 'INSERT INTO `scrapy_data`.`segment_fault`( `title`, `create_data`, `url`, `votes`) VALUES ("%s", "%s", "https://segmentfault.com%s", %s);' % (emoji.demojize(x['title']), x['offset'], x['url'], x['votes'])
            cursor.execute(sql)
        offset = data['message'][0]
        
        conn.commit()
        i += 1
        if(i >= 10):
            exit()
        time.sleep(2)

    cursor.close()
