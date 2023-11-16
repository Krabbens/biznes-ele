import time
import random

from selenium.common import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# TODO: add asserts?
class AddRandomFromCategoriesToCart:
    def __init__(self, website_addr, browser, products_num, categories_num):
        self._website_addr = website_addr
        self._browser = browser
        self._products_num = products_num
        self._categories_num = categories_num

        self._categories_filters_addr = ['&q=Kategorie-Art', '&q=Kategorie-Produkty+powiązane']
        num = random.randint(1, 7)  # After scrapper it should be (1,10) - art has only 7 products.
        self._num_products_from_categories = [num, 10 - num]

    def run(self):
        products_links_category_first = self._getProductsLinks(self._website_addr + self._categories_filters_addr[0],
                                                               self._num_products_from_categories[0])
        products_links_category_second = self._getProductsLinks(self._website_addr + self._categories_filters_addr[1],
                                                                self._num_products_from_categories[1])

        for product_link in products_links_category_first:
            self._addProductToCartRandomQuantity(product_link)

        for product_link in products_links_category_second:
            self._addProductToCartRandomQuantity(product_link)

    def _getProductsLinks(self, addr, num):
        self._browser.get(addr)

        WebDriverWait(self._browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'product'))
        )

        products = self._browser.find_elements(By.CLASS_NAME, 'thumbnail')
        product_links = [element.get_attribute("href") for element in products]

        return random.sample(product_links, k=num)

    def _addProductToCartRandomQuantity(self, product_link):
        self._browser.get(product_link)

        # page loaded
        WebDriverWait(self._browser, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'form-control'))
        )

        # check if customizable product (can't add to cart without customizing)
        try:
            _ = WebDriverWait(self._browser, 0.1).until(
                EC.element_to_be_clickable((By.CLASS_NAME, 'add-to-cart'))
            )
        except TimeoutException:
            customization_box = self._browser.find_element(By.CLASS_NAME, 'product-message')
            customization_box.send_keys("Selenium test")

            submit_customization = self._browser.find_element(By.NAME, 'submitCustomizedData')
            submit_customization.click()

        try:
            WebDriverWait(self._browser, 0.1).until(
                EC.presence_of_element_located((By.XPATH, "//span[@data-stock]"))
            )
            available_quantity = self._browser.find_element(By.XPATH, "//span[@data-stock]")
            available_quantity = available_quantity.get_attribute("data-stock")
        except TimeoutException:
            available_quantity = 2  # sometimes quantity is not provided (eg selling ebooks)

        quantity_box = self._browser.find_element(By.NAME, 'qty')  # prestashop quantity input name = 'qty'
        quantity_box.send_keys(Keys.DELETE)
        t = random.randint(1, int(available_quantity))
        quantity_box.send_keys(t)

        add_to_cart_button = self._browser.find_element(By.CLASS_NAME, 'add-to-cart')
        add_to_cart_button.click()

        WebDriverWait(self._browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'cart-products-count'))
        )
