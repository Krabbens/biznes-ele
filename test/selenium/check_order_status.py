from selenium.common import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckOrderStatus:
    def __init__(self, website_addr, browser):
        self._website_addr = website_addr
        self._browser = browser

    def run(self):
        self._go_to_account()
        self._go_to_history()
        self._go_to_order_details()

    def _go_to_account(self):
        WebDriverWait(self._browser, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'account'))
        )

        self._browser.find_element(By.CLASS_NAME, 'account').click()

    def _go_to_history(self):
        WebDriverWait(self._browser, 10).until(
            EC.element_to_be_clickable((By.ID, 'history-link'))
        )

        self._browser.find_element(By.ID, 'history-link').click()

    def _go_to_order_details(self):
        WebDriverWait(self._browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-link-action=\"view-order-details\"]"))
        )

        self._browser.find_element(By.CSS_SELECTOR, "a[data-link-action=\"view-order-details\"]").click()
