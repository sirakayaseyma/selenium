from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()

def login(username,password):
    driver.get("https://the-internet.herokuapp.com/login")
    kullanici_adi = driver.find_element(By.NAME, "username")
    kullanici_adi.send_keys(username) 
    sifre = driver.find_element(By.NAME, "password")
    sifre.send_keys(password)
    login_button = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/form/button")
    login_button.click()
    mesaj = driver.find_element(By.ID, "flash").text
    return mesaj

mesaj = login("asde", "ppppp")

#assert doğrulama yapar , kodu işletmeye devam eder
assert "Your username is invalid" in mesaj

# if "Your username is invalid" in mesaj:
#     print("Ok! kullanici adi yanlış ")
# else:
#     print("Hata: yanlış kullanici adi çalışmıyor")


mesaj = login("tomsmith" , "asdf")

assert "Your password is invalid" in mesaj

# if "Your password is invalid" in mesaj:
#     print("Ok! şifre yanlış ")
# else:
#     print("Hata: yanlış şifre çalışmıyor")


mesaj = login("tomsmith" , "SuperSecretPassword!")

assert "You logged into a secure area!" in mesaj

# if "You logged into a secure area!" in mesaj:
#     print("Ok! doğru bilgi kullanici adı ve  şifre doğru ")
# else:
#     print("Hata: doğru bilgiler çalışmıyor")


link = driver.current_url
assert "secure" in link

# if "secure" in link: 
#     print("Link secure içeriyor") 
# else:
#     print("Link secure içermiyor.")


dogru_mesaj = driver.find_element(By.CSS_SELECTOR, "h2 i").text

if "Secure Area" in dogru_mesaj:
    print("başlık doğru")
else: 
    print("başlık yanlış")


#Logout butonu
logout_button = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/a/i").click()

mesaj3 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div").text

if  "You logged out of the secure area!" in mesaj3:
    print("Çıkış işlemi başarılı")
else:
    print("Çıkış başarısız :(")
sleep(5)