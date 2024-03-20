from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Edge()
driver.get('http://google.com')

driver = webdriver.Chrome()
driver.get('http://google.com')

driver = webdriver.Firefox()
driver.get('http://google.com')

