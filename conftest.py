import pytest
from selenium import webdriver
import time


@pytest.fixture(autouse=True)
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

# @pytest.fixture(autouse=True)
# def browser():
#     browser = webdriver.Firefox()
#     yield browser
#     browser.quit()
