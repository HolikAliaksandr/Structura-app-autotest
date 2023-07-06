from selenium.webdriver.common.by import By
class ConstructorPageLocators:
    BUTTON_S_CHISTOGO_LISTA = (By.XPATH, '//*[@id="root"]/div/main/div[2]/div/div[1]/button[1]')
    FIELD_ELEMENT_IN_PROJECT = (By.CLASS_NAME,   'page_comments_btn ')
    BUTTON_ADD_ELEMENT_PLUS = (By.CLASS_NAME, 'plus')
    BUTTON_ADD_ELEMENT_PLUS2 = (By.NAME, 'Добавить страницу')
    FIELD_MY_PROJEKT = (By.XPATH, '//*[@id="root"]/div/main/div[2]/div/div[5]/div/div[1]/div[1]')
    BUTTON_ADD_COMMENT_TO_ELEMENT = (By.CLASS_NAME, 'page_comments_btn ')
    BUTTON_ADD_COMMENT_TO_ELEMENT2 = (By.CLASS_NAME, 'editInput')