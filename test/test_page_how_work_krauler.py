import pytest
from link_test_site import Links as L
from pages.how_work_krauler import HowWorkKraulerClass
from locators.how_work_krauler_page_locators import HowWorkKrauPageLocators as HWK
import time


@pytest.mark.smoke
@pytest.mark.regression
def test_work_Links_how_work_krauler(browser):
    link = L.page_how_work_krauler
    page_how = HowWorkKraulerClass(browser, link)
    page_how.open()

    page_how.click_link(HWK.BATTON_NACHATb_BESPLATNO, L.page_reg)
    page_how.click_link(HWK.BATTON_VISUALISIROVATb_STRUCTURU, L.page_reg)
    page_how.click_link(HWK.LINK_SITEMAPS_1, 'https://app.structura.app/neweditor/9933a5b5-f3d6-3312-a56b-79334ac2364a?utm_source=example')
    page_how.click_link(HWK.LINK_STRUCTURA_APP_1, 'https://app.structura.app/editor/cf870d1a-8388-89a2-2ffb-5cebf003396a?utm_source=example')
    page_how.click_link(HWK.LINK_SITEMAPS_2, 'https://app.structura.app/neweditor/9933a5b5-f3d6-3312-a56b-79334ac2364a?utm_source=example')
    page_how.click_link(HWK.LINK_STRUCTURA_APP_2, 'https://app.structura.app/editor/cf870d1a-8388-89a2-2ffb-5cebf003396a')
    page_how.scroll_down()
    page_how.click_link(HWK.LINK_TARIFI_1, L.link_tarifs)
    time.sleep(1)
    page_how.scroll_down()
    page_how.click_link_simpl_click(HWK.LINK_HOW_WORK_KRAULER_HEADER)
    page_how.scroll_down()
    page_how.click_link(HWK.LINK_BLOG_HEADER, L.page_blog)
    page_how.scroll_down()
    time.sleep(1)
    page_how.click_link(HWK.LINK_CASE_1, 'https://structura.app/blog?slug=%D0%9A%D0%B5%D0%B9%D1%81%D1%8B')
    time.sleep(1)
    page_how.click_link(HWK.LINK_POLITIKA_KOFIDENC, L.link_politica_confid)
    page_how.click_link(HWK.LINK_USER_OFERTA, L.link_polsovat_soglas)
    page_how.scroll_down()
    page_how.click_link_simpl_click(HWK.LINK_HOW_WORK_KRAULER_2)
    page_how.click_link(HWK.LINK_TARIFI_2, L.link_tarifs)
    time.sleep(1)
    page_how.click_link(HWK.LINK_BLOG_2, L.page_blog)
    time.sleep(1)
    page_how.click_link(HWK.LINK_TELEGRAMM, L.page_tg_bot)
    page_how.click_link(HWK.LINK_YOUTUBE, L.page_youtub_blog)
    page_how.click_link(HWK.LINK_VK, L.page_vk_blog)
