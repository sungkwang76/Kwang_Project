def asterisk_test_1(a, *args):
    print(a,args)
    print(type(args))

asterisk_test_1(1,2,3,4,5,6)

def asterisk_test_2(a, **kargs):
    print(a,kargs)
    print(type(kargs))

def asterisk_test_3(a, *args):
    print(a,args[0])
    print(type(args))

def asterisk_test_4(a, args):
    print(a,*args)
    print(type(args))

asterisk_test_2(1, b=2, c=3, d=4, e=5, f=6)

asterisk_test_3(1,(2,3,4,5,6))

asterisk_test_4(1,(2,3,4,5,6))

a,b,c = ([1,2],[3,4],[5,6])
print(a,b,c)

data = ([1,2],[3,4],[5,6])
print(*data)

def  asterisk_test_5(a,b,c,d):
    print(a,b,c,d)

data = {"b":1, "c":2, "d":3}
asterisk_test_5(10, **data)

for data in zip(*([1,2],[3,4],[5,6])):
    print(sum(data))

