# Study.py
""" 한글 입력 """
# -*- coding: utf8 -*- 

""" 231p ~ 246p"""
""" 내장함수 """
'''
print(abs(-3))
print(abs(-1.2))
'''
'''
print(all([1,2,3]))
print(all([1,2,3,0]))
'''
'''
print(any([1,2,3,0]))
print(any([0,""]))
'''
'''
print(chr(97))
print(chr(45))
'''
'''
print(dir([1,2,3]))
print(dir({'1':'a'}))
'''
'''
print(divmod(7,3))
'''
'''
for i, name in enumerate(['body','foo','bar']):
    print(i,name)
'''
'''
print(eval('1+2'))
print(eval("'hi'+'a'"))
print(eval('divmod(4,3)'))
'''
'''
def positive(l):
    result = []
    for i in l:
        if i > 0:
            result.append(i)
    return result
print(positive([1,-3,2,0,-5,-6]))

def positive1(x):
    return x > 0
print(list(filter(positive1, [1,-3,2,0,-5,-6])))
print(list(filter(lambda x: x>0,[1,-3,2,0,-5,6])))
'''
'''
print(hex(234))
print(hex(3))
'''
'''
a = 3
print(id(3))
print(id(a))
b = a
print(id(b))
'''
'''
a = input("Enter : ")
print (a)
'''
'''
print(int('3'))
print(int(3.4))
print(int('11',2))
print(int('1A',16))
'''
'''
class person: pass
a = person()
print(isinstance(a, person))
b = 3
print(isinstance(b, person))
'''
'''
print(len("python"))
print(len([1,2,3,4]))
print(len((1,'a')))
'''
'''
print(list("python"))
print(list((1,2,3)))
a = [1,2,3]
b = list(a)
print(b)
'''
'''
def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number*2)
    return result

result = two_times([1,2,3,4])
print(result)

def two_times1(x): return x*2
print(list(map(two_times1, [1,2,3,4])))
print(list(map(lambda a: a*2,[1,2,3,4])))
'''
'''
print(max([1,2,3]))
print(max('python'))
print(min([1,2,3]))
print(min('python'))
'''
'''
print(oct(34))
print(oct(12345))
'''
'''
print(ord('a'))
print(ord('-')) 
'''
'''
print(pow(2,4))
print(pow(3,3))
'''
'''
print(list(range(5)))
print(list(range(5,10)))
print(list(range(1,10,2)))
print(list(range(0,-10,-1)))
'''
'''
print(round(4.5))
print(round(4.2))
print(round(5.678,2))
'''
'''
print(sorted([1,3,2]))
print(sorted(['a','c','b']))
print(sorted("zero"))
print(sorted((3,2,1)))
'''
'''
print(str(3))
print(str('hi'))
print(str('hi'.upper()))
'''
'''
print(sum([1,2,3]))
print(sum((4,5,6)))
'''
'''
print(tuple("abc"))
print(tuple([1,2,3]))
print(tuple((1,2,3)))
'''
'''
print(type("abc"))
print(type([]))
print(type(open('test','w')))
'''
'''
print(list(zip([1,2,3],[4,5,6])))
print(list(zip([1,2,3],[4,5,6],[7,8,9])))
print(list(zip("abc","def")))
'''