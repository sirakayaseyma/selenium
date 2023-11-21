from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.homeexchange.com/")
driver.execute_script("window.scrollBy(0,300)" , " ")
sleep(3)
#herhangi bir yerdeki durumu bulmak için
showmore = driver.find_element(By.XPATH, "/html/body/div[3]/div[10]/div/div/div[3]/p[2]/a")
driver.execute_script("arguments[0].scrollIntoView();" , showmore)
sleep(3)
# #sayfanın en altına gitmek için 
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
sleep(4) 