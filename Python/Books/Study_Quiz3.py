# Study.py
""" 한글 입력 """
# -*- coding: utf8 -*- 

""" quiz 179p ~ 181p """
""" q1 """
'''
def is_odd(number):
    if number % 2 == 1:
        return True
    else:
        return False
number = 3
print(is_odd(number))
'''
""" q2 """
'''
def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result / len(args)
print(avg_numbers(1,2))
print(avg_numbers(1,2,3,4,5))
'''
""" q3 """
'''
input1 = input("첫번째 숫자를 입력하세요 : ")
input2 = input("두번째 숫자를 입력하세요 : ")
total = int(input1) + int(input2)
print("두 수의 합은 %d 입니다" %total)
'''
""" q5 """
'''
f1 = open("Study_Quiz3.txt",'w')
f1.write("Life is too short")
f1.close()

f2 = open("Study_Quiz3.txt",'r')
print(f2.read())
f2.close()
'''
""" q6 """
'''
user_input = input("저장할 내용을 입력하세요 : ")
f = open('Study_Quiz3.txt', 'a')
f.write(user_input)
f.write("\n")
f.close()
'''
""" q7 """
'''
f = open('Study_Quiz3.txt','r')
body = f.read()
f.close()

body = body.replace('test3','Test3')

f = open('Study_Quiz3.txt','a')
f.write(body)
f.close()
'''