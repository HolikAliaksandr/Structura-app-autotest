from telnetlib import EC

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePageClass
from locators.login_locators import LoginPageLocators as L
from selenium.webdriver.common.by import By
import traceback
import re
import time

class LoginPageClass(BasePageClass):
    def open(self):
        self.browser.get(self.url)
        # self.browser.maximize_window()

    def input_email(self, email):
        self.browser.find_element(*L.FIELD_EMAIL).send_keys(email)

    def input_password(self, passw):
        self.browser.find_element(*L.FIELD_PASSWORD).send_keys(passw)

    def click_voiti(self):
        x = self.browser.find_element(*L.BUTTON_VOITI)
        x.click()
        contr_login = self.browser.find_element(By.CLASS_NAME, 'new_feedback_caption')
        assert contr_login.is_displayed()


    def in_with_google(self):
        x = self.browser.find_element(*L.IN_WITH_GOOGLE)
        x.click()

    def clear_email(self):
        self.browser.find_element(*L.FIELD_EMAIL).send_keys(Keys.CONTROL + "a")
        self.browser.find_element(*L.FIELD_EMAIL).send_keys(Keys.DELETE)

    def click_profile(self):
        but = self.browser.find_element(*L.LINK_PROFILL)
        but.click()
        contr_profile = self.browser.find_elements(By.CLASS_NAME, 'MuiTouchRipple-root')[0]
        assert contr_profile.is_displayed()

    def click_button(self, lokator):
        self.browser.find_element(*lokator).click()


