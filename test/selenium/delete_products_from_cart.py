import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DeleteProductsFromCart:
    def __init__(self, website_addr, browser, products_num):
        self._website_addr = website_addr
        self._browser = browser
        self._products_num = products_num

    def run(self):
        product_deletion_links = self._getLinksToDeleteProductsFromCart()
        for link in product_deletion_links:
            self._browser.get(link)

    def _getLinksToDeleteProductsFromCart(self):
        self._browser.get(self._website_addr)

        WebDriverWait(self._browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'remove-from-cart'))
        )

        products = self._browser.find_elements(By.CLASS_NAME, 'remove-from-cart')
        product_links = [element.get_attribute("href") for element in products]

        return random.sample(product_links, k=self._products_num)
