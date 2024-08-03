from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium import webdriver
from Ankieta_Dziwnych_Pytan.pages.page_3 import Page3
import time
from Ankieta_Dziwnych_Pytan.test.skip import skip_page3

@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.get("https://qa.thebitbybit.com/form/ankieta-dziwnych-pytan/2")
    assert  driver.title == ("Geoankieta")
    yield driver
    driver.quit()
class Test_Page3:
    def test_page3(self, driver):
        page3 = Page3(driver)
        wait = WebDriverWait(driver, 10)

        # Przeklikanie do strony page3
        skip_page3(driver)

        #driver.find_element(*page3.napisz_nam_swoj_ulubiony_wierszyk_input()).click()
        driver.find_element(*page3.napisz_nam_swoj_ulubiony_wierszyk_input()).send_keys("""
               Nie nowina, że głupi mądrego przegadał
               Kontent więc, iż uczony nic nie odpowiadał,
               Tym bardziej jeszcze krzyczeć przeraźliwie począł;
               Na koniec, zmordowany, gdy sobie odpoczął,
               Rzekł mądry, żeby nie był w odpowiedzi dłużny:
               "Wiesz, dlaczego dzwon głośny? Bo wewnątrz jest próżny
               """)
        driver.find_element(By.CSS_SELECTOR, 'div.overlay').click()
        driver.find_element(By.ID,"btn-navigation-finish").click()