
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

def skip_page3(driver):
    # Przeklikanie do strony page3
    driver.find_element(By.ID, "btn-landingPage-fillIn").click()
    driver.find_element(By.CSS_SELECTOR, 'div.overlay').click()
    driver.find_element(By.XPATH,
                        "//*[@id='root']/main/section/div/div/div[2]/div[2]/main/div[2]/div/div/div/div[4]/div[2]/div/div/label[2]/span[1]").click()

    wait = WebDriverWait(driver, 10)
    location = (By.ID, "btn-navigation-nextPage")
    element = wait.until(EC.presence_of_element_located(location))
    element.click()
    driver.find_element(By.XPATH,
                        "//*[@id='root']/main/section/div/div/div[2]/div/main/div[2]/div/div/div/div[2]/div/div[2]/table/tbody/tr[1]/td[1]/div/span/input").click()
    driver.find_element(By.XPATH,
                        "//*[@id='root']/main/section/div/div/div[2]/div/main/div[2]/div/div/div/div[2]/div/div[2]/table/tbody/tr[2]/td[2]/div/span/input").click()
    driver.find_element(By.XPATH,
                        "//*[@id='root']/main/section/div/div/div[2]/div/main/div[2]/div/div/div/div[2]/div/div[2]/table/tbody/tr[3]/td[3]/div/span/input").click()
    driver.find_element(By.ID, "btn-navigation-nextPage").click()
def skip_page2(driver):
    # Przeklikanie do strony page2
    driver.find_element(By.ID, "btn-landingPage-fillIn").click()
    driver.find_element(By.CSS_SELECTOR, 'div.overlay').click()
    driver.find_element(By.XPATH,
                        "//*[@id='root']/main/section/div/div/div[2]/div[2]/main/div[2]/div/div/div/div[4]/div[2]/div/div/label[2]/span[1]").click()
    wait = WebDriverWait(driver, 10)
    location = (By.ID, "btn-navigation-nextPage")
    element = wait.until(EC.presence_of_element_located(location))
    element.click()
def skip_page1(driver):
    # Przeklikanie do strony page1
    driver.find_element(By.ID, "btn-landingPage-fillIn").click()
    driver.find_element(By.CSS_SELECTOR, 'div.overlay').click()