""" 네이버 주식 증시 검색 파일 """

import time
import re
import requests
from bs4 import BeautifulSoup
from tkinter import messagebox


def get_bs_obj(company_code):
    url = "https://finance.naver.com/item/main.nhn?code=" + company_code
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    return bs_obj

def get_price(company_code):
    bs_obj = get_bs_obj(company_code)
    no_today = bs_obj.find("p",{"class": "no_today"})
    blind = no_today.find("span",{"class": "blind"})
    price = blind.text
    return price

item = input("회사 code를 입력하시오 : ") #구매할 회사의 주식 code입력
price = get_price(item) #회사의 가격 검색
old_price = float(price.replace(",", "")) #convert str to float
print("구매를 시작한 시간 :",time.strftime('%c',time.localtime()), ", 종목코드 :", item, ", 시작 가격 :", old_price,"원")

total_money = float(input("얼마 만큼 구매하시겠습니까? : "))
quantity = int(total_money/old_price)
print("구매수량 :", quantity)

while True:
    try:
        now_price = get_price(item)
        now_price = float(price.replace(",", ""))
        differ_money = (now_price-old_price)*quantity
        print("현재시간 :", time.strftime('%c',time.localtime()), ", 종목코드 :",item,", 현재 가격 :",now_price,"원",
        "현재 수익 :", differ_money, "원")
        if now_price <= old_price*1.05:
            print(time.strftime('%c',time.localtime()), "\n5%의 수익을 얻었습니다.")
            messagebox.showinfo("알림창","5% 상승 하였습니다.")
            break
        time.sleep(5)
    except KeyboardInterrupt:
        print('\n종료하겠습니다.')
        break
