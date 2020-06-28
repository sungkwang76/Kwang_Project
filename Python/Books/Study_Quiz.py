# Study.py

""" quiz 112p ~ """
""" q1 """
'''
a = 80
b = 75
c = 55
print((a+b+c)/3)
'''
""" q2 """
'''
a = 13
if (a%2 == 0):
    print("0")
else :
    print("1")
'''
""" q3 """
'''
pin = "881120-1068234"
yyyymmdd = pin[:6] 
num = pin[7:]
print (yyyymmdd)
print (num)
'''
""" q4 """
'''
pin = "881120-1068234"
print(pin[7])
'''
""" q5 """
'''
a = "a:b:c:d"
b = a.replace(':','#')
print(b)
'''
""" q6 """
'''
a = [1,3,5,4,2]
a.sort()
a.reverse()
print(a)
'''
""" q7 """
'''
a = ['Life', 'is', 'too', 'short']
result = " ".join(a)
print(result)
'''
""" q8 """
'''
a = (1,2,3)
a = a + (4,)
print(a)
'''
""" q10 """
'''
a = {'A':90, 'B':80, 'C':70}
result = a.pop('B')
print(a)
print(result)
'''
""" q11 """
'''
a = {1,1,1,2,2,3,3,3,4,4,5}
aSet = set(a)
b = list(aSet)
print(b)
'''