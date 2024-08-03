from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium import webdriver
from Ankieta_Dziwnych_Pytan.pages.page1 import Page1
import time
from Ankieta_Dziwnych_Pytan.test.skip import skip_page1
@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.get("https://qa.thebitbybit.com/form/ankieta-dziwnych-pytan/1")
    assert  driver.title == ("Geoankieta")
    yield driver
    driver.quit()
class Test_Page1:
    def test_page1(self, driver):
        page1 = Page1(driver)
        wait = WebDriverWait(driver, 10)

        #Przeklikanie do strony page1
        skip_page1(driver)

        driver.find_element(*page1.jak_masz_na_imie_input()).send_keys("Błażej")
        driver.find_element(*page1.jaka_jest_twoja_plec_checkbox('m')).click()
        try:
            assert driver.find_element(*page1.zaznacz_swoja_droge_do_pracy_btn()).is_enabled()
        except AssertionError as e:
            # Wypisywanie komunikatu błędu do logów
            print(f"AssertionError: Przycisk Zaznacz_swoją_drogę_do_pracy niedostępny")

        try:
            assert driver.find_element(*page1.zaznacz_swoje_3_ulubione_miejsca_w_poznaniu_btn()).is_enabled()
        except AssertionError as e:
            # Wypisywanie komunikatu błędu do logów
            print(f"AssertionError: Przycisk Zaznacz_3_ulubione_miejsca_w_Poznaniu niedostępny")

        driver.find_element(*page1.co_lubisz_robic_w_wolnym_czasie_1()).click()
        driver.find_element(*page1.co_lubisz_robic_w_wolnym_czasie_7()).click()
        assert driver.find_element(*page1.inna_odpowiedz_input()).is_enabled()
        driver.find_element(*page1.inna_odpowiedz_input()).send_keys("Odpowiedź")
        slider = driver.find_element(*page1.ocen_jakosc_drog_w_polsce_slider())
        driver.execute_script("arguments[0].scrollIntoView(true);", slider)
        actions = ActionChains(driver)
        actions.click_and_hold(slider).move_by_offset(100, 0).release().perform()
        driver.find_element(By.ID, "btn-navigation-nextPage").click()
        location = (By.XPATH, "//*[@id='root']/main/section/div/div/div[2]/div/main/div[2]/div/div/div/div[2]/div/h3")
        header_page2 = wait.until(EC.presence_of_element_located(location))
        text = header_page2.text
        assert "Jakie lody lubisz najbardziej?" in text
