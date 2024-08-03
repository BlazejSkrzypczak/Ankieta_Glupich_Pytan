from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Page1:
    def __init__(self, driver):
        self.driver = driver
    def witaj_w_naszej_testowej_ankiecie_paragraph(self):
        return (By.CSS_SELECTOR, "div.paragraph")
    def jak_masz_na_imie_input(self):
        return (By.ID, "Jak masz na imię?")
    def jaka_jest_twoja_plec_checkbox(self, input):
        if input.lower() == 'k':
            return (By.XPATH, "//*[@id='root']/main/section/div/div/div[2]/div[2]/main/div[2]/div/div/div/div[4]/div[2]/div/div/label[1]/span[1]")
        if input.lower() == 'm':
            return (By.XPATH, "//*[@id='root']/main/section/div/div/div[2]/div[2]/main/div[2]/div/div/div/div[4]/div[2]/div/div/label[2]/span[1]")
    def zaznacz_swoja_droge_do_pracy_btn(self):
        return (By.XPATH, "//*[@id='root']/main/section/div/div/div[2]/div[2]/main/div[2]/div/div/div/div[5]/div/button")
    def zaznacz_swoje_3_ulubione_miejsca_w_poznaniu_btn(self):
        return (By.XPATH, "//*[@id='root']/main/section/div/div/div[2]/div[2]/main/div[2]/div/div/div/div[6]/div/button")
    def co_lubisz_robic_w_wolnym_czasie_1(self):
        return (By.XPATH, "//*[@id='root']/main/section/div/div/div[2]/div[2]/main/div[2]/div/div/div/div[7]/div/div/div[1]/label[1]/span[1]/input")
    def co_lubisz_robic_w_wolnym_czasie_7(self):
        return (By.XPATH, "//*[@id='root']/main/section/div/div/div[2]/div[2]/main/div[2]/div/div/div/div[7]/div/div/div[1]/label[7]/span[1]/input")
    def inna_odpowiedz_input(self):
        return (By.ID, "user-opinion-576c6c9b-eec0-491a-9be4-fa1dc9b20dbc")
    def ocen_jakosc_drog_w_polsce_slider(self):
        return (By.CSS_SELECTOR, '.MuiSlider-thumb.MuiSlider-thumbSizeMedium.MuiSlider-thumbColorPrimary.MuiSlider-thumb.MuiSlider-thumbSizeMedium.MuiSlider-thumbColorPrimary.css-3xswkt')
    def next_page_btn(self):
        return (By.ID, "btn-navigation-nextPage")
