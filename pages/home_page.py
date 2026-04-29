from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input[placeholder="Місто, район, вулиця, ЖК"]')
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    CURRENCY_BUTTON = (By.XPATH, "//button[contains(text(), 'UAH') or contains(text(), 'USD')]")
    CURRENCY_USD = (By.XPATH, "//li[contains(text(), 'USD')]")

    def open(self):
        """Відкриває головну сторінку LUN"""
        self.open_page()

    def enter_search_keyword(self, keyword):
        """Вводить текст у головний рядок пошуку"""
        self.enter_text(self.SEARCH_INPUT, keyword)

    def click_search(self):
        """Натискає кнопку пошуку"""
        self.click_element(self.SEARCH_BUTTON)

    def change_currency_to_usd(self):
        """Перемикає валюту на долари"""
        self.click_element(self.CURRENCY_BUTTON)
        self.click_element(self.CURRENCY_USD)