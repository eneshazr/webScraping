import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.kitapyurdu.com/index.php?route=product/best_sellers&list_id=1&filter_in_stock=1&filter_in_stock=1&limit=25"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}
r = requests.get(url, headers=headers).content
soup = BeautifulSoup(r, "html.parser")

fiyat = []
yazar = []
yayın = []
s = 1
s2 = 0

pricenew = soup.find_all("div", {"class":"price-new"})

author = soup.find_all("div", {"class":"author compact ellipsis"})
publisher = soup.find_all("div", {"class":"publisher"})
list = soup.find_all("div", {"class":"name ellipsis"})

file = open("Desktop/kitap.csv","w", newline= "", encoding='utf-8')
writer = csv.writer(file)
writer.writerow(["ID","Kitap Adı", "Yazar", "Yayıncı", "Bağlantı URL", "Fiyat"])

for i in pricenew:
    price = i.find("span", {"class":"value"})
    fiyat.append(price.text.strip().replace(",",".")+" TL")

for i in author:
    yazr = i.find("a", {"class":"alt"})
    yazar.append(yazr.text.strip())

for i in publisher:
    yayinci = i.find("a", {"class":"alt"})
    yayın.append(yayinci.text.strip())

for i in list:
    title = i.find("span").text.strip()
    link = i.find("a").get("href")

    writer.writerow([s, title, yazar[s2], yayın[s2], link, fiyat[s2]])
    s2 += 1
    s += 1
print(table)
print("Bitti")
