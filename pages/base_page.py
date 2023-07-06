from selenium.webdriver.common.by import By
import requests
import time
import re
import traceback
from selenium.webdriver.support import wait

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BasePageClass:
    def __init__(self, browser, url, timeout=4):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        # self.browser.set_window_size(1200, 800)


    def how_work_outer_link(self, var):
        url = self.browser.find_element(*var).get_attribute('href')
        result = requests.get(url, timeout=3)
        stack = traceback.extract_stack()
        filename, lineno, function_name, code = stack[-2]
        vars_name = re.compile(r'\((.*?)\).*$').search(code).groups()[0]
        name_link = f'{vars_name=}'.split('.')[1]
        if result.status_code != 200:
            print(name_link + "=>", url, result.status_code)
        elif result.status_code == 200:
            print(name_link + "работает!")


    def click_link(self, var, need_url):
        x = self.browser.find_element(*var)
        url = x.get_attribute('href')
        x.click()
        # time.sleep(1)
        self.browser.set_page_load_timeout(5)


        assert url == need_url, 'Не открывается нужная ссылка'
        time.sleep(1)
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

    def scroll_down(self):
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def click_link_one(self, var):
        x = self.browser.find_element(*var)
        x.click()
        time.sleep(2)
        self.browser.back()

    def click_link_two(self, var):
        x = self.browser.find_element(*var)
        x.click()
        time.sleep(2)
        self.browser.switch_to.window(self.browser.window_handles[1])
        self.browser.close()
        self.browser.switch_to.window(self.browser.window_handles[0])

    def click_link_tri(self, var):
        x = self.browser.find_element(*var)
        x.click()
        time.sleep(2)
        self.browser.switch_to.window(self.browser.window_handles[1])
        self.browser.close()
        self.browser.switch_to.window(self.browser.window_handles[0])
        self.browser.switch_to.window(self.browser.window_handles[1])
        self.browser.close()
        self.browser.switch_to.window(self.browser.window_handles[0])


    def click_link_simpl_click(self, var): #метод для ссылок, которые возвращают на текущую страницу
        x = self.browser.find_element(*var)
        x.click()
        time.sleep(1)
        url = self.browser.find_element(*var).get_attribute('href')
        assert url == self.url, 'Странно, но эта ссылка уже не может открыться снова'
        stack = traceback.extract_stack()
        filename, lineno, function_name, code = stack[-2]
        vars_name = re.compile(r'\((.*?)\).*$').search(code).groups()[0]
        name_link = f'{vars_name=}'.split('.')[1]
        print(name_link + "   работает!")

    def get_link(self, lokator):
        x = self.browser.find_element(*lokator)
        url = x.get_attribute('href')
        if url is None:
            url = self.browser.current_url
        return url
