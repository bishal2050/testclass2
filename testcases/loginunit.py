import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.loginpage import Login

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://demoblaze.com")
        self.lp = Login(self.driver)



    def test_login(self):
        self.lp.loginpage("testmorning", "test123")
        expected_result = "Welcome testmorning"
        actaul_result = self.driver.find_element(By.ID, "nameofuser").text
        self.assertEqual(expected_result, actaul_result, "Username and logged in username didn't match")

    def test_negative_login(self):
        self.lp.loginpage("testmorning", "test12")
        expected_result = "Welcome testmorning"
        actual_result = self.driver.switch_to.alert.text.title()
        print(actual_result)
        self.assertNotEqual(expected_result,actual_result,"This is same user")

    def tearDown(self) -> None:
        self.driver.quit()




if __name__ == '__main__':
    unittest.main()
