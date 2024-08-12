from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SearchResultsPage(BasePage):
    SECOND_PAGE = (By.XPATH, "//a[@aria-label='2 sayfasına git']")
    RESULT_TEXT = (By.XPATH, "//span[contains(text(),'sonuç')]")

    def verify_search_results(self):
        return self.find_element(*self.RESULT_TEXT)

    def go_to_second_page(self):
        self.click(*self.SECOND_PAGE)

    def verify_second_page(self):
        current_url = self.driver.current_url
        if "page=2" not in current_url:
            raise AssertionError("Second page is not displayed")

    def select_fifth_row_first_item(self, row_number=5, column_number=1):
        product_selector = f"(//div[@data-component-type='s-search-result'])[{17}]//h2/a"
        product = self.wait_for_element(By.XPATH, product_selector)
        product.click()
