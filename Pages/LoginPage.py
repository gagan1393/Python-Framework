from selenium.webdriver.common.by import By

from Configuration.config import TestData
from Pages.BasePage import BasePage


class LoginPage(BasePage):

    """By locator"""
    EMAIL_ID = (By.ID, "username")
    PASSWORD_ID = (By.ID, "password")
    LOGINBUTTON_ID = (By.ID, "loginBtn")
    SIGNUP_LINK =(By.LINK_TEXT, "Sign up")

    """constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def get_login_page_title(self, title):
        return self.get_title(title)

    def is_signup_exist(self):
        return self.is_visble(self.SIGNUP_LINK)

    def do_login(self, username, password):
        self.do_send_keys(self.EMAIL_ID, username)
        self.do_send_keys(self.PASSWORD_ID, password)
        self.do_click(self.LOGINBUTTON_ID)

