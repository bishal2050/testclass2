import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoblaze.com")

nav_login = driver.find_element(By.ID, "login2")
nav_login.click()
time.sleep(5)
uname = driver.find_element(By.ID, 'loginusername')
uname.send_keys("testmorning")
pwd = driver.find_element(By.ID, 'loginpassword')
pwd.send_keys("test123")
button_login = driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
button_login.click()
time.sleep(10)