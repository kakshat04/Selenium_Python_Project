from selenium import webdriver
from pages.home.login_pages import LoginPage
import unittest
import time
import pytest


@pytest.mark.usefixtures("oneTimeSetUp")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.lp = LoginPage(self.driver)

    @pytest.mark.run(order=2)
    def test_valid_login(self):
        self.lp.login_page(email="test@email.com", password="abcabc")
        time.sleep(2)
        assert self.lp.verify_login_successful() is True  # Verify login successful
        self.driver.quit()

    @pytest.mark.run(order=1)
    def test_invalid_login(self):
        self.lp.login_page(email="1002@email.com", password="acbacb")
        time.sleep(2)
        assert self.lp.verify_login_failed() is True  # Verify login not successful
