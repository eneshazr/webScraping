# https://yazilimfuryasi.com/selenium-ile-hava-durumu-botu/


from selenium import webdriver
from bs4 import BeautifulSoup
import time

# Selenium Ayarları
browserProfile = webdriver.ChromeOptions()
browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'tr,tr_TR'})
browser = webdriver.Chrome('Desktop/Python/chromedriver.exe', chrome_options=browserProfile)

# Kullanıcıdan Bilgi Alma
il = input("İl: ").lower().capitalize()         # Girilen karakterleri lower ile küçült, capitalize ile ilk harfi büyüt.
ilce = input("İlçe: ").lower().capitalize()
url = browser.get(f"https://www.mgm.gov.tr/tahmin/il-ve-ilceler.aspx?il={il}&ilce={ilce}")

# Kaynak kodlarını çekiyor
kaynak = browser.page_source
# Beautifulsoup ile parse ediyor
soup = BeautifulSoup(kaynak, "html.parser")
time.sleep(1)

# Etiketler
anlikDurumTarih = soup.find("span",{"class":"ad_time ng-binding"})
anlikDerece = soup.find("div", {"class":"anlik-sicaklik-deger ng-binding"})
anlikHava = soup.find("div", {"class":"anlik-sicaklik-havadurumu-ikonismi ng-binding"})
anlikNem = soup.find("div", {"class":"anlik-nem-deger-kac ng-binding"})

# Ekrana Yazdırma
print(f"""
İl: {il}/{ilce}
Tarih: {anlikDurumTarih.text}
Sıcaklık: {anlikDerece.text}°C
Hava: {anlikHava.text}
Nem: %{anlikNem.text}
""")
