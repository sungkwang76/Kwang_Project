# Study.py
""" 한글 입력 """
# -*- coding: utf8 -*- 

""" 291p ~  320p """
""" 정규식 """
'''
import re

data = """
park 800905 - 1049118
kim 700905 - 1059119
"""
pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******",data))
'''
"""
import re
p = re.compile('[a-z]+')
'''
m = p.match("python")
print(m)
m1 = p.match("3 python")
print(m1)
'''
'''
m = p.search("python")
print(m)
m1 = p.search("3 python")
print(m1)
'''
'''
result = p.findall("life is too short")
print(result)
'''
'''
result = p.finditer("life is too short")
print(result)
for i in result : print(i)
'''
'''
m = p.match("python")
print(m.group())
print(m.start())
print(m.end())
print(m.span())
'''
'''
m = p.search("3 python")
print(m.group())
print(m.start())
print(m.end())
print(m.span())
'''
"""

import re
'''
p = re.compile('a.b')
m = p.match('a\nb')
print(m)
'''
'''
p = re.compile('a.b', re.DOTALL)
m = p.match('a\nb')
print(m)
'''
'''
p = re.compile('[a-z]',re.I)
print(p.match('python'))
print(p.match('Python'))
print(p.match('PYTHON'))
'''
'''
p = re.compile("^python\s\w+",re.M)

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data))
'''
'''
charref = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);)

charref = re.compile(r"""
    &[#]
    (
        0[0-7]+
        | [0-9]+
        | x[0-9a-fA-F]+
    )
    ;
""", re.VERBOSE)
'''
'''
p = re.compile('Crow|Servo')
m = p.match('CrowHello') 
print(m)
'''
'''
print(re.search('^Life','Life is too short'))
print(re.search('^Life','My Life'))
'''
'''
print(re.search('short$','Life is too short'))
print(re.search('short$','Life is too short, you need python'))
'''
'''
p = re.compile(r'\bclass\b')
print(p.search('no class at all'))
print(p.search('the declassified algorithm'))
'''
'''
p = re.compile(r'\Bclass\B')
print(p.search('no class at all'))
print(p.search('the declassified algorithm'))
print(p.search('one subclass is'))
'''
'''
p = re.compile('(ABC)+')
m = p.search('ABCABCABC OK?')
print(m)
print(m.group(0))
'''
'''
p = re.compile(r"\w+\s+\d+[-]\d+[-]\d+")
m = p.search("park 010-1234-1234")
print(m)

p1= re.compile(r"(\w+)\s+\d+[-]\d+[-]\d+")
m1 = p1.search("park 010-1234-1234")
print(m1.group(1))

p2= re.compile(r"(\w+)\s+(\d+[-]\d+[-]\d+)")
m2 = p2.search("park 010-1234-1234")
print(m2.group(2))

p3= re.compile(r"(\w+)\s+((\d+)[-]\d+[-]\d+)")
m3 = p3.search("park 010-1234-1234")
print(m3.group(3))
'''
'''
p = re.compile(r"(?P<name>\w+)\s+(\d+[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group("name"))

p1 = re.compile(r'(?P<word>\b\w+)\s+(?P=word)')
print(p1.search('Paris in the the spring').group())
'''
'''
p = re.compile(".+:")
m = p.search("http://google.com")
print(m.group())

p1 = re.compile(".+(?=:)")
m1 = p1.search("http://google.com")
print(m1.group())
'''
'''
p = re.compile('(blue|white|red)')
print(p.sub('colour','blue socks and red shoes'))
print(p.sub('colour','blue socks and red shoes',count = 1))
'''
'''
p = re.compile((r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)"))
print(p.sub("\g<phone> \g<name>","park 010-1234-1234"))
'''
'''
def hexrepl(match):
    "Return the hex string for a decimal number"
    value = int(match.group())
    return hex(value)
p = re.compile(r'\d+')
print(p.sub(hexrepl, 'Call 65490 for printing, 49152 for user code.'))
'''
'''
s = '<html><head><title>Title</title>'
print(len(s))
print(re.match('<.*>',s).span())
print(re.match('<.*>',s).group())
print(re.match('<.*?>',s).group())
'''