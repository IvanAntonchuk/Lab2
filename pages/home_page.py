from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://lun.ua/uk/"

    SEARCH_INPUT = (By.NAME, "query")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def open(self):
        self.driver.get(self.url)

    def search_for(self, text):
        """Об'єднаний метод пошуку через JS"""
        self.js_type(self.SEARCH_INPUT, text)
        self.js_click(self.SEARCH_BUTTON)