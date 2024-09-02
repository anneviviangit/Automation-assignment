import pytest
from utilities.webdriver_setup import WebDriverSetup

class BaseTest(WebDriverSetup):

    @pytest.fixture(autouse=True)
    def setup(self, request):
        self.driver = self.get_driver()
        request.cls.driver = self.driver
        yield
        self.driver.quit()