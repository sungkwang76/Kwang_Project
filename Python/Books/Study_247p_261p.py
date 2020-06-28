# Study.py
""" 한글 입력 """
# -*- coding: utf8 -*- 

""" 247p ~ 261p """
""" 외장함수 """
'''
import sys
print(sys.argv)
'''
'''
import pickle
f1 = open("Study_249p.txt",'wb')
data = {1: 'python', 2 : 'you need'}
pickle.dump(data,f1)
f1.close()
f2 = open("Study_249p.txt",'rb')
data = pickle.load(f2)
print(data)
'''
'''
import os
print(os.environ)
print(os.environ['PATH'])
print(os.getcwd())
'''
'''
import shutil
shutil.copy("Study_249p.txt","Study_251p.txt")
'''
'''
import glob
print(glob.glob("/User/sungkwangkim/Developer/Python/Kwang-s-Study"))
'''
'''
import tempfile
filename = tempfile.mktemp()
print(filename)
f = tempfile.TemporaryFile()
f.close() 
'''
'''
import time
print(time.time())
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))
print(time.ctime())
print(time.strftime('%x',time.localtime(time.time())))
print(time.strftime('%c',time.localtime(time.time())))

for i in range(10):
    print(i)
    time.sleep(1)
'''
'''
import calendar
print(calendar.calendar(2015))
print(calendar.prcal(2015))
print(calendar.prmonth(2015, 12))
print(calendar.weekday(2015, 12, 31))
print(calendar.monthrange(2015,12))
'''

import random
'''
print(random.random())
print(random.randint(1,10))
'''
'''
def random_pop(data):
    number = random.randint(0, len(data)-1)
    return data.pop(number)

if __name__ == "__main__":
    data = [1,2,3,4,5]
    while data : print(random_pop(data))
'''
'''
def random_pop(data):
    number = random.choice(data)
    data.remove(number)
    return number
if __name__ == "__main__":
    data = [1,2,3,4,5]
    while data : print(random_pop(data))
'''
'''
data = [1,2,3,4,5]
random.shuffle(data)
print(data)
'''
'''
import webbrowser
webbrowser.open("http://google.co.kr")
webbrowser.open_new("http://google.co.kr")
'''
'''
import time
def long_task():
    for i in range(5):
        time.sleep(1)
        print("working:%s \n" %i)
print("Start")
for i in range(5):
    long_task()
print("End")
'''
'''
import time
import threading

def long_task():
    for i in range(5):
        time.sleep(1)
        print("working:%s \n" %i)
print("Start")

threads = []
for i in range(5):
    t = threading.Thread(target=long_task)
    threads.append(t)

for t in threads:
    t.start()
print("End")
'''
'''
import time
import threading

def long_task():
    for i in range(5):
        time.sleep(1)
        print("working:%s \n" %i)
print("Start")

threads = []
for i in range(5):
    t = threading.Thread(target=long_task)
    threads.append(t)

for t in threads:
    t.start()
for t in threads:
    t.join()
print("End")
'''