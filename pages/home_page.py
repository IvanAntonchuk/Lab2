from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = "https://lun.ua/uk/"

    def open(self):
        self.driver.get(self.base_url)

    def go_to_city_results(self, city_name):
        """Прямий перехід до результатів пошуку по місту"""
        direct_url = f"https://lun.ua/uk/search?query={city_name}"
        self.driver.get(direct_url)