import os
from telnetlib import EC

import pytest
from selenium.common import TimeoutException
from selenium.webdriver.common import alert
from selenium.webdriver.support.wait import WebDriverWait

from link_test_site import Links
from pages.login_in_page import LoginPageClass
from locators.login_locators import LoginPageLocators as Log
import time



@pytest.mark.smoke
@pytest.mark.regression
def test_in_with_email(browser):
    link = Links.page_login
    page_login = LoginPageClass(browser, link, 1)
    page_login.open()

    time.sleep(1)

    page_login.input_email('aliaksandr.holik@gmail.com')
    page_login.click_voiti()
    time.sleep(1)
    browser.save_screenshot('no_passw.png')


    #alert_obj = driver.switch_to.alert
    # msg = alert_obj.text()
    # print(msg)
    # time.sleep(2)

    page_login.clear_email()
    page_login.input_password('Test123456')
    page_login.click_voiti()
    time.sleep(1)
    browser.save_screenshot('no_email.png')
    time.sleep(1)


    page_login.input_email('aliaksandr.holik@gmail.com')
    page_login.click_voiti()
    time.sleep(1)
    browser.save_screenshot('validation_in.png')
    # time.sleep(1)

