#coding=utf-8
import os
import threading
import time
def openDb(bat):
    os.system(bat)

def open_mongo():
    path = u"脚本"
    bat_name = "\mogodb.bat"
    db_thread = threading.Thread(target=openDb, args=(path+bat_name,))
    db_thread.start()
    #等待5秒直到mongodb完全打开
    time.sleep(5)
    print u"mongoDB已经打开"
