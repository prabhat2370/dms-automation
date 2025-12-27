import time
from pages.login_page import LoginPage
from pages.sales_order_page import SalesOrderPage

EMAIL = "apiuser@ripplr.in"
PASSWORD = "R!pp1r@2023"


def test_sales_order_flow(driver):
    # Login
    login_page = LoginPage(driver)
    login_page.open_url("https://dms-staging.ripplr.in/#/login")
    login_page.login(EMAIL, PASSWORD)

    # Navigate: Order Management -> Sales Order
    sales_page = SalesOrderPage(driver)
    sales_page.go_to_sales_order()

    # # Click "Create Sales Order" on the Sales Order page
    sales_page.click_create_sales_order()

    # # Select client: search then click "Test Client"
    sales_page.select_client()
    sales_page.select_fc()
    sales_page.select_salesman()
    sales_page.select_store()
    sales_page.select_brand()

    sales_page.click_add_product()
    sales_page.enter_product()
    sales_page.enter_qty()
    sales_page.submit_order()

    sales_page.confirm_order()
    sales_page.order_confirmed()
   
    time.sleep(60)





