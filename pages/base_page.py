from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def js_click(self, locator):
        """Клік через JavaScript (ігнорує перекриття іншими вікнами)"""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def js_type(self, locator, text):
        """Ввід тексту через JavaScript (найшвидший і найнадійніший спосіб)"""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].value = '';", element)
        self.driver.execute_script(f"arguments[0].value = '{text}';", element)
        self.driver.execute_script("arguments[0].dispatchEvent(new Event('input', { bubbles: True }));", element)