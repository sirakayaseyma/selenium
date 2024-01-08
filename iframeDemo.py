from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tobeto.com/giris")
sleep(3)
        
# İframe geçişini beklemek için implicit veya explicit bekleme kullanabilirsiniz.
iframe = driver.find_element(By.ID, "exw-launcher-frame")
driver.switch_to.frame(iframe)

# İçeriklerin yüklenmesini beklemek için explicit bekleme kullanabilirsiniz.
launcher_button = driver.find_element(By.ID, "launcher")
launcher_button.click()
sleep(20)
adsoyad = driver.find_element(By.XPATH, "//*[@id='exw-messages']/div[2]/div[2]/div[2]/input")
adsoyad.send_keys("Şeyma ")
sleep(4)

#default_content => en ana sayfaya dön , sayfanın aslına dön
#parent_frame => bir üstteki frame'e geçiş yap 
# 1.anasayfa
#     2.frame1 frame1den ana sayfaya geçmek için parent_frame kulanılabilir
#         3.frame2  frame 2den frame1e geçmek için parent_frame kullanılabilir

#driver.switch_to.default_content()
sleep(3)