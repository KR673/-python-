from  apscheduler.schedulers.blocking import BlockingScheduler
import sys
import importlib
import time
import random

# 设置编码格式
importlib.reload(sys)

def request_update_status():
    pam = random.randint(0, 60) * 60
    time.sleep(pam)
    file = open('E:\\scheduleTest.txt', 'a')
    file.writelines(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ' 执行成功\n')
    file.close

if __name__ == "__main__":
    scheduler = BlockingScheduler()
    scheduler.add_job(request_update_status, 'interval', seconds=2, max_instances=10)
    scheduler.start()



