import time
import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
from pages.results_page import ResultsPage

class TestFilter:
    def setup_method(self):
        options = uc.ChromeOptions()
        options.add_argument('--disable-blink-features=AutomationControlled')
        self.driver = uc.Chrome(options=options, version_main=147)
        self.driver.maximize_window()

    def teardown_method(self):
        if self.driver: self.driver.quit()

    def test_one_room_filter(self):
        page = ResultsPage(self.driver)
        page.open()
        time.sleep(12)
        
        try: self.driver.find_element("tag name", "body").send_keys(Keys.ESCAPE)
        except: pass
        
        page.filter_one_room()
        assert page.is_filtered_by_one_room(), "Помилка: Фільтр 1-кімнатних не застосувався!"