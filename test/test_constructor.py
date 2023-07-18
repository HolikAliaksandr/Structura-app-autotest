import pytest
from selenium.common import TimeoutException
from selenium.webdriver.common import alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from link_test_site import Links
from locators.constructor_page_lockators import ConstructorPageLocators as CPL
from pages.constructor_page import ConstructorPageClass
import time


@pytest.mark.smoke
@pytest.mark.regression
def test_constructor_s_chistogo_lista_many_elements_horizont(browser):
    link = Links.page_login
    page_constructor = ConstructorPageClass(browser, link, 1)
    page_constructor.open()

    page_constructor.input_email('aliaksandr.holik@gmail.com')
    page_constructor.input_password('Test123456')
    page_constructor.click_voiti()

    page_constructor.click_element(CPL.BUTTON_S_CHISTOGO_LISTA)
    # page_constructor.click_element(CPL.FIELD_MY_PROJEKT)
    time.sleep(1)

    page_constructor.add_elements_titleH(0)
    # сколько еще добавить элементов к первому
    for i in range(9):
        page_constructor.muve_cursor_to_element(CPL.FIELD_ELEMENT_IN_PROJECT)
        page_constructor.click_element(CPL.BUTTON_ADD_ELEMENT_PLUS)
        page_constructor.add_elements_titleH(i+1)

    browser.save_screenshot('project_on_horizont.png')
    page_constructor.delete_this_project()
    time.sleep(1)

@pytest.mark.smoke
@pytest.mark.regression
def test_constructor_s_chistogo_lista_many_elements_vertical(browser):
    link = Links.page_login
    page_constructor = ConstructorPageClass(browser, link, 1)
    page_constructor.open()

    page_constructor.input_email('aliaksandr.holik@gmail.com')
    page_constructor.input_password('Test123456')
    page_constructor.click_voiti()

    page_constructor.click_element(CPL.BUTTON_S_CHISTOGO_LISTA)
    # page_constructor.click_element(CPL.FIELD_MY_PROJEKT)
    time.sleep(1)
    page_constructor.add_elements_titleV(0)
    for i in range(4):
        page_constructor.move_cursor_to_elements(CPL.BUTTON_ADD_COMMENT_TO_ELEMENT, i)
        page_constructor.click_elements(CPL.BUTTON_ADD_ELEMENT_PLUS, i)
        page_constructor.add_elements_titleV(i+1)

    browser.save_screenshot('project_on_vertical.png')
    page_constructor.delete_this_project()
    time.sleep(1)


@pytest.mark.smoke
@pytest.mark.regression
def test_constructor_in_self_element(browser):
    link = Links.page_login
    page_constructor = ConstructorPageClass(browser, link, 1)
    page_constructor.open()

    page_constructor.input_email('aliaksandr.holik@gmail.com')
    page_constructor.input_password('Test123456')
    page_constructor.click_voiti()

    # page_constructor.click_element(CPL.BUTTON_S_CHISTOGO_LISTA)
    page_constructor.click_element(CPL.FIELD_MY_PROJEKT)
    time.sleep(1)


    page_constructor.add_new_area_in_element(3)
    # time.sleep(2)
    # browser.save_screenshot('any_elements_in_project.png')
    # page_constructor.delete_this_project()

    time.sleep(2)


