from pages.base_page import BasePageClass
from locators.home_page_locators import HomePageLocatorsLinks as HPL
from selenium.webdriver.common.by import By
import traceback
import re
import time
class HomePageClass(BasePageClass):

    def open(self):
        self.browser.get(self.url)

    def test_button_swich(self,):
        self.browser.find_element(*HPL.BATTON_GOD_MESJAC).click()
        element = self.browser.find_element(By.XPATH, '//*[@id="tariffs"]/div/div/div[1]/div[1]/div/div/div/span[2]')
        if 'tariff_type_selector_wrapper__checkbox__span active' in element.get_attribute('class'):
            print("BATTON_GOD_MESJAC работает!")
        else:
            print("BATTON_GOD_MESJAC не работает")

    def test_video_link(self, var):
        self.browser.find_element(*var).click()
        time.sleep(1)
        self.browser.switch_to.frame(self.browser.find_element(By.TAG_NAME, 'iframe'))
        element3 = self.browser.find_element(*HPL.IT_IS_VIDEO)
        stack = traceback.extract_stack()
        filename, lineno, function_name, code = stack[-2]
        vars_name = re.compile(r'\((.*?)\).*$').search(code).groups()[0]
        name_link = f'{vars_name=}'.split('.')[1]
        if 'ytp-impression-link' in element3.get_attribute('class'):
            print("Рабочая видео ссылка " + name_link)
        else:
            print("Не рабочая видео ссылка " + name_link)
        self.browser.switch_to.default_content()
        # close video windows
        self.browser.find_element(*HPL.LINK_VIDEO_CLOSE).click()