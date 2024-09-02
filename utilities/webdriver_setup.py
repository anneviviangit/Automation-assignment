from selenium import webdriver
from configFiles.config import Config

class WebDriverSetup:
    def get_driver(self):
        if Config.BROWSER == "chrome":
            driver = webdriver.Chrome()
        elif Config.BROWSER == "firefox":
            driver = webdriver.Firefox()
        else:
            driver = webdriver.Chrome()
        driver.maximize_window()
        return driver
