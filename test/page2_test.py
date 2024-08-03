from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium import webdriver
from Ankieta_Dziwnych_Pytan.pages.page_2 import Page2
import time
from Ankieta_Dziwnych_Pytan.test.skip import skip_page2

@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.get("https://qa.thebitbybit.com/form/ankieta-dziwnych-pytan/2")
    assert  driver.title == ("Geoankieta")
    yield driver
    driver.quit()
class Test_Page2:
    def test_page2(self, driver):
        page2 = Page2(driver)
        wait = WebDriverWait(driver, 10)
        time.sleep(2)

        # Przeklikanie do strony page2
        skip_page2(driver)

        driver.find_element(*page2.czekolada_grycan_checkbox()).click()
        driver.find_element(*page2.czekolada_algida_chceckbox()).click()
        error_text = driver.find_element(*page2.error_text())
        assert error_text.is_displayed(), f"Komunikat: 'Kolumny powinny mieć miedzy 1 - 1 odpowiedzi' nie jest widoczny na stornie"
        time.sleep(2)
        driver.find_element(*page2.wanilia_algida_checkbox()).click()
        try:
            WebDriverWait(driver, 5).until(
                EC.invisibility_of_element_located(page2.error_text())
            )
        except TimeoutException:
            assert False, "Tekst powinien być niewidoczny po kliknięciu przycisku."
        driver.find_element(*page2.nie_jadlem_zielona_budka_checkbox()).click()
        driver.find_element(*page2.next_page_btn()).click()
        location = (By.XPATH,"//*[@id='root']/main/section/div/div/div[2]/div[2]/main/div[2]/div/div/div/div[2]/div[2]/h3/label")
        header_page3 = wait.until(EC.presence_of_element_located(location))
        text = header_page3.text
        assert "Napisz nam swój ulubiony wierszyk" in text