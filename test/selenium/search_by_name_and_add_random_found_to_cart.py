import time
import random

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# TODO: fix assert, it should check quantity directly in checkout
# TODO: check if possible to add product (quantity check)
class SearchByNameAndAddRandomFoundToCart:
    def __init__(self, website_addr, browser):
        self._website_addr = website_addr
        self._browser = browser

    def run(self, name):
        self._browser.get(self._website_addr)
        products = self._getProductsByName(name)
        product = self._getRandomProduct(products)
        self._addProductToCart(product)
        self._assertProductInCheckout()

    def _getProductsByName(self, name):
        search_box = self._browser.find_element(By.NAME, 's')  # prestashop searchbar name = 's'
        search_box.send_keys(name)
        search_box.send_keys(Keys.RETURN)

        WebDriverWait(self._browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'product'))
        )

        products = self._browser.find_elements(By.CLASS_NAME, 'product')
        products_flags = self._browser.find_elements(By.CLASS_NAME, 'product-flags')
        assert len(products_flags) == len(products)

        product_in_stock = []
        for idx in range(len(products)):
            if products_flags[idx].find_elements(By.CLASS_NAME, 'out_of_stock'):
                continue

            product_in_stock.append(products[idx])

        return product_in_stock

    def _getRandomProduct(self, products):
        return random.choice(products)

    def _addProductToCart(self, product):
        product.click()

        WebDriverWait(self._browser, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'add-to-cart'))
        )

        add_to_cart_button = self._browser.find_element(By.CLASS_NAME, 'add-to-cart')
        add_to_cart_button.click()

        WebDriverWait(self._browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'cart-products-count'))
        )

    def _assertProductInCheckout(self):
        time.sleep(0.25)

        cart_quantity_element = self._browser.find_element(By.CLASS_NAME, 'cart-products-count')
        formatted_quantity = cart_quantity_element.text[1:-1]
        cart_quantity = int(formatted_quantity)
        assert cart_quantity > 0, "Koszyk nie został zaktualizowany po dodaniu produktu"

