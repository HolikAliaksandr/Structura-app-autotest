from selenium.webdriver.common.by import By
class LoginPageLocators:
    FIELD_EMAIL = (By.XPATH, '//*[@id="root"]/div/main/div[2]/div/div/div/form/div[1]/div/input')
    FIELD_PASSWORD = (By.XPATH, '//*[@id="root"]/div/main/div[2]/div/div/div/form/div[2]/div/div/input')
    IN_WITH_GOOGLE = (By.CLASS_NAME, 'googlesvgbg')
    BUTTON_VOITI = (By.XPATH, '//*[@id="root"]/div/main/div[2]/div/div/div/form/div[3]/button')
    BUTTON_3_TOCHKI = (By.XPATH, '//*[@id="root"]/div/main/div[1]/div/div[2]/div[2]')
    LINK_PROFILL = (By.XPATH, '//*[@id="root"]/div/main/div[1]/div/div[2]/div[2]/div[2]/div[2]')
    BUTTON_LOG_OUT_OF_PROFILE = (By.XPATH, '//*[@id="root"]/div/main/div[2]/div/div/div[3]/button')