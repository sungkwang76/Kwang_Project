# Study.py
""" 한글 입력 """
# -*- coding: utf8 -*- 


""" 150p ~ 167p"""
""" 함수 """
'''
def add (a,b):
    return a+b
a = 3
b = 4
c = add(a,b)
print(c)
print(add(3,4))
'''
'''
def add(a,b):
    result = a+b
    return result
a = add(3,4)
print(a)
'''
'''
def add(a,b):
    print("%d, %d의 합은 %d 입니다" % (a,b,a+b))
add(3,4)
a = add(3,4)
print(a)
'''
'''
def add(a,b):
    return a+b
result = add(a=3,b=7)
print(result)
'''
'''
def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result
result = add_many(3,4,5)
print(result)
result = add_many(353,32,23,12,2)
print(result)
'''
''' *args = 튜플형
def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result*i
    return result
result = add_mul('add',1,2,3,4,5)
print (result)
result = add_mul('mul',1,2,3,4,5)
print (result)
'''
''' **kwargs = 딕셔너리
def print_kwargs(**kwargs):
    print(kwargs)
print_kwargs(a=1)
print_kwargs(name='foo',age=3)
'''
'''
def add_and_mul(a,b):
    return a+b, a*b
result = add_and_mul(3,4)
print(result)
result1, result2 = add_and_mul(3,4)
print(result1)
print(result2)
'''
'''
def say_myself(name,old,man=True):
    print("name is %s" % name)
    print("old is %d" % old)
    if man:
        print("Man")
    else:
        print("Woman")

say_myself("kwang",27,True)
say_myself("sung",29,False)
'''
'''
a = 1
def vartest(a):
    a = a + 1
    return a
a = vartest(a)
print(a)
'''
'''
add = lambda a, b : a+b
result = add(3,4)
print(result)
'''
""" 168P ~ 170P """
""" 입출력 """
'''
a = input("input your number : ")
print(a)
'''
'''
print("Life" "is" "too Short")
print("Life"+"is"+"too Short")
print("Life","is","too Short")
'''
'''
for i in range(10):
    print(i, end = ' ')
''' 
""" 171P ~ 178P """
""" 파일 읽고 쓰기 """
'''
f = open("Study_172P.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" %i
    f.write(data)
f.close
'''
'''
f = open("Study_172P.txt", 'r')
line = f.readline()
print(line)
f.close()
'''
'''
f = open("Study_172P.txt",'r')
while True:
    line = f.readline()
    if not line : break
    print(line)
f.close()
'''
'''
f = open("Study_172P.txt",'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()
'''
'''
f = open("Study_172P.txt",'r')
data = f.read()
print(data)
f.close()
'''
'''
f = open("Study_172P.txt",'a')
for i in range(11,20):
    data = "%d 번째 줄입니다.\n" %i
    f.write(data)
f.close()
'''
'''
with open("Study_172P.txt",'a') as f:
    f.write("Life is too short, you need python")
'''
