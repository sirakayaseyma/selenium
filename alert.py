from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
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
WebDriverWait(driver,3).until(expected_conditions.alert_is_present()) #sayfada bir js uyarısı görünene kadar bekle
uyari = Alert(driver)
uyari.accept()

#presence  vs visibilty(kullanıcıya görünmeyebilir)
# implicit wait - gizli bekleme
# explicit wait - açıktan bekleme
#fluent wait 
sleep(3)