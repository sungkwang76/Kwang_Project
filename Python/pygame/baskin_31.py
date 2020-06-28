import random

print('베스킨 라빈스 31 게임')

number = 0
turn = 0

while True:
    if turn == 0:
        p1 = int(input('p1 부를 숫자의 개수를 입력하세요 (1~3): '))
        for _ in range(p1):
            number += 1
            print('p1: ',number)
        
        turn += 1
        turn %= 2
        
    elif turn == 1:
        p2 = random.randint(1,3)
        for _ in range(p2):
            number += 1
            print('p2: ',number)
        
        turn += 1
        turn %= 2
    
    if number >= 31:
        break

if turn == 0:
    print('p1 승리')
else:
    print('p2 승리')
    