from selenium.webdriver.common.by import By

class HomePageSelectors:
    # Home page selectors here
    SVG_POP_UP = (By.XPATH,  "//svg[@class='ic']")
    ACCOUNT_BUTTON = (By.XPATH, "//label[normalize-space()='Account']")
    SIGN_IN_BUTTON = (By.XPATH, "//a[normalize-space()='Sign In']")
    INPUT_MOBILE_EMAIL = (By.ID, "input_identifierValue")
    CONTINUE_BTN = (By.XPATH, "//button[@type='submit']//span[@class='mdc-button__touch']")
    SVG_POP_UP_CLOSE = (By.XPATH, "//button[@class='cls']")
    SEARCH_BAR_INPUT = (By.ID, "fi-q")
    SEARCH_BTN = (By.XPATH, "//button[normalize-space()='Search']")
    CARD_TEXT_ELECT_DRY_IRON = (By.XPATH, "//h3[contains(text(),'AILYONS HD-199A Electric Dry Iron Box Silver & Bla')]")

    CARD_IMAGE = (By.XPATH, "//img[@class='img']")
    CART_ADD_BTN = (By.XPATH, "//button[@class='add btn _prim -pea _i -fw']")
    NOTIFICATION_BAR = (By.XPATH, "//aside[@class='noti']")
    CART_MENU = (By.XPATH, "//a[normalize-space()='Cart']")

class LoginPageSelectors:
    # Login page selectors
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
