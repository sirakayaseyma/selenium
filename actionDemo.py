from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/hovers")

user = driver.find_element(By.CSS_SELECTOR, "div.figure")
isim = driver.find_element(By.CSS_SELECTOR, "div.figcaption h5")
link = driver.find_element(By.CSS_SELECTOR, "div.figcaption a")

sleep(3)

hareket = ActionChains(driver)
hareket.move_to_element(user) ##user uzerinde fare hareketi yapacak
hareket.perform() # perform demekssek actions Change ile kullanıan nesneler geçersiz olacaktır


sleep(3)
print("--------")
print(user.is_displayed) #true dönmesi lazım
print("isim: " + user.text)
link.click()
sleep(3)

url = driver.current_url
assert "users/1" in url
sleep(3)