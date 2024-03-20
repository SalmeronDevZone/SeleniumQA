from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()

driver.get("https://gmail.com")


usuario = driver.find_element(By.ID, "identifierId")
usuario.send_keys("jsalmedev@gmail.com")
usuario.send_keys(Keys.ENTER)


time.sleep(10)  #Tiempo de seguridad de cargado de la página.


passwd = driver.find_element(By.name, "Passwd")
passwd.send_keys("TU_CONTRASEÑA")  #Obviamente no es mi contraseña!!!
passwd.send_keys(Keys.ENTER)
