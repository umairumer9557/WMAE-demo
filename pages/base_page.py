from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from config.settings import Settings

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = Settings.URL

    def open(self, url):
        self.driver.get(self.base_url + url)

    def find_element(self, locator):
        return WebDriverWait(self.driver, Settings.TIMEOUT).until(
            EC.presence_of_element_located(locator)
        )

    def find_elements(self, locator):
        return WebDriverWait(self.driver, Settings.TIMEOUT).until(
            EC.presence_of_all_elements_located(locator)
        )




