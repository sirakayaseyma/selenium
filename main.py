from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # Chrome kullanmamı sağlıyor
driver.maximize_window() #Sayfayı büyütmemi sağlıyor
driver.get("https://www.apple.com/")
link = driver.current_url   #Şu anki başlığı göstermeme yardımcı olur

baslik = driver.title
print("sayfa başlığı:" + baslik)
if "apple.com" in link:
 print("Doğru sayfadasın " + link)
sleep(2)


driver.get("https://www.etsy.com/")
link = driver.current_url

baslik = driver.title
print("sayfa başlığı:" + baslik)
driver.save_screenshot("./etys.png")
if "etsy" in link:
 print("Doğru sayfadasın " + link)

 driver.back()  #önceki sayfaya geri dön
 baslik = driver.title
 driver.save_screenshot("./apple.png")
 if "Apple" in baslik:
  print("Tebrikler Apple sayfasına döndün")
# else:
#  driver.save_screenshot("./ekrangrountusu.png") #ekran görüntüsü almamı sağlar.

sleep(2)

# driver.close() => şuanki pencereyi kapatır.
# driver.quit() => seleniumun kullandığı tüm pencereleri kapatır.
driver.refresh() #sayfayı yeniler
sleep(2)



driver.quit()