from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()  
driver.maximize_window() 
driver.implicitly_wait(30)
driver.get("https://www.apple.com/")
sleep(2)
driver.switch_to.new_window("tab")#yeni bir pencere açmama yardımcı olur. Selenim için hem sayfa hem sekme açmak aynı şey gibi görüyor
#tab => yeni sekme açmamı saplar.
#window => yeni pencere açmamı sağlar. 
driver.get("http://www.tesla.com") #gittiğim yeni sekme veya sayfada açmak istediğim site 
sleep(3)
