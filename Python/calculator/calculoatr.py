# Hex or Dec Calculator

def plus (a,b):
    return a+b

def minus (a,b):
    return a-b

def mul (a,b):
    return a*b

def div (a,b):
    return a/b

print("D : Decimal , H : Hex")
print("1.더하기, 2.빼기, 3.곱하기, 4.나누기, 5.나가기")

while True:
    dec_hex = input("원하는 변수를 입력하시오 : ")
    menu = int(input("원하는 기능을 입력하시오 : "))
    if dec_hex == 'D':
        if (menu < 5):
            numberA = int(input("첫번째 숫자를 입력하시오 : "))
            numberB = int(input("두번째 숫자를 입력하시오 : "))
            if(menu == 1):
                result = plus(numberA,numberB)
                print("결과 :", result)
            elif(menu == 2):
                result = minus(numberA,numberB)
                print("결과 :", result)
            elif(menu == 3):
                result = mul(numberA,numberB)
                print("결과 :", result)
            elif(menu == 4):
                result = div(numberA,numberB)
                print("결과 :", result)
        elif(menu == 5):
            print("나가기")
            break
        else:
            print("menu를 잘못 입력하셨습니다.")
    elif dec_hex == 'H':
        if (menu < 5):
            numberA = hex(int(input("첫번째 숫자를 입력하시오 : ")))
            numberB = hex(int(input("두번째 숫자를 입력하시오 : ")))
            if(menu == 1):
                result = plus(numberA,numberB)
                print("결과 :", result)
            elif(menu == 2):
                result = minus(numberA,numberB)
                print("결과 :", result)
            elif(menu == 3):
                result = mul(numberA,numberB)
                print("결과 :", result)
            elif(menu == 4):
                result = div(numberA,numberB)
                print("결과 :", result)
        elif(menu == 5):
            print("나가기")
            break
        else:
            print("menu를 잘못 입력하셨습니다.")