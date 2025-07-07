from datetime import datetime 
import time

def task():
    with open('timestamp_log.txt','a') as f:
        f.write(f'Script ran at : {datetime.now()}\n')
    print(f'Task ran at : {datetime.now()}')

while True:
    task()
    time.sleep(3)