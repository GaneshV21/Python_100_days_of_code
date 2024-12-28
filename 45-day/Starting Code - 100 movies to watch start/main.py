import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response=requests.get(URL)

soup=BeautifulSoup(response.text,'html.parser')
title=soup.find_all(name="h3",class_="title")
new_Arr=[item.getText() for item in title]
new_Arr=new_Arr[::-1]
print(new_Arr)

with open('main.txt',mode='w',encoding="utf8") as new_file:
    for item in new_Arr:
        new_file.write(f"{item}\n")