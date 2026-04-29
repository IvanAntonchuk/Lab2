import time
import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
from pages.results_page import ResultsPage

class TestCurrency:
    def setup_method(self):
        options = uc.ChromeOptions()
        options.add_argument('--disable-blink-features=AutomationControlled')
        self.driver = uc.Chrome(options=options, version_main=147)
        self.driver.maximize_window()

    def teardown_method(self):
        if self.driver:
            self.driver.quit()

    def test_change_currency_to_usd(self):
        results_page = ResultsPage(self.driver)
        
        # 1. Відкриваємо сайт
        results_page.open()
        
        # Чекаємо 15 секунд для Cloudflare
        time.sleep(15)
        
        # Закриваємо зайві вікна (куки), якщо є
        try:
            self.driver.find_element("tag name", "body").send_keys(Keys.ESCAPE)
            time.sleep(1)
        except:
            pass
        
        # 2. Відкриваємо меню і міняємо валюту
        try:
            results_page.change_currency_to_usd()
        except Exception as e:
            self.driver.save_screenshot("menu_error.png")
            assert False, f"Не зміг клікнути на $. Дивись menu_error.png"

        # 3. Перевірка
        assert results_page.is_usd_applied(), "Символ $ не з'явився на сторінці!"