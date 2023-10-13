#TEST AŞAMALARI 
#internet login sayfasına git => https://the-internet.herokuapp.com/login
#kullanici adi gir
#Şifre gir
#login düğmesine tıkla
#yanlis kullaici adi girersem mesaj: Your username is invalid
#yanlis şifre girersem  mesaj : Your password is invalid
#her ikisi de doğru ise alacağım mesaj : You logged into a secure area! 
#giriş başarılı olunca yeni link: https://the-internet.herokuapp.com/secure olarak değişti ve Secure Area başlıkta yazacak.



from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/login")
kullanici_adi = driver.find_element(By.NAME, "username")
kullanici_adi.send_keys("tomsmith")
sleep(2)
