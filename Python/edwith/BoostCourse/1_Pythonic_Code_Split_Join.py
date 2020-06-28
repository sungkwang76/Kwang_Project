"""Split 함수"""
items = 'zero one two three'.split()
print(items)
example = 'python,jquery,javascript'
print(example.split(","))
a,b,c = example.split(",")
print(a,b,c)
example = 'cs50.gachos.edu'
subdomain,domain,tld = example.split('.')
print(subdomain,domain,tld)


"""Join 함수"""
colors = ['red', 'blue', 'green','yellow']
result = ' '.join(colors)
print(result)
result = ', '.join(colors)
print(result)
result = '-'.join(colors)
print(result)



