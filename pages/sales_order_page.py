from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.base import BasePage
from selenium.webdriver.common.keys import Keys



class SalesOrderPage(BasePage):

    ORDER_MANAGEMENT_MENU = (By.XPATH, "//span[normalize-space()='Order Management']")
    SALES_ORDER_MENU = (By.XPATH, "//a[normalize-space()='Sales Order']")
    CREATE_SALES_ORDER_BUTTON = (By.XPATH, "//span[contains(text(),'Create Sales Order')]")
    ADD_PRODUCT_BUTTON = (By.CSS_SELECTOR, "button[aria-label='add line item'] span[class='MuiButton-label']")
    ADD_QTY = (By.XPATH, "//input[@id='order_details[0].ordered_qty']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@aria-label='Submit']")
    CONFIRM_BUTTON = (By.XPATH, "(//tr[.//td[normalize-space()='Order Placed']]//button[@aria-label='confirm order'])[1]")
    ORDER_CONFIRMED_MESSAGE = (By.XPATH, "//button[@aria-label='Confirm']")



    CLIENT_INPUT = (By.XPATH, "//input[@id='client_id']")
    FC_INPUT = (By.XPATH, "//input[@id='fc_ids']")
    SALESMAN_INPUT = (By.XPATH, "//input[@id='salesman_id']")
    STORE_INPUT = (By.XPATH, "//input[@id='store_id']")
    BRAND_INPUT = (By.XPATH, "//input[@id='new_brand_id']")
    PRODUCT_INPUT = (By.XPATH, "//input[contains(@id,'order_details')]")
    
    # ✅ FINAL, STABLE DROPDOWN LOGIC
    def _select_from_dropdown(self, input_locator, option_text, timeout=20):
        search_input = self.wait.until(
            EC.element_to_be_clickable(input_locator)
        )

        search_input.click()

        option = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(
                (By.XPATH, f"//strong[normalize-space()='{option_text}']")
            )
        )

        # JS click = stable for your DOM
        self.driver.execute_script("arguments[0].click();", option)

        return self

    def go_to_sales_order(self):
        order_mgmt = self.wait.until(
            EC.visibility_of_element_located(self.ORDER_MANAGEMENT_MENU)
        )
        ActionChains(self.driver).move_to_element(order_mgmt).perform()

        self.wait.until(
            EC.element_to_be_clickable(self.SALES_ORDER_MENU)
        ).click()
        return self

    def click_create_sales_order(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CREATE_SALES_ORDER_BUTTON)
        ).click()
        return self

    def select_client(self):
        return self._select_from_dropdown(
            self.CLIENT_INPUT,
            "Test Client"
        )

    def select_fc(self):
        return self._select_from_dropdown(
            self.FC_INPUT,
            "TF: Btm"
        )

    def select_salesman(self):
        return self._select_from_dropdown(
            self.SALESMAN_INPUT,
            "Api User"
        )

    def select_store(self):
        return self._select_from_dropdown(
            self.STORE_INPUT,
            "TC202: Onboarding Store"
        )

    def select_brand(self):
        return self._select_from_dropdown(
            self.BRAND_INPUT,
            "tElec: testElectronics"
        )

    def click_add_product(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.ADD_PRODUCT_BUTTON)
        ).click()
        
    def enter_product(self):
        return self._select_from_dropdown(
            self.PRODUCT_INPUT,
            "TC62: testelce1"
        )

    def enter_qty(self, qty="10"):
      qty_input = self.wait.until(
          EC.element_to_be_clickable(self.ADD_QTY)
      )

      # Scroll so it becomes interactable
      self.driver.execute_script(
          "arguments[0].scrollIntoView({block:'center'});", qty_input
      )

      # Click on the qty input field first
      qty_input.click()

      # Then enter the quantity
      qty_input.clear()
      qty_input.send_keys(qty)

      return self

    def submit_order(self):
        submit_button = self.wait.until(
            EC.element_to_be_clickable(self.SUBMIT_BUTTON)
        )

        # Click submit button twice
        submit_button.click()
        submit_button.click()

        return self

    def confirm_order(self, timeout=20):
        # Wait for confirm button to appear and click immediately when visible (even after 1 second)
        confirm_button = WebDriverWait(self.driver, timeout, poll_frequency=0.5).until(
            EC.element_to_be_clickable(self.CONFIRM_BUTTON)
        )

        # Click immediately when button becomes clickable
        confirm_button.click()

        return self


    def order_confirmed(self, timeout=20):
        order_confirmed_message = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(self.ORDER_CONFIRMED_MESSAGE)
        )

        return self