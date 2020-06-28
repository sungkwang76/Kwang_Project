# Study.py
""" 한글 입력 """
# -*- coding: utf8 -*- 

""" 269p ~ 289p """
'''
def GuGu(n):
    result = []
    i = 1
    while i < 10 :
        result.append(n*i)
        i = i + 1
    return result 

print(GuGu(2))
'''
'''
result = 0
for n in range(1, 1000):
    if n % 3 == 0 or n % 5 == 0 : 
        result += n
print(result)
'''
'''
def getTotalPage(m,n):
    if m % n == 0 :
        return m//n
    else:
        return m // n + 1

print(getTotalPage(5,10))
print(getTotalPage(15,10))
print(getTotalPage(25,10))
print(getTotalPage(30,10))
'''
'''
import sys
option = sys.argv[1]
if option == '-a':
    memo = sys.argv[2]
    f = open('Study_278p.txt','a')
    f.write(memo)
    f.write('\n')
    f.close()
elif option == '-v':
    f = open('Study_278p.txt')
    memo = f.read()
    f.close()
    print(memo)
'''
'''
import sys

src = sys.argv[1]
dst = sys.argv[2]

f = open(src)
tab_content = f.read()
f.close
space_content = tab_content.replace("\t"," "*4)
f = oepn(dst, 'w')
f.write(space_content)
f.close()
'''
'''
import os
def search(dirname):
    try :
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                search(full_filename)
            else:        
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.py':
                    print(full_filename)
    except PermissionError:
        pass
search("c:/")
'''