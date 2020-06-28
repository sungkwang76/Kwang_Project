# Study.py
""" 한글 입력 """
# -*- coding: utf8 -*- 

""" q2 """
'''
result = 0
i = 1
while i <= 1000:
    if i % 3 == 0:
        result += i
    i += 1
print(result)
'''
""" q3 """
'''
i = 0
while True:
    i += 1
    if i > 5 : break
    print('*'*i)
'''
""" q4 """
'''
for i in range(101):
    print(i)
'''
""" q5 """
'''
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for score in A:
    total += score
average = total / len(A)
print(average)
'''
""" q6 """
"""
numbers = [1,2,3,4,5]
'''
result = []
for n in numbers:
    if n %2 == 1:
        result.append(n*2)
print(result)
'''
'''
result = [n*2 for n in numbers if n % 2 == 1]        
print(result)
'''
"""