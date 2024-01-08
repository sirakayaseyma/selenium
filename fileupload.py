from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/upload")


file = "C:/Users/symag/OneDrive/chromedriver"


upload_file = driver.find_element(By.ID, "file-upload")
sleep(3)
upload_file.send_keys(file)

upload_button = driver.find_element(By.ID, "file-submit")

WebDriverWait(driver,30).until(expected_conditions.presence_of_element_located((By.TAG_NAME , "h3")))
baslik = driver.find_element(By.TAG_NAME, "h3").text

print(baslik)

dosya = driver.find_element(By.ID, "uploaded-files").text

print(dosya)


sleep(10)