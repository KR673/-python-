from  apscheduler.schedulers.blocking import BlockingScheduler
import sys
import importlib
import time
import random

# 设置编码格式
importlib.reload(sys)

def request_update_status():
    print(2)

if __name__ == "__main__":
    scheduler = BlockingScheduler()
    scheduler.add_job(request_update_status, 'interval', seconds=2, max_instances=10)
    scheduler.start()



