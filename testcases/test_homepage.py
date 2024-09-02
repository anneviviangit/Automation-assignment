import pytest
from pages.home_page import HomePage
from base.base_test import BaseTest


@pytest.mark.usefixtures("setup")
class TestHomePage(BaseTest):
    def test_open_jumia_homepage(self):
        home_page = HomePage(self.driver)
        home_page.open_homepage()

    def test_login(self):
        home_page = HomePage(self.driver)
        home_page.login()

    def test_search_for_item(self):
        home_page = HomePage(self.driver)
        home_page.search_for_item("ailyons hd-199a electric dry iron box silver & black (1 yr wrty)")

    def test_add_to_cart(self):
        home_page = HomePage(self.driver)
        home_page.add_to_cart()

    def test_navigate_to_cart(self):
        home_page = HomePage(self.driver)
        home_page.navigate_to_cart()
