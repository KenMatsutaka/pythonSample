# threading : 複数スレッドの実行を行う為のライブラリ
import threading
import time

def fnc():
    for i in range(0, 4):
        time.sleep(1)
        print('count' , i)

thread1 = threading.Thread(target=fnc)
thread2 = threading.Thread(target=fnc)

thread1.start()
time.sleep(0.1)
thread2.start()