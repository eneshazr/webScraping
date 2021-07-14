# instagram.com/yazilimfuryasi
# yazilimfuryasi.com
# https://yazilimfuryasi.com/beautifulsoup-web-scraping/

import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
r = requests.get(url).content
soup = BeautifulSoup(r, "html.parser") 
list = soup.find("tbody", {"class":"lister-list"}).find_all("tr",limit=250)
s = 1
for i in list:
    title = i.find("td",{"class":"titleColumn"}).find("a").text
    yil = i.find("span",{"class":"secondaryInfo"}).text.strip("()")
    rating = i.find("td",{"class":"ratingColumn"}).find("strong").text
    print(f"{s}. {title.ljust(50)} {yil}   Rating: {rating}")
    s += 1
