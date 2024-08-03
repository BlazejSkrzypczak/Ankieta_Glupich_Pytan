from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class LandingPage:
    def __init__(self, driver):
        self.driver = driver
    def wypelnij_kwestionariusz_btn(self):
        wypelnij_kwestionariusz_btn = (By.ID, "btn-landingPage-fillIn")
        return wypelnij_kwestionariusz_btn
    def cookie_window(self):
        #wait = WebDriverWait(self.driver, 10)
        cookie = (By.CSS_SELECTOR, "div.rodo-box")
        return cookie
    def cookie_window_close_btn(self):
        cookie_window_close_btn = (By.ID, "btn-rodo-closeRodo")
        return cookie_window_close_btn
