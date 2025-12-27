from re import S
import time
from pages.login_page import LoginPage
from pages.store_page import StorePage

EMAIL = "apiuser@ripplr.in"
PASSWORD = "R!pp1r@2023"


def test_sales_order_flow(driver):
    # Login
    login_page = LoginPage(driver)
    login_page.open_url("https://dms-staging.ripplr.in/#/login")
    login_page.login(EMAIL, PASSWORD)

    # Navigate: Order Management -> Sales Order
    store_page = StorePage(driver)
    store_page.go_to_onboarding()