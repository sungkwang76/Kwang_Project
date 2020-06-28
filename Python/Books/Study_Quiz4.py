# Study.py
""" 한글 입력 """
# -*- coding: utf8 -*- 

""" quiz 262p ~ 265p """
''' q1 '''
'''
class Calculator:
    def __init__(self):
        self.value = 0
    
    def add(self, val):
        self.value += val

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)
print(cal.value)
'''
''' q2 '''
'''
class Calculator:
    def __init__(self):
        self.value = 0
    def add(self, val):
        self.value += val

class MaxLimitCalculator(Calculator):
    def add(self,val):
        self.value += val
        if self.value >= 100:
            self.value = 100

cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)
print(cal.value)
'''
''' q4 '''
'''
print(list(filter(lambda x: x>0, [1,-2,3,-5,8,-3])))
'''
''' q5 '''
'''
print(int('0xea',16))
'''
''' q6 '''
'''
print(list(map(lambda x: x*3,[1,2,3,4])))
'''
''' q7 '''
'''
a = [-8,2,7,5,-3,5,0,1]
print(max(a))
print(min(a))
'''
''' q8 '''
'''
print(round(17/3 , 4))
'''
''' q9 '''
''''
import sys
numbers = sys.argv[1:]
result = 0
for number in numbers:
    result += int(number)
print(result)
'''
''' q10 '''
'''
import os
os.chdir("c:/doit")
result = os.popen("dir")
print(result.read())
'''
''' q11 '''
'''
import glob
glob.glob("c:/doit/*.py")
'''
''' q12 '''
'''
import time
print(time.strftime("%Y/%m/%d %H:%M:%S"))
'''
''' q13 '''
'''
import random
result = []
while len(result)<6:
    num = random.randint(1,45)
    if num not in result:
        result.append(num)
print(result)
'''