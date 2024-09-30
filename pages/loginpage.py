import time

from selenium.webdriver.common.by import By
from locate.locators import Locate

class Login:
    def __init__(self, driver):
        self.driver = driver
        self.lp = Locate()

    def get_nav_login(self):
        nav_login = self.driver.find_element(By.ID, self.lp.nav_login_id)
        return nav_login
    def clicknavlogin(self):
        self.get_nav_login().click()

    def get_user_name(self):
        uname = self.driver.find_element(By.ID, self.lp.uname_id)
        return uname

    def enter_username(self, usname):
        self.get_user_name().send_keys(usname)

    def get_password(self):
        pwd = self.driver.find_element(By.ID, self.lp.pwd_id)
        return pwd

    def enter_password(self,pwwd):
        self.get_password().send_keys(pwwd)

    def get_login_button(self):
        button_login = self.driver.find_element(By.XPATH, self.lp.ib_xpth)
        return button_login

    def click_login_button(self):
        self.get_login_button().click()



    def loginpage(self,usname,pwwd):
        driver = self.driver
        self.clicknavlogin()
        driver.implicitly_wait(10)
        self.enter_username(usname)
        self.enter_password(pwwd)
        self.click_login_button()

        time.sleep(10)