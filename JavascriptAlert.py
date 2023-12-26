from selenium.webdriver.common.by  import By
from selenium.webdriver.support  import expected_conditions
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

driver = webdriver.Chrome()  
driver.maximize_window() 
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

#alert mesajı cancel yapma 
# buton2 = driver.find_element(By.XPATH, "(//button)[2]")
# buton2.click()
# WebDriverWait(driver,3).until(expected_conditions.alert_is_present()) #alert var olana kadar 3 sn bekle 
# alert = Alert(driver)
# sleep(2)
# mesaj = alert.text
# alert.dismiss()  #dismiss hayır seçeneğini seçmeme yardımcı olur
# result = driver.find_element(By.ID , "result").text
# print(f"mesaj: {mesaj}")
# print(f"sonuc: {result}")


#alert mesajı kutu içinde kendin yazma
buton2 = driver.find_element(By.XPATH, "(//button)[3]")
buton2.click()
WebDriverWait(driver,3).until(expected_conditions.alert_is_present()) #alert var olana kadar 3 sn bekle 
alert = Alert(driver)
sleep(2)
mesaj = alert.text
alert.send_keys("Seyma Sirakaya")  #içine metin girmeme yardım olan alert classı
sleep(3)
alert.accept() #ok tuşuna basmama yardımcı olur kabul eder.
sleep(3)
result = driver.find_element(By.ID , "result").text
print(f"mesaj: {mesaj}")
print(f"sonuc: {result}")
