#TEST AŞAMALARI 
#internet login sayfasına git => https://the-internet.herokuapp.com/login
#kullanici adi gir
#Şifre gir
#login düğmesine tıkla
#yanlis kullanici adi girersem mesaj: Your username is invalid
#yanlis şifre girersem  mesaj : Your password is invalid
#her ikisi de doğru ise alacağım mesaj : You logged into a secure area! 
#giriş başarılı olunca yeni link: https://the-internet.herokuapp.com/secure olarak değişti ve Secure Area başlıkta yazacak.



from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()


#1.işlem

#internet login sayfasına git => https://the-internet.herokuapp.com/login
driver.get("https://the-internet.herokuapp.com/login")

#1.İŞLEM
#kullanici adi gir
kullanici_adi = driver.find_element(By.NAME, "username")
kullanici_adi.send_keys("qqq")
sleep(1)
#Şifre gir
sifre = driver.find_element(By.NAME, "password")
sifre.send_keys("qqq!")
sleep(2)
#button tıklama 
login_button = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/form/button")
login_button.click()
#yanlis kullanici adi girersem mesaj: Your username is invalid
mesaj = driver.find_element(By.ID, "flash").text

if "Your username is invalid" in mesaj:
    print("Ok! kullanici adi yanlış ")
else:
    print("Hata: yanlış kullanici adi çalışmıyor")

#2.İŞLEM
#yanlis şifre girersem  mesaj : Your password is invalid 

kullanici_adi = driver.find_element(By.NAME, "username")
kullanici_adi.send_keys("tomsmith")

sifre = driver.find_element(By.NAME, "password")
sifre.send_keys("qqq!")
login_button = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/form/button")
login_button.click()
mesaj2 = driver.find_element(By.ID, "flash").text

if "Your password is invalid" in mesaj2:
    print("Ok! şifre yanlış ")
else:
    print("Hata: yanlış şifre çalışmıyor")


#3.İŞLEM
#her ikisi de doğru ise alacağım mesaj : You logged into a secure area! 

kullanici_adi = driver.find_element(By.NAME, "username")
kullanici_adi.send_keys("tomsmith")

sifre = driver.find_element(By.NAME, "password")
sifre.send_keys("SuperSecretPassword!")
login_button = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/form/button")
login_button.click()

mesaj2 = driver.find_element(By.ID, "flash").text

if "You logged into a secure area!" in mesaj2:
    print("Ok! doğru bilgi kullanici adı ve  şifre doğru ")
else:
    print("Hata: doğru bilgiler çalışmıyor")

#giriş başarılı olunca yeni link: https://the-internet.herokuapp.com/secure olarak değişti ve Secure Area başlıkta yazacak.
link = driver.current_url
if "secure" in link: 
    print("Link secure içeriyor") 
else:
    print("Link secure içermiyor.")


dogru_mesaj = driver.find_element(By.CSS_SELECTOR, "h2 i").text

if "Secure Area" in dogru_mesaj:
    print("başlık doğru")
else: 
    print("başlık yanlış")


#Logout butonu
logout_button = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/a/i").click()

mesaj3 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div").text

if  "You logged out of the secure area!" in mesaj3:
    print("Çıkış şlemi başarılı")
else:
    print("Çıkış başarısız :(")
sleep(5)
