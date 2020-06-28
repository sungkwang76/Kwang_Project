# Study.py
""" 한글 입력 """
# -*- coding: utf8 -*- 

""" 117p~129p """
""" if문 """
'''
money = True
if money:
    print("택시타라")
else :
    print("걸어가라")
'''
'''
money = 2000
card = True
if (money>3000 or card):
    print("택시타라")
else :
    print("걸어가라")
'''
'''
print (1 in [1,2,3])
print (1 not in [1,2,3])
print ('a' in ('a','b','c'))
print ('j' not in 'python')

pocket = ['paper','cellphone','money']
if 'money' in pocket :
    print ("택시타라")
else :
    print ("걸어가라")
'''
'''
pocket = ['paper','cellphone','money']
if 'card' in pocket :
    print("버스타라")
else :
    print("걸어가라")
'''
'''
pocket = ['paper','cellphone']
card = True
if 'money' in pocket:
    print("택시타라")
elif card:
    print("택시타라")
else :
    print("걸어가라")
'''
'''
score = 40
if score >=60 :
    message = "success"
    print(message)
else :
    message = "failure"
    print(message)

message ="success" if score >= 60 else "faliure"
print(message)
'''

""" 130p~137p """
""" while문 """
'''
treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1
    print("나무를 %d번 찍엇습니다." %treeHit)
    if treeHit == 10 :
        print("넘어갑니다")
'''
'''
prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number : """

number = 0
while number != 4:
    print(prompt)
    number = int(input())
    if number > 4:
        print("Error Value")
'''
'''
coffee = 10
money = 300
while money:
    print("돈 받았으니 커피 줍니다")
    coffee =  coffee - 1
    print("남은 커피의 양 : %d" %coffee)
    if coffee == 0 :
        print("커피 다팔렸음")
        break
'''
'''
coffee = 10
while True :
    money = int(input("돈을 넣어주세요 : "))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee - 1
    elif money > 300:
        print("커피를 주고 거스름돈 : %d 입니다" %(money-300))
        coffee = coffee - 1
    else :
        print("커피 안줍니다")
        print("남은커피의 양은 : %d" %coffee)
    if coffee == 0:
        print("커피 다 팔림")
        break
'''
'''
a = 0
while a < 10:
    a = a +1
    if a % 2 == 0 : continue
    print(a)
'''
'''
a = 0
while a < 10:
    a = a + 1
    if a % 3 == 0 : continue
    print(a)
'''

""" 138p ~ 145p """
""" for문 """
'''
test_list = ['one','two','three']
for i in test_list:
    print(i)
'''
'''
a = [(1,2),(3,4),(5,6)]
for (first,last) in a :
    print(first+last)
'''
'''
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
        print("%d번 학생은 합격" %number)
    else :
        print("%d번 학생은 불합격" %number)
'''
'''
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark < 60 : continue
    print("%d번 학생 합격" %number)
'''
'''
add = 0
for i in range(1, 11):
    add = add + i
print(add)
'''
'''
marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60 : continue
    print("%d번 합격 입니다" %(number+1))
'''
'''
add = 0
for a in range(101):
    add = add + a
print(add)
'''
'''
for i in range(2,10):
    for j in range(2,10):
        print(i*j, end=" ")
    print(' ')
'''
'''
a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)
print(result)
'''
'''
a = [1,2,3,4]
result = [num*3 for num in a]
print(result)
result2 = [num*3 for num in a if num%2 == 0]
print(result2)
'''
'''
result = [x*y for x in range(2,10) for y in range(2,10)]
print(result)
'''