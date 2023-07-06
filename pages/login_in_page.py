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
        self.browser.maximize_window()

    def input_email(self, email):
        self.browser.find_element(*L.FIELD_EMAIL).send_keys(email)

    def input_password(self, passw):
        self.browser.find_element(*L.FIELD_PASSWORD).send_keys(passw)

    def click_voiti(self):
        x = self.browser.find_element(*L.BUTTON_VOITI)
        x.click()

    def in_with_google(self):
        x = self.browser.find_element(*L.IN_WITH_GOOGLE)
        x.click()

    def clear_email(self):
        self.browser.find_element(*L.FIELD_EMAIL).send_keys(Keys.CONTROL + "a")
        self.browser.find_element(*L.FIELD_EMAIL).send_keys(Keys.DELETE)

