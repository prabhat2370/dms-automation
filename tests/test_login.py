import time
from pages.login_page import LoginPage

EMAIL = "apiuser@ripplr.in"
PASSWORD = "R!pp1r@2023"


def test_login(driver):
    login_page = LoginPage(driver)
    login_page.open_url("https://dms-preprod.ripplr.in/#/login")
    assert "Distribution" in driver.title

    login_page.login(EMAIL, PASSWORD)

    # Optional wait to observe the result; shorten/remove as needed
    time.sleep(5)

