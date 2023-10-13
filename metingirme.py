
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # Chrome kullanmamı sağlıyor
driver.maximize_window() #Sayfayı büyütmemi sağlıyor
driver.get("https://www.duckduckgo.com/")
aramakutusu  = driver.find_element(By.ID , "searchbox_input") #idsi bilinen sayfada arama yapacağım kısmı seçtim
aramakutusu.send_keys("selenium") # arama kısmına ne yazacağımı bildirdiğim alan
aramakutusu.send_keys(Keys.ENTER) #enter tuşunu direk işaretlememe yardımcı oldu. Klavyeden diğer seçeneklerde seçilebir.
sleep(4)


driver.get("https://www.google.com/")
aramakutusu  = driver.find_element(By.NAME , "q") #idsi bilinen sayfada arama yapacağım kısmı seçtim
aramakutusu.send_keys("python") # arama kısmına ne yazacağımı bildirdiğim alan
aramakutusu.send_keys(Keys.ENTER) #enter tuşunu direk işaretlememe yardımcı oldu. Klavyeden diğer seçeneklerde seçilebir.
sleep(4)