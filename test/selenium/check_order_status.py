from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckOrderStatusAndDownloadInvoice:
    def __init__(self, website_addr, browser):
        self._website_addr = website_addr
        self._browser = browser

    def run(self):
        self._go_to_account()
        self._go_to_history()
        self._go_to_order_details()
        self._download_invoice()

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

    def _download_invoice(self):
        WebDriverWait(self._browser, 10).until(
            EC.presence_of_element_located((By.ID, 'order-infos'))
        )

        order_infos_div = self._browser.find_element(By.ID, 'order-infos')
        li_elements = order_infos_div.find_elements(By.CSS_SELECTOR, '.box > ul > li')
        for li_element in li_elements:
            try:
                a_element = li_element.find_element(By.TAG_NAME, 'a')
                href_value = a_element.get_attribute('href')
                self._browser.get(href_value)
                return
            except NoSuchElementException as e:
                continue

        print("Invoice not found.")
