from telnetlib import EC

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class ProductPage(BasePage):
    ADD_TO_CART = (By.ID, "add-to-cart-button")
    PRODUCT_TITLE = (By.ID, "productTitle")

    def add_to_cart(self):
        self.click(*self.ADD_TO_CART)

    def verify_on_product_page(self):
        assert "Amazon.com.tr" in self.driver.title, "Not on product page."
        product_title = self.find_element(*self.PRODUCT_TITLE)
        assert product_title.is_displayed(), "Product title is not displayed."
