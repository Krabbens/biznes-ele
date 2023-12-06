from selenium.common import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GoToCartAndPlaceOrder:
    def __init__(self, website_addr, browser):
        self._website_addr = website_addr
        self._browser = browser

    def run(self):
        self._browser.get(self._website_addr)
        self._go_to_cart()
        self._place_order()

    def _go_to_cart(self):
        WebDriverWait(self._browser, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'cart-preview'))
        )

        self._browser.find_element(By.CLASS_NAME, 'cart-preview').click()

    def _place_order(self):
        WebDriverWait(self._browser, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'checkout'))
        )

        self._browser.find_element(By.CLASS_NAME, 'checkout').click()

        WebDriverWait(self._browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'continue'))
        )

        self._set_delivery_info()
        self._choose_carrier()
        self._choose_payment_option()

    def _set_delivery_info(self):
        self._browser.find_element(By.ID, 'field-address1').send_keys('TestAddress 10')
        self._browser.find_element(By.ID, 'field-postcode').send_keys('12-345')
        self._browser.find_element(By.ID, 'field-city').send_keys('TestCity')
        self._browser.find_element(By.NAME, 'confirm-addresses').click()

        WebDriverWait(self._browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'continue'))
        )

    def _choose_carrier(self):
        self._browser.find_element(By.ID, 'delivery_option_2').click()
        self._browser.find_element(By.NAME, 'confirmDeliveryOption').click()

        WebDriverWait(self._browser, 10).until(
            EC.presence_of_element_located((By.ID, 'payment-confirmation'))
        )

    def _choose_payment_option(self):
        self._browser.find_element(By.ID, 'payment-option-2').click()
        self._browser.find_element(By.ID, 'conditions_to_approve[terms-and-conditions]').click()

        WebDriverWait(self._browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary.center-block"))
        )
        self._browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary.center-block").click()
