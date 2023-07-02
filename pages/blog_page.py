from pages.base_page import BasePageClass
from locators.home_page_locators import HomePageLocatorsLinks as HPL
from selenium.webdriver.common.by import By
import traceback
import re
import time


class BlogPageClass(BasePageClass):
    def open(self):
        self.browser.get(self.url)

    def click_link_simpl_click_filtr(self, var, test):
        self.browser.find_element(*var).click()
        time.sleep(1)
        url = self.browser.current_url
        assert url == test, "Фильтр не рабочий!"
        stack = traceback.extract_stack()
        filename, lineno, function_name, code = stack[-2]
        vars_name = re.compile(r'\((.*?)\).*$').search(code).groups()[0]
        name_link = f'{vars_name=}'.split('.')[1]
        print(name_link + " работает!")

    def click_link_read_blog(self, var, need_url):
        x = self.browser.find_element(*var)
        x.click()
        time.sleep(2)
        url = self.browser.current_url
        assert url == need_url, 'Не открывается нужная сcылка'

        stack = traceback.extract_stack()
        filename, lineno, function_name, code = stack[-2]
        vars_name = re.compile(r'\((.*?)\).*$').search(code).groups()[0]
        name_link = f'{vars_name=}'.split('.')[1]
        print(name_link + " работает!")

        if(len(self.browser.window_handles)==2):
            self.browser.switch_to.window(self.browser.window_handles[1])
            self.browser.close()
            self.browser.switch_to.window(self.browser.window_handles[0])
            time.sleep(1)
        elif(len(self.browser.window_handles)==3):
            self.browser.switch_to.window(self.browser.window_handles[1])
            self.browser.close()
            self.browser.switch_to.window(self.browser.window_handles[0])
            self.browser.switch_to.window(self.browser.window_handles[1])
            self.browser.close()
            self.browser.switch_to.window(self.browser.window_handles[0])
        else:
            self.browser.back()
        time.sleep(5)
