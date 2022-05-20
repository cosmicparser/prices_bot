import requests
from bs4 import BeautifulSoup

responseside = requests.get('https://docs.google.com/document/d/16qfSiIaN1okmuWxTHp-fM-2fkZ9YY-AfFlH9hS-jewM/edit')
soup = BeautifulSoup(responseside.content, 'html.parser')
ids = []
likes = []

for a in soup.find_all("a"):
    div = a.find("div")
    ids.append(div)

res = list(filter(None, ids))

for i in res:
    print(res[res.index(i)].get_text())


for g in soup.find_all("a"):
    span = g.find("span")
    likes.append(span)


reslks = list(filter(None, likes))

for i in reslks:
 print(reslks[reslks.index(i)].get_text())





'''
c = soup.find("div", id="lenta-card__text-quote-42725732-wrapper-8450093")
b = c.find_all("p")
s=str(b)
print("цитата 1: ", s[4:len(s)-5])

like=soup.find("span", id="vote-plus-span-quote-42725732")
print("лайков: ", like.get_text())
saves = soup.find("a", id = "a-fav-quote-42725732")
savesb = saves.find_all("span")
print("сохранений: ", savesb[0].get_text())



response = requests.get('https://www.livelib.ru/author/1162444/quotes-dzhordan-bernt-piterson')
soup = BeautifulSoup(response.content, 'html.parser')

c = soup.find("div", id="lenta-card__text-quote-42669454-wrapper-685537")
b = c.find_all("p")
s=str(b)
print("цитата 2: ", s[4:len(s)-5])

like=soup.find("a", id="vote-plus-hand-quote-42669454")
print("лайков:", like.get_text())

saves = soup.find("span", id = "fav-quote-42669454")
savesb = saves.find_all("span")
print("сохранений: ", savesb[0].get_text())


c = soup.find("div", id="lenta-card__text-quote-42714317-wrapper-8281878")
b = c.find_all("p")
s=str(b)
print("цитата 3: ", s[4:len(s)-5])

like=soup.find("a", id="vote-plus-hand-quote-42714317")
print("лайков:", like.get_text())

saves = soup.find("a", id = "a-fav-quote-42714317")
savesb = saves.find_all("span")
print("сохранений: ", savesb[0].get_text())



c = soup.find("div", id="lenta-card__text-quote-42714838-wrapper-1394329")
b = c.find_all("p")
s=str(b)
print("цитата 4: ", s[4:len(s)-5])

like=soup.find("a", id="vote-plus-hand-quote-42714838")
print("лайков:", like.get_text())

saves = soup.find("a", id = "a-fav-quote-42714838")
savesb = saves.find_all("span")
print("сохранений: ", savesb[0].get_text())

'''
