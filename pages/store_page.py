from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.base import BasePage
from selenium.webdriver.common.keys import Keys


class StorePage(BasePage):
    onboarding_button = (By.XPATH, "//span[normalize-space()='Onboarding']")


    def go_to_onboarding(self):
        onboarding_button = self.wait.until(
            EC.element_to_be_clickable(self.onboarding_button)
        )
        onboarding_button.click()
        return self

   