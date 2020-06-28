for i, v in enumerate(['tic','tac','toe']):
    print(i,v)

mylist = ["a","b","c","d"]
print(list(enumerate(mylist)))

result = {i:j for i,j in enumerate('Gachon University is an academic institue located in South Korea'.split())}
print(result)

alist = ['a1','a2','a3']
blist = ['b1','b2','b3']
for a,b in zip(alist,blist):
    print (a,b)

a,b,c = zip((1,2,3),(10,20,30),(100,200,300))
print(a,b,c)
result = [sum(x) for x in zip((1,2,3),(10,20,30),(100,200,300))]
print(result)

alist = ['a1','a2','a3']
blist = ['b1','b2','b3']

for i, (a,b) in enumerate(zip(alist,blist)):
    print( i,a,b)