from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tomspizzeria.b4a.app")

def siparisver():
    siparis = driver.find_element(By.ID,"siparis")
    siparis.click()

def mesajoku():
    return driver.find_element(By.ID,"mesaj").text

# müşteri ismini test etmemiz gerekir.
siparisver()
mesaj = mesajoku()

#müşteri ismi girmediniz
assert mesaj == "Müşteri ismi girmediniz"
sleep(2)

#pizza boyunu test etme
isim = "Osman Sırakaya"
driver.find_element(By.ID, "musteri-adi").send_keys(isim)
siparisver()

#Pizza boyutu seçmediniz
mesaj = mesajoku()
assert mesaj == "Pizza boyu seçmediniz"
sleep(2)

# ödeme şekli test etme 
driver.find_element(By.CSS_SELECTOR, "input[value='Küçük']").click()
siparisver()
mesaj = mesajoku()

#ödeme şekli seçmediniz
assert mesaj == "Ödeme tipi seçmediniz"
sleep(4)

zeytin = driver.find_element(By.CSS_SELECTOR, "input[value='zeytin']")
mantar = driver.find_element(By.CSS_SELECTOR, "input[value='mantar']")
zeytin.click()
mantar.click()

#siparişiniz alındı.
dropdown = driver.find_element(By.ID, "odeme-tipi")
odeme = Select(dropdown)
odeme.select_by_index(1)
siparisver()
mesaj = mesajoku()
assert mesaj == "Siparişiniz alındı"


musteri = driver.find_element(By.ID, "musteri").text
boy = driver.find_element(By.ID, "pizzaboyu").text
ek = driver.find_element(By.ID, "pizzaustu").text
odeme = driver.find_element(By.ID, "odeme").text
tutar = driver.find_element(By.ID, "tutar").text

assert musteri == "Müşteri ismi: " + isim
assert boy == "Pizza boyu: Küçük"
assert ek == "Pizza üstü: zeytin, mantar"
assert odeme == "Ödeme tipi: Nakit"
assert tutar == "Tutar: 10 TL"
driver.save_screenshot("./pizzasiparis.png")
sleep(5)
