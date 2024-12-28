from bs4 import BeautifulSoup
import lxml
# with open("website.html",encoding="utf8") as file:
#     content = file.read()
#
# soup=BeautifulSoup(content,'lxml')
# print(soup)
#
# find_all=soup.findAll(name="a")
# print(find_all)
#
# for tag in find_all:
#     print(tag.getText())
#     print(tag.get("href"))
#
# heading=soup.find(name="h1",id="name")
# print(heading)
#
# heading2=soup.find(name="h3",class_="heading")
# print(heading2)
#
# id=soup.select_one(selector="#name")
# print(id)

###########################################################
import requests

response =requests.get("https://news.ycombinator.com/news")
yc_web_page=response.text
print(yc_web_page)
yc_soup=BeautifulSoup(yc_web_page,"html.parser")
print("##########################################")
news=(yc_soup.find_all(name='span',class_='titleline'))
print(news)
article_text=[]
artile_link=[]
for title in news:
    text=title.getText()
    article_text.append(text)
    link=title.get("href")
    artile_link.append(link)
artile_upvote=[int(score.getText().split(" ")[0]) for score in yc_soup.find_all(name='span',class_="score")]
print(article_text)
print(artile_link)
print(artile_upvote)

max_item=max(artile_upvote)
index=artile_upvote.index(max_item)
print(article_text[index])
print(artile_link[index])
