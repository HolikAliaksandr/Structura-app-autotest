from pages.base_page import BasePageClass
from locators.home_page_locators import HomePageLocatorsLinks as HPL
from selenium.webdriver.common.by import By
import traceback
import re
import time


class BlogPageClass(BasePageClass):
    def open(self):
        self.browser.get(self.url)
