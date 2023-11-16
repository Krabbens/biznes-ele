from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SeleniumScraper:
    def __init__(self, driver_path, headless=True):
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless")
        self.service = webdriver.chrome.service.Service(driver_path)
        self.driver = webdriver.Chrome(service=self.service, options=options)

    def visit(self, url):
        self.driver.get(url)

    def from_xpath(self, xpath):
        return self.driver.find_element(By.XPATH, xpath)

    def from_class_name(self, classname):
        return self.driver.find_elements(By.CLASS_NAME, classname)

    def from_css(self, css):
        return self.driver.find_element(By.CSS_SELECTOR, css)