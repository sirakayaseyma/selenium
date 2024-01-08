from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tomspizzeria.herokuapp.com/yeni-sekme.html")
facebook = driver.find_element(By.ID , "facebook").click()
twitter = driver.find_element(By.ID , "twitter").click()
instagram = driver.find_element(By.ID , "instagram").click()
sleep(2)


def sekme_degistir(baslik):
    for sayfa in driver.window_handles:
        driver.switch_to.window(sayfa)
        if baslik.lower() in driver.title.lower():
            break

sekme_degistir("facebook")
print("Facebook : " + driver.title)

sekme_degistir("twitter")
print("Twitter : " + driver.title)

sekme_degistir("instagram")
print("Instagram : " + driver.title)

sleep(5)
