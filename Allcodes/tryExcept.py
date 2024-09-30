import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoblaze.com")

try:
    try:
        nav_login = driver.find_element(By.ID, "login2")
        nav_login.click()
        uname = driver.find_element(By.ID, 'loginusername')
        uname.send_keys("testmorning")
        pwd = driver.find_element(By.ID, 'loginpassword')
        pwd.send_keys("test123")
        button_login = driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
        button_login.click()
        time.sleep(10)
    except ElementNotInteractableException:
        print("This is from element not interactable exception")
        driver.implicitly_wait(10)
        uname = driver.find_element(By.ID, 'loginusername2')
        uname.send_keys("testmorning")
        pwd = driver.find_element(By.ID, 'loginpassword')
        pwd.send_keys("test123")
        button_login = driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
        button_login.click()
        time.sleep(10)
except Exception as e:
    print(e)
