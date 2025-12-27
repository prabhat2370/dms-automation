from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        # Use a higher default timeout to avoid flakiness after login/navigation
        self.wait = WebDriverWait(driver, 30)

    def open_url(self, url):
        self.driver.get(url)
