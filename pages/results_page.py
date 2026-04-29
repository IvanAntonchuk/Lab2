import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ResultsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://lun.ua/uk/новобудови-києва"

    MORE_MENU = (By.XPATH, "//*[normalize-space(text())='Інше']")
    USD_OPTION = (By.XPATH, "//*[normalize-space(text())='$']")
    LANGUAGE_EN = (By.XPATH, "//a[contains(@href, '/en')]")
    ONE_ROOM_FILTER = (By.XPATH, "//a[contains(@href, '1-kimnatni')] | //button[contains(., '1 кімн')]")
    MAP_BUTTON = (By.XPATH, "//a[contains(@href, 'map') and not(contains(@href, 'sitemap'))]")

    def open(self):
        self.driver.get(self.url)

    def change_currency_to_usd(self):
        self.js_click(self.MORE_MENU)
        time.sleep(2)
        self.js_click(self.USD_OPTION)
        time.sleep(5) 

    def is_usd_applied(self):
        return "$" in self.driver.page_source

    def change_language_to_en(self):
        try:
            self.js_click(self.LANGUAGE_EN)
        except:
            self.driver.get(self.driver.current_url.replace("/uk/", "/en/"))
        time.sleep(5)

    def is_english_applied(self):
        return "/en/" in self.driver.current_url.lower()

    def filter_one_room(self):
        try:
            self.js_click(self.ONE_ROOM_FILTER)
        except:
            self.driver.get("https://lun.ua/uk/новобудови-києва?rooms=1")
        time.sleep(5)

    def is_filtered_by_one_room(self):
        url = self.driver.current_url.lower()
        return "1" in url or "kimnatni" in url

    def go_to_map(self):
        try:
            self.js_click(self.MAP_BUTTON)
        except:
            self.driver.get("https://lun.ua/uk/новобудови-києва/map")
        time.sleep(5)

    def is_on_map(self):
        return "map" in self.driver.current_url.lower()