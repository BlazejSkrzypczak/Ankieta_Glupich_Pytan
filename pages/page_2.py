from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Page2:
    def __init__(self, driver):
        self.driver = driver
    def czekolada_grycan_checkbox(self):
        return (By.XPATH, "//*[@id='root']/main/section/div/div/div[2]/div/main/div[2]/div/div/div/div[2]/div/div[2]/table/tbody/tr[1]/td[1]/div/span/input")
    def czekolada_algida_chceckbox(self):
        return (By.XPATH, "//*[@id='root']/main/section/div/div/div[2]/div/main/div[2]/div/div/div/div[2]/div/div[2]/table/tbody/tr[2]/td[1]/div/span/input")
    def wanilia_algida_checkbox(self):
        return (By.XPATH,"//*[@id='root']/main/section/div/div/div[2]/div/main/div[2]/div/div/div/div[2]/div/div[2]/table/tbody/tr[2]/td[2]/div/span/input")
    def nie_jadlem_zielona_budka_checkbox(self):
        return (By.XPATH, "//*[@id='root']/main/section/div/div/div[2]/div/main/div[2]/div/div/div/div[2]/div/div[2]/table/tbody/tr[3]/td[5]/div/span/input")
    def error_text(self):
        return (By.CSS_SELECTOR, "p.error")
    def next_page_btn(self):
        return (By.ID,"btn-navigation-nextPage")
