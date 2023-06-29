import pytest
from link_test_site import Links
from pages.how_work_krauler import HowWorkKraulerClass
from locators.how_work_krauler_page_locators import HowWorkKrauPageLocators as HWK
import time


@pytest.mark.smoke
@pytest.mark.regression
def test_work_Links_how_work_krauler(browser):
    link = Links.page_how_work_krauler
    page_how = HowWorkKraulerClass(browser, link)
    page_how.open()

    page_how.click_link(HWK.BATTON_NACHATb_BESPLATNO)
    page_how.click_link(HWK.BATTON_NACHATb_BESPLATNO)
    page_how.click_link(HWK.BATTON_VISUALISIROVATb_STRUCTURU)
    page_how.click_link(HWK.LINK_SITEMAPS_1)
    page_how.click_link(HWK.LINK_STRUCTURA_APP_1)
    page_how.click_link(HWK.LINK_TARIFI_1)
    page_how.click_link(HWK.LINK_SITEMAPS_2)
    page_how.click_link(HWK.LINK_STRUCTURA_APP_2)
    page_how.click_link(HWK.LINK_TARIFI_1)
    page_how.scroll_down()
    page_how.click_link_simpl_click(HWK.LINK_HOW_WORK_KRAULER_1)
    page_how.scroll_down()
    page_how.click_link(HWK.LINK_BLOG_1)
    page_how.click_link(HWK.LINK_CASE_1)
    page_how.click_link(HWK.LINK_POLITIKA_KOFIDENC)
    page_how.click_link(HWK.LINK_USER_OFERTA)
    page_how.scroll_down()
    page_how.click_link_simpl_click(HWK.LINK_HOW_WORK_KRAULER_2)
    page_how.click_link(HWK.LINK_TARIFI_2)
    page_how.click_link(HWK.LINK_BLOG_2)
    page_how.click_link(HWK.LINK_TELEGRAMM)
    page_how.click_link(HWK.LINK_YOUTUBE)
    page_how.click_link(HWK.LINK_VK)
