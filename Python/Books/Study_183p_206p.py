# Study.py
""" 한글 입력 """
# -*- coding: utf8 -*- 

""" 183p ~ 206p"""
""" 클래스 """
"""
'''
result1 = 0
result2 = 0
def add1(num):
    global result1
    result1 += num
    return result1
def add2(num):
    global result2
    result2 += num
    return result2

print(add1(3))
print(add2(3))
print(add1(4))
print(add2(7))
'''
'''
class Calculator:
    def __init__(self):
        self.result = 0
    def add(self, num):
        self.result += num
        return self.result
    def sub(self, num):
        self.result -= num
        return self.result
cal1 = Calculator()
cal2 = Calculator()
cal3 = Calculator()

print(cal1.add(3))
print(cal2.add(3))
print(cal3.sub(7))
print(cal1.add(3))
print(cal2.add(7))
print(cal3.sub(3))
'''

class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
'''
a = FourCal()
b = FourCal()
a.setdata(4,2)
b.setdata(7,3)
print(a.first)
print(b.first)
'''
'''
a = FourCal()
a.setdata(4,2)
print(a.add())
'''
'''
a = FourCal()
b = FourCal()
a.setdata(4,2)
b.setdata(3,8)
print(a.add())
print(b.add())
print(a.mul())
print(b.mul())
print(a.sub())
print(b.sub())
print(a.div())
print(b.div())
'''
'''
a = FourCal(4,2)
print(a.add())
print(a.mul())
'''

class MoreForuCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result
'''
a = MoreForuCal(4,2)
print(a.pow())
'''

class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second
'''
a = SafeFourCal(4,0)
print(a.div())
'''
class FailFourCal(FourCal):
    def mul(self):
        if self.second == 0:
            return 0
        else:
            return self.first * self.second
'''
a = FailFourCal(4,0)
print(a.mul())
'''
"""