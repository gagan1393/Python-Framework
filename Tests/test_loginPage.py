import pytest

from Configuration.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class Test_Login(BaseTest):

    def test_signup_link_visible(self):
        self.LoginPage = LoginPage(self.driver)
        flag = self.LoginPage.is_signup_exist()
        assert flag

    def test_login_page_title(self):
        self.LoginPage = LoginPage(self.driver)
        title = self.LoginPage.get_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE

    def test_login(self):
        self.LoginPage = LoginPage(self.driver)
        self.LoginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
