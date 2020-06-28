from collections import deque
from collections import Counter
from collections import OrderedDict
from collections import defaultdict
from collections import namedtuple
import time

deque_list = deque()
for i in range(5):
    deque_list.append(i)
print(deque_list)

deque_list.appendleft(10)
print(deque_list)

deque_list.rotate(2)
print(deque_list)
deque_list.rotate(2)
print(deque_list)

deque_list.extend([5,6,7])
print(deque_list)
deque_list.extendleft([5,6,7])
print(deque_list)

print(deque_list)
print(deque(reversed(deque_list)))

start_time = time.perf_counter()
deque_list_1 = deque()
for i in range(10):
    for i in range(10):
        deque_list_1.append(i)
        deque_list_1.pop()
print(time.perf_counter()-start_time, "seconds")

d = OrderedDict()
d['x'] = 100
d['y'] = 200
d['z'] = 300
d['l'] = 500

for k,v in d.items():
    print (k,v)
 
e = defaultdict(object)
e = defaultdict(lambda:0)
print(e["first"])

text = """I'm studying Python.I'm not very good right now, but I will study and do well."""
word_count = {}
for word in text:
    if word in word_count.keys():
        word_count[word] += 1
    else:
        word_count[word] = 0
print(word_count)


word_count = defaultdict(object)
word_count = defaultdict(lambda: 0)
for word in text:
    word_count[word] += 1
for i, v in OrderedDict(sorted(word_count.items(),key=lambda t: t[1],reverse=True)).items():
    print(i,v)

c = Counter()
c = Counter('gallahad')
print(c)