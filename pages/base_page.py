from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://lun.ua/"

    def open_page(self):
        """Відкриває головну сторінку"""
        self.driver.get(self.base_url)

    def find_element(self, locator, time=10):
        """Шукає елемент на сторінці з очікуванням до 10 секунд"""
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Не зміг знайти елемент за локатором {locator}"
        )

    def click_element(self, locator, time=10):
        """Шукає елемент і клікає на нього"""
        element = WebDriverWait(self.driver, time).until(
            EC.element_to_be_clickable(locator),
            message=f"Елемент не клікабельний {locator}"
        )
        element.click()

    def enter_text(self, locator, text, time=10):
        """Шукає поле і вводить туди текст"""
        element = self.find_element(locator, time)
        element.clear()
        element.send_keys(text)