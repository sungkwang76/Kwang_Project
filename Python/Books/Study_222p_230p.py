# Study.py
""" 한글 입력 """
# -*- coding: utf8 -*- 

""" 222p ~ 230p """
""" 예외처리 """
'''
try:
    4/0
except ZeroDivisionError as e:
    print(e)
'''
'''
try:
    a = [1,2,3]
    print(a[4])
except IndexError as e:
    print(e)
'''
'''
f = open('Study_225p.txt','w')
try:
    a = [1,2,3]
    print(a[4])
finally:
    f.close()
'''
"""
try:
    a = [1,2]
    print(a[3])
    4/0
'''
except (ZeroDivisionError, IndexError) as e:
    print(e)
'''
'''
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다")
except IndexError:
    print("인덱싱할 수 없습니다")
'''
"""
'''
try:
    f = open('not file','r')
except FileNotFoundError:
    pass
'''
'''
class Myerror(Exception):
    pass

def say_nick(nick):
    if nick == '바보':
        raise Myerror()
    print(nick)

try:
    print(say_nick("천사"))
    print(say_nick("바보"))
except MyError():
    print("허용되지 않는 별명입니다.")
'''


