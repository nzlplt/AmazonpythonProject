from selenium import webdriver

from Tests.base_test import BaseTest
from pages.home_page import HomePage, wait_for_seconds
from pages.search_results_page import SearchResultsPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


class TestAmazon(BaseTest):
    def test_amazon(self):

        home_page = HomePage(self.driver)
        home_page.assert_page_title("Amazon.com.tr")
        home_page.search("samsung")
        search_results_page = SearchResultsPage(self.driver)
        search_results_page.verify_search_results()
        search_results_page.go_to_second_page()
        search_results_page.verify_second_page()
        search_results_page.select_fifth_row_first_item()
        product_page = ProductPage(self.driver)
        product_page.verify_on_product_page()
        cart_page = CartPage(self.driver)
        #cart_page.verify_on_cart_page()
        product_page.add_to_cart()
        wait_for_seconds(2)
        home_page.go_to_home()
        home_page.assert_page_title("Amazon.com.tr")




