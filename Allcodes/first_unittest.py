import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://demoblaze.com")

    def tearDown(self):
        self.driver.close()


    def test_something(self):
        driver = self.driver
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
                uname = driver.find_element(By.ID, 'loginusername')
                uname.send_keys("testmorning")
                pwd = driver.find_element(By.ID, 'loginpassword')
                pwd.send_keys("test123")
                button_login = driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
                button_login.click()
                time.sleep(10)
        except Exception as e:
            print(e)

        expected_result = "Welcome testmorning"
        actaul_result = driver.find_element(By.ID, "nameofuser").text
        self.assertEqual(expected_result, actaul_result, "Username and logged in username didn't match")




if __name__ == '__main__':
    unittest.main()
