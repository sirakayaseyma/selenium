from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome() 
driver.maximize_window() 
driver.get("https://www.imdb.com/")
menu = driver.find_element(By.ID, "imdbHeader-navDrawerOpen")
menu.click()
sleep(2)
mbs = driver.find_element(By.XPATH, "/html/body/div[2]/nav/div[2]/aside[1]/div/div[2]/div/div[1]/span/div/div/ul/a[2]")
mbs.click()
film_isimleri = driver.find_elements(By.XPATH, "//ul/li/div[@class='ipc-metadata-list-summary-item__c']")
#find_element => hepsini verir

# for i in range(20):
#     print(film_isimleri[i].text)

for i in film_isimleri:
    if i.text[-5:-1] == "2000":
        print(i.text)


sleep(2)