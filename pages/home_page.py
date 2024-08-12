import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


def wait_for_seconds(seconds):
    time.sleep(seconds)


class HomePage(BasePage):
    SEARCH_BAR = (By.ID, "twotabsearchtextbox")
    LOGO = (By.ID, "nav-logo-sprites")
    ACCEPT_COOKIES = (By.ID, "sp-cc-accept")

    def accept_cookies(self):
        try:
            accept_button = self.find_element(*self.ACCEPT_COOKIES)
            accept_button.click()
        except:

            pass

    def search(self, text):
        self.accept_cookies()
        search_box = self.find_element(*self.SEARCH_BAR)
        search_box.clear()
        search_box.send_keys(text)
        search_box.send_keys(Keys.RETURN)

    def go_to_home(self):
        self.click(*self.LOGO)

