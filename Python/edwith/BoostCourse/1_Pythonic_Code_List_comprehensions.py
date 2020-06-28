result = []
for i in range(10):
    result.append(i)
print(result)

result = [i for i in range(10)]
print(result)
result = [i for i in range(10) if i%2 == 0]
print(result)

word_1 = "Hello"
word_2 = "World"
result = [i+j for i in word_1 for j in word_2]
print(result)

case_1 = ["A","B","C"]
case_2 = ["D","E","A"]
result = [i+j for i in case_1 for j in case_2]
print(result)
result = [i+j for i in case_1 for j in case_2 if not(i==j)]
print(result)
result.sort()
print(result)

words = 'The quick brown fox jumps over the lazy dog'.split()
print(words)
"""two dimensional list"""
stuff = [[w.upper(),w.lower(),len(w)] for w in words]
for i in stuff:
    print(i)

case_1 = ["A","B","C"]
case_2 = ["D","E","F"]
result = [a+b for a in case_1 for b in case_2]
print(result)

result = [[a+b for a in case_1] for b in case_2]
print(result)