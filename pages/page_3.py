from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Page3:
    def __init__(self, driver):
        self.driver = driver
    def napisz_nam_swoj_ulubiony_wierszyk_input(self):
        return (By.ID, "Napisz nam swój ulubiony wierszyk")
    def zakoncz_btn(self):
        return (By.ID,"btn-navigation-finish")