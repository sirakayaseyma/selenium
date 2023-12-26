from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


# driver = webdriver.Chrome()  
# driver.maximize_window() 
# driver.implicitly_wait(30)
# driver.get("https://www.apple.com/")
# sleep(2)
# print(driver.title) #başlığı yazdırır
# print(driver.current_window_handle) #harflerden ve rakamlardn oluşan handle bilgisini verir

# driver.switch_to.new_window("tab")
# driver.get("http://www.tesla.com") 
# print(driver.title)
# print(driver.current_window_handle)

# print(driver.window_handles) #tüm handle bilgilerini verir.
# sleep(3)


#burada sayfalar arası geçiş yaptıktan sonra bir önceki sayfaya dönmeme handle -bilgisi yardımcı olur.
#bunun için şöyle bir yapı kurabilirim.

driver = webdriver.Chrome()  
driver.maximize_window() 
driver.implicitly_wait(30)
driver.get("https://www.apple.com/")
sleep(2)
print(driver.title) #başlığı yazdırır
apple = driver.current_window_handle #apple handle bilgisini apple değişkenine atadım.
driver.switch_to.new_window("tab")
driver.get("http://www.tesla.com") 
print(driver.title)
tesla = driver.window_handles[1] #bu 1 rakamı birinci indekste yer alan yapımı göstermeme yardımcı olur. 
#tesla 1.indexte gibi , apple 0.indexte olduğu için bu gösterimlede handle yazılabilir.
driver.switch_to.window(apple) #burada handle atadığım apple değişkenini parantez içinde yazıyorum ve ona geri dönüyorum
print(driver.window_handles) #tüm handle bilgilerini verir
print(driver.title)
sleep(2)
driver.switch_to.window(tesla) #burada handle atadığım tesla değişkenini parantez içinde yazıyorum ve ona geri dönüyorum
print(driver.title)
sleep(2)
driver.switch_to.window(apple) #burada handle atadığım apple değişkenini parantez içinde yazıyorum ve ona geri dönüyorum
print(driver.title)
sleep(2)