import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ResultsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://lun.ua/uk/"

    # Локатори
    MORE_MENU = (By.XPATH, "//*[normalize-space(text())='Інше']")
    # Шукаємо саме значок $, бо на твоєму фото буков USD немає!
    USD_OPTION = (By.XPATH, "//*[normalize-space(text())='$']")

    def open(self):
        self.driver.get(self.url)

    def change_currency_to_usd(self):
        # Відкриваємо меню "Інше"
        self.js_click(self.MORE_MENU)
        time.sleep(2)
        
        # Натискаємо на значок долара
        self.js_click(self.USD_OPTION)
        time.sleep(5) 

    def is_usd_applied(self):
        # Якщо ми натиснули на долар, він має з'явитися в цінах на сторінці
        page_text = self.driver.page_source
        return "$" in page_text