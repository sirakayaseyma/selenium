from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome()
driver.maximize_window()
#driver.implicitly_wait(30) #performans sorunu olup olmadığının kontrolünü sağlar.
# driver nesnesi ile çalışıyor.
driver.get("http://pynishant.github.io/Selenium-python-waits.html")

tryit = driver.find_element(By.XPATH, "//button[contains(text(), 'Try it')]").click()

WebDriverWait(driver, 45).until(expected_conditions.presence_of_all_elements_located((By.XPATH, "//button[contains(text(), 'CLICK ME')]")))

clickme = driver.find_element(By.XPATH, "//button[contains(text(), 'CLICK ME')]").click()

#presence  vs visibilty(kullanıcıya görünmeyebilir)
# implicit wait - gizli bekleme
# explicit wait - açıktan bekleme
#fluent wait 
sleep(3)