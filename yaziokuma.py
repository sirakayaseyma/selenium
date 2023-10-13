from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tr.wikipedia.org/wiki/Anasayfa")
seckin_madde_alani = driver.find_element(By.ID , "mp-tfa")
seckin_madde_yazisi = seckin_madde_alani.text #web elementin textini veriyor.
seckin_madde_yazisi = seckin_madde_yazisi.split(",")[0] #istediğim kadar kelimeyi almamı sağlıyor. İlk virgüle kadar al
print("seckin madde: " + seckin_madde_yazisi)
kaliteli_madde = driver.find_element(By.ID, "mf-tfp").text
kaliteli_madde = kaliteli_madde.split(",")[0]
print("Kaliteli madde:" + kaliteli_madde)
sleep(2)
