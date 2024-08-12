from telnetlib import EC

from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class CartPage(BasePage):
    CART_PAGE_HEADER = (By.CSS_SELECTOR, "h1.a-size-medium")  # Sepet başlığı için CSS seçici
    CART_ITEM = (By.CSS_SELECTOR, ".sc-list-item")
    CART_PAGE_HEADER_TEXT = "Sepetim"

    def verify_on_cart_page(self):
        try:

            WebDriverWait(self.driver, 10).until(
                EC.text_to_be_present_in_element(
                    (By.CSS_SELECTOR, "h1.a-size-medium"),
                    self.CART_PAGE_HEADER_TEXT
                )
            )
            print("Cart page is displayed correctly.")
        except TimeoutException:
            raise AssertionError("Timed out waiting for cart page to load.")