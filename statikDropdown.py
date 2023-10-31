from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tomspizzeria.b4a.app")
dropdown = driver.find_element(By.ID , "odeme-tipi")

odeme = Select(dropdown)
odeme_tipleri = odeme.options  #web element listesi , her bişr option tagı

for tip in odeme_tipleri:
    print(tip.text)
sleep(2)
odeme.select_by_visible_text("Kredi Kartı")  #selenium benim verdiğim texti direk seçecek
sleep(2)
odeme.select_by_index(3)  #benim seçtiğimm indexi verecek

sleep(2)
