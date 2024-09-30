import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Alerts.html")

simple_nav = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/ul/li[1]/a')
simple_nav.click()
button1 = driver.find_element(By.XPATH, '//*[@id="OKTab"]/button')
button1.click()
time.sleep(5)
Alert = driver.switch_to.alert
Alert.accept()
time.sleep(5)

confim_nav = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/ul/li[2]/a')
confim_nav.click()
button2 = driver.find_element(By.XPATH, '//*[@id="CancelTab"]/button')
button2.click()
time.sleep(5)

Alert.dismiss()
time.sleep(5)

textbox_nav = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/ul/li[3]/a')
textbox_nav.click()
button3 = driver.find_element(By.XPATH, '//*[@id="Textbox"]/button')
button3.click()
time.sleep(5)
Alert.send_keys("Sarswati")
Alert.accept()
time.sleep(5)