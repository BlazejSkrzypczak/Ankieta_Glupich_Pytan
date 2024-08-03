from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Ankieta_Dziwnych_Pytan.pages.LandingPage import LandingPage
import pytest
from selenium import webdriver
from Ankieta_Dziwnych_Pytan.pages.page1 import Page1


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.get("https://qa.thebitbybit.com/form/ankieta-dziwnych-pytan/")
    assert  driver.title == ("Geoankieta")
    yield driver
    driver.quit()
class Test_LandingPage:
    def test_cookie_window_displayed(self, driver):
        landing_page = LandingPage(driver)
        cookie_window = landing_page.cookie_window()
        try:
            wait = WebDriverWait(driver, 10)
            wait.until(EC.visibility_of_element_located(cookie_window))
            return driver.find_element(*cookie_window).is_displayed()
        except NoSuchElementException:
            return False
    def test_cookie_window_closed(self, driver):
        landing_page = LandingPage(driver)
        cookie_window_close_btn = landing_page.cookie_window_close_btn()
        driver.find_element(*cookie_window_close_btn).click()
        try:
            wait = WebDriverWait(driver, 10)
            wait.until(EC.invisibility_of_element_located(landing_page.cookie_window()))
            return driver.find_element(*landing_page.cookie_window()).is_displayed()
        except NoSuchElementException:
            return False, "Cookie window did not disappear"
    def test_wypelnij_kwestionariusz_btn(self, driver):
        landing_page = LandingPage(driver)
        page1 = Page1(driver)
        wait = WebDriverWait(driver, 10)
        wypelnij_kwestionariusz_btn = landing_page.wypelnij_kwestionariusz_btn()
        wait.until(EC.element_to_be_clickable(wypelnij_kwestionariusz_btn))
        driver.find_element(*wypelnij_kwestionariusz_btn).click()
        paragraph_element = wait.until(EC.presence_of_element_located(page1.witaj_w_naszej_testowej_ankiecie_paragraph()))
        text = paragraph_element.text
        assert "Witaj w naszej testowej ankiecie!" in text




