import time
import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
from pages.results_page import ResultsPage

class TestMap:
    def setup_method(self):
        options = uc.ChromeOptions()
        options.add_argument('--disable-blink-features=AutomationControlled')
        self.driver = uc.Chrome(options=options, version_main=147)
        self.driver.maximize_window()

    def teardown_method(self):
        if self.driver: self.driver.quit()

    def test_open_map(self):
        page = ResultsPage(self.driver)
        page.open()
        time.sleep(12)
        
        try: self.driver.find_element("tag name", "body").send_keys(Keys.ESCAPE)
        except: pass
        
        page.go_to_map()
        assert page.is_on_map(), "Помилка: Ми не перейшли на карту!"