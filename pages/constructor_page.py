from selenium.webdriver import ActionChains

from pages.base_page import BasePageClass
from locators.login_locators import LoginPageLocators as L
from locators.constructor_page_lockators import ConstructorPageLocators as CPL
from selenium.webdriver.common.by import By
import traceback
import re
import time


class ConstructorPageClass(BasePageClass):
    def open(self):
        self.browser.get(self.url)

    def input_email(self, email):
        self.browser.find_element(*L.FIELD_EMAIL).send_keys(email)

    def input_password(self, passw):
        self.browser.find_element(*L.FIELD_PASSWORD).send_keys(passw)

    def click_voiti(self):
        x = self.browser.find_element(*L.BUTTON_VOITI)
        x.click()

    def click_element(self, var):
        x = self.browser.find_element(*var)
        x.click()

    def muve_cursor_to_element(self, loc):
        hoverable = self.browser.find_element(*loc)
        ActionChains(self.browser).scroll_to_element(hoverable)
        ActionChains(self.browser) \
        .move_to_element(hoverable) \
        .perform()

    def add_elements_titleH(self, x):
        lisTs = self.browser.find_elements(By.CLASS_NAME, 'editInput')[x]
        ActionChains(self.browser) \
            .move_to_element_with_offset(lisTs, 30, 0) \
            .perform()

        lisTs.click()
        y = str(x + 1)
        lisTs.send_keys(' ' + y)
        clickable = self.browser.find_element(By.TAG_NAME, 'textarea')
        clickable.click()

    def muve_cursor_to_elements(self, loc, x):
        hoverable = self.browser.find_elements(*loc)[x]
        ActionChains(self.browser).scroll_to_element(hoverable)
        ActionChains(self.browser) \
            .move_to_element(hoverable) \
            .perform()


    def click_elements(self, var, z):
        x = self.browser.find_elements(*var)[z]
        x.click()
        pozic_1 = self.browser.find_elements(*var)[z]
        pozic_2 = self.browser.find_elements(*var)[z-1]
        action = ActionChains(self.browser)
        action.click_and_hold(pozic_1).pause(1).move_to_element(pozic_2).release(pozic_1).perform()


    def add_elements_titleV(self, x):
        lisTs = self.browser.find_elements(By.CLASS_NAME, 'editInput')[x]
        lisTs.click()
        y = str(x + 1)
        lisTs.send_keys(' ' + y)
        clickable = self.browser.find_element(By.TAG_NAME, 'textarea')
        clickable.click()

    def delete_this_project(self):
        button_brot = self.browser.find_elements(By.CLASS_NAME, 'item')[2]
        button_brot.click()
        delete = self.browser.find_element(By.XPATH, "//span[text()='Удалить проект']")
        delete.click()

