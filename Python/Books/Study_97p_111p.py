# Study.py

""" 97p ~ 101p"""
"""Set data type"""
"""
s1 = set([1,2,3])
print(s1)
"""
"""
s2 = set("Hello")
print(s2)
"""
"""
s1 = set([1,2,3])
l1 = list(s1)
print(l1)
t1 = tuple(s1)
print(t1)
print(t1[0])
"""
"""
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
print(s1&s2)
print(s1.intersection(s2))
print(s1|s2)
print(s1.union(s2))
print(s1-s2)
print(s1.difference(s2))
print(s2.difference(s1))

s1.add(7)
print(s1)
s1.update([7,8,9])
print(s1)
s1.remove(1)
print(s1)
"""

""" 102p ~ 106p """
"""bool data type"""
"""
a = True
b = False
print(type(a))
print(type(b))
print(1 == 1)
print(2 > 1)
print(2 < 1)
"""
"""
a = [1,2,3,4]
while a :
    print(a.pop())

if [1,2,3]:
    print ("참")
else :
    print ("거짓")

print (bool([1,2,3]))
print (bool([]))
print (bool(0))
print (bool(3))
"""

""" 107p ~ 111p"""
""" Variable of type """
"""
a = [1,2,3]
b=a
print(id(a))
print(id(b))
a[1] = 4
print(a)
print(b)
"""
"""
a = [1,2,3]
'''
b = a[:]
a[1] = 4
print(a)
print(b)
'''
from copy import copy
b = copy(a)
print(a)
print(b)
print ( b is a ) 
"""
"""
a,b = ('python','life')
(a,b) = 'python', 'life'
[a,b] = ['python', 'life']
a = b = 'python'
"""
"""
a = 3
b = 5
a, b = b, a
print(a)
print(b)
"""