from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # Chrome kullanmamı sağlıyor
driver.maximize_window() #Sayfayı büyütmemi sağlıyor
driver.get("https://www.duckduckgo.com/")
sleep(2)
aramakutusu  = driver.find_element(By.ID , "searchbox_input") #classı bilinen sayfada arama yapacağım kısmı seçtim
sleep(2)

aramakutusu.send_keys("selenium") # arama kısmına ne yazacağımı bildirdiğim alan
sleep(2)
#print("Hata mesajı")
butonClc = driver.find_elements(By.CSS_SELECTOR, "#searchbox_homepage > div > div > button")
butonClc.click()

sleep(3)

