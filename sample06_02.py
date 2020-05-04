# threading : クラス化
import threading
import time

class My_Thread(threading.Thread):
    def __init__(self, name):
        super(My_Thread, self).__init__()
        self.name = name
    
    def run(self):
        for i in range(0, 4):
            time.sleep(1)
            print('name', self.name, 'count', i)

thread1 = My_Thread('thread1')
thread2 = My_Thread('thread2')

thread1.start()
time.sleep(0.1)
thread2.start()
