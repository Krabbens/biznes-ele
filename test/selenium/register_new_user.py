import uuid

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegisterNewUser:
    def __init__(self, website_addr, browser):
        self._website_addr = website_addr
        self._browser = browser

    def run(self):
        self._browser.get(self._website_addr)

        WebDriverWait(self._browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'form-control-submit'))
        )

        self._browser.find_element(By.CSS_SELECTOR, "input[value=\"1\"]").click()
        self._browser.find_element(By.CSS_SELECTOR, "input[name=\"firstname\"]").send_keys("Uzytkownik")
        self._browser.find_element(By.CSS_SELECTOR, "input[name=\"lastname\"]").send_keys("Testowy")
        self._browser.find_element(By.CSS_SELECTOR, "input[name=\"email\"]").send_keys(
            "testowy" + str(uuid.uuid4()) + "@gmail.com")
        self._browser.find_element(By.CSS_SELECTOR, "input[name=\"password\"]").send_keys("testtest")
        self._browser.find_element(By.CSS_SELECTOR, "input[name=\"customer_privacy\"]").click()
        self._browser.find_element(By.CSS_SELECTOR, "input[name=\"psgdpr\"]").click()
        self._browser.find_element(By.CLASS_NAME, 'form-control-submit').click()
