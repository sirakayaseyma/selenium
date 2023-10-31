from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tomspizzeria.b4a.app")
orta_boy = driver.find_element(By.CSS_SELECTOR, "input[value='Orta']")
zeytin = driver.find_element(By.CSS_SELECTOR, "input[value='zeytin']")
mantar = driver.find_element(By.CSS_SELECTOR, "input[value='mantar']")
print(orta_boy.is_selected())   #is_selected => seçili mi diye kullanımlarda geçerlidir. seçili değilse false olur
print(zeytin.is_selected())
print(mantar.is_selected())

orta_boy.click()
zeytin.click()
mantar.click()

print(orta_boy.is_selected())
print(zeytin.is_selected())
print(mantar.is_selected())


sleep(3)