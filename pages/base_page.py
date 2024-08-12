from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def find_element(self, *locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))

    def click(self, *locator):
        element = self.find_element(*locator)
        element.click()

    def type(self, text, *locator):
        element = self.find_element(*locator)
        element.clear()
        element.send_keys(text)

    def get_title(self):
        return self.driver.title

    def assert_page_title(self, title):
        try:
            WebDriverWait(self.driver, self.timeout).until(EC.title_contains(title))
        except TimeoutException:
            raise AssertionError(f"Expected title '{title}' not found")

    def wait_for_element(self, by, value, timeout=10):
            try:
                return WebDriverWait(self.driver, timeout).until(
                    EC.presence_of_element_located((by, value))
                )
            except TimeoutException:
                raise AssertionError(f"Element with locator {value} not found within {timeout} seconds.")