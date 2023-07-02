from selenium.webdriver import ActionChains
from pages.base_page import BasePageClass
from locators.home_page_locators import HomePageLocatorsLinks as HPL
from selenium.webdriver.common.by import By
import traceback
import re
import time
class HomePageClass(BasePageClass):

    def open(self):
        self.browser.get(self.url)

    def click_button_swich(self):
        x = self.browser.find_element(*HPL.BATTON_GOD_MESJAC)
        ActionChains(self.browser).scroll_to_element(x)
        x.click()
        clas_status = self.browser.find_element(By.XPATH, '//*[@id="tariffs"]/div/div/div[1]/div[1]/div/div/div/span[2]')
        assert clas_status.get_attribute('class') == "tariff_type_selector_wrapper__checkbox__span active ", "BUTTON_GOD_MESJAC не работает"

    def click_video_link(self, var):
        self.browser.find_element(*var).click()
        time.sleep(2)
        self.browser.switch_to.frame(self.browser.find_element(By.TAG_NAME, 'iframe'))
        element_youtube = self.browser.find_element(*HPL.IT_IS_VIDEO)
        assert element_youtube.get_attribute('class') == 'ytp-impression-link', 'Нету нужного видеофайла!'

        stack = traceback.extract_stack()
        filename, lineno, function_name, code = stack[-2]
        vars_name = re.compile(r'\((.*?)\).*$').search(code).groups()[0]
        name_link = f'{vars_name=}'.split('.')[1]
        print("Рабочая видео ссылка " + name_link)
        self.browser.switch_to.default_content()
        # close video windows
        self.browser.find_element(*HPL.LINK_VIDEO_CLOSE).click()