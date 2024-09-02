from base.base_page import BasePage
from pages.selectors import HomePageSelectors
from selenium.webdriver.common.by import By
import time

class MainPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.website_url = "https://www.jumia.co.ke/"

    def open_main_page(self):
        self.go_to_page()
        assert "Jumia" in self.browser.title

    def go_to_page(self):
        self.navigate_to(self.website_url)

    def dismiss_pop_up(self):
        time.sleep(5)
        self.click_element(*HomePageSelectors.SVG_POP_UP_CLOSE)

    def search_item(self, item):
        self.go_to_page()
        self.dismiss_pop_up()
        self.find_element(*HomePageSelectors.SEARCH_BAR_INPUT).send_keys(item)
        self.click_element(*HomePageSelectors.SEARCH_BTN)

        time.sleep(4)
        product_text = self.find_element(*HomePageSelectors.CARD_TEXT_ELECT_DRY_IRON).text
        assert "Dry Iron" in product_text
        time.sleep(4)

    def user_login(self):
        self.go_to_page()
        self.dismiss_pop_up()

        self.click_element(*HomePageSelectors.ACCOUNT_BUTTON)
        time.sleep(2)

        self.click_element(*HomePageSelectors.SIGN_IN_BUTTON)

        time.sleep(5)
        self.browser.find_element(By.ID, "input_identifierValue").send_keys("assessbill5@gmail.com")

        time.sleep(2)
        self.browser.find_element(By.XPATH, "//button[@type='submit']//span[@class='mdc-button__touch']").click()

        time.sleep(2)
        self.browser.find_element(By.XPATH, "//input[@name='password']").send_keys("Albertbill100%")
        time.sleep(3)

    def add_product_to_cart(self):
        self.go_to_page()
        self.dismiss_pop_up()
        self.find_element(*HomePageSelectors.SEARCH_BAR_INPUT).send_keys("ailyons hd-199a electric dry iron box silver & black (1 yr wrty)")
        self.click_element(*HomePageSelectors.SEARCH_BTN)
        self.click_element(*HomePageSelectors.CARD_IMAGE)
        time.sleep(5)
        self.click_element(*HomePageSelectors.CART_ADD_BTN)

        time.sleep(5)
        alert_text = self.find_element(*HomePageSelectors.NOTIFICATION_BAR).text
        assert "successfully" in alert_text

    def go_to_cart(self):
        # Handles browser load and initial navigation
        self.go_to_page()
        self.dismiss_pop_up()

        # Add element to cart
        self.find_element(*HomePageSelectors.SEARCH_BAR_INPUT).send_keys(
            "ailyons hd-199a electric dry iron box silver & black (1 yr wrty)")
        self.click_element(*HomePageSelectors.SEARCH_BTN)
        self.click_element(*HomePageSelectors.CARD_IMAGE)
        time.sleep(5)
        self.click_element(*HomePageSelectors.CART_ADD_BTN)
        time.sleep(5)

        # Navigate to cart
        self.click_element(*HomePageSelectors.CART_MENU)

        # Assert if element is in cart
        cart_product_text = self.find_element(*HomePageSelectors.CARD_TEXT_ELECT_DRY_IRON).text
        assert "Dry Iron" in cart_product_text
