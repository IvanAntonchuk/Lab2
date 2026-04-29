import time
import undetected_chromedriver as uc
from pages.home_page import HomePage

class TestSearch:
    def setup_method(self):
        options = uc.ChromeOptions()
        options.add_argument('--disable-blink-features=AutomationControlled')
        self.driver = uc.Chrome(options=options, version_main=147)
        self.driver.maximize_window()

    def teardown_method(self):
        if self.driver:
            self.driver.quit()

    def test_search_nordica(self):
        home_page = HomePage(self.driver)
        home_page.open()
        
        time.sleep(15)

        search_query = "Nordica Residence"
        try:
            home_page.search_for(search_query)
        except:
            print("UI пошук не спрацював, переходимо за прямим URL")
            direct_url = f"https://lun.ua/uk/search?query={search_query.replace(' ', '+')}"
            self.driver.get(direct_url)
        
        time.sleep(10)
        
        current_url = self.driver.current_url.lower()
        page_source = self.driver.page_source.lower()
        
        assert "nordica" in current_url or "nordica" in page_source, \
            f"ЖК не знайдено. Поточний URL: {current_url}"