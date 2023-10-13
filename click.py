from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # Chrome kullanmamı sağlıyor
driver.maximize_window() #Sayfayı büyütmemi sağlıyor
driver.get("https://www.google.com/")
aramakutusu  = driver.find_element(By.NAME , "q") 
aramakutusu.send_keys("selenium") 
aramakutusu.send_keys(Keys.ENTER)
#driver.find_element(By.CSS_SELECTOR, "div.FPdolc input.gNO89b").click()

sleep(2)