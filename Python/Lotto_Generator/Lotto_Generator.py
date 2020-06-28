#Lotto number Generator

import random

file = open('lotto_number.txt','wt')

print('-----------------------------\n')
print('***로또 번호 자동 생성기***\n')
print('-----------------------------\n')

count = 0
cm = "Y"

while True:
    amount = input("몇 개를 구매하시겠습니까? ")
    count+=1
    print(count,'회차')
    file.write(str(count))
    file.write('회차')
    file.write('\n')
    for i in range(0,int(amount)): 
        Lotto_number = random.sample(range(1,45),6)
        print(i+1,"번 :",sorted(Lotto_number))
        file.write(str(sorted(Lotto_number)))
        file.write('\n')
    cm = input("추가로 더 구매 하시겠습니까? Y/N : ")
    if(cm == "N"):
        print('번호 생성을 중지합니다.')
        break