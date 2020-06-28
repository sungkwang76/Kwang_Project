""" 네이버 주식 증시 검색 파일 """

import time
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/item/main.nhn?code=263750"
result = requests.get(url)
bs_obj = BeautifulSoup(result.content, "html.parser")
no_today = bs_obj.find("p",{"class": "no_today"})
blind = no_today.find("span",{"class": "blind"})
now_price = blind.text

print(time.strftime('%c',time.localtime()), now_price)

