from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base import BasePage


class LoginPage(BasePage):
    """Login page object with methods for email, password, and login button"""
    
    # Locators for DMS login page
    EMAIL_INPUT = (By.XPATH, "//input[@id='username']")  # Username/email input field
    PASSWORD_INPUT = (By.XPATH, "//input[@id='password']")  # Password input field
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")  # Login button
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def enter_email(self, email):
        """Enter email into the email input field"""
        email_field = self.wait.until(
            EC.presence_of_element_located(self.EMAIL_INPUT)
        )
        email_field.clear()
        email_field.send_keys(email)
        return self
    
    def enter_password(self, password):
        """Enter password into the password input field"""
        password_field = self.wait.until(
            EC.presence_of_element_located(self.PASSWORD_INPUT)
        )
        password_field.clear()
        password_field.send_keys(password)
        return self
    
    def click_login(self):
        """Click on the login button"""
        login_btn = self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        )
        login_btn.click()
        return self
    
    def login(self, email, password):
        """Complete login flow: enter email, password, and click login"""
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()
        return self

