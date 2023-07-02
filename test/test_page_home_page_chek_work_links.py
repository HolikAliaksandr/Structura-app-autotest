import pytest
from link_test_site import Links as L
from pages.home_page import HomePageClass
from locators.home_page_locators import HomePageLocatorsLinks as HPL
import time



@pytest.mark.smoke
@pytest.mark.regression
def test_click_link_home_page(browser):
    link = L.page_main
    page_home = HomePageClass(browser, link, 1)
    page_home.open()

    page_home.click_video_link(HPL.LINK_VIDEO_WORK)
    page_home.click_link(HPL.BATTON_NACHATb_BESPLATNO, L.page_reg)
    time.sleep(1)
    page_home.click_link(HPL.LINK_GO_TO_BLOG, L.page_blog)
    time.sleep(3)
    page_home.click_link(HPL.BATTON_POPROBOVATb, L.page_reg)
    page_home.click_link(HPL.BATTON_POPROBOVATb_BESPLATNO, L.page_reg)
    time.sleep(2)
    page_home.click_link(HPL.LINK_ONAS_BLOG, L.page_blog)
    page_home.click_link(HPL.LINK_ONAS_TG, L.page_tg_bot)
    page_home.click_link(HPL.LINK_ONAS_VCRU, L.page_vc_ru)
    page_home.click_link(HPL.LINK_ONAS_VK, L.page_vk_blog)
    page_home.click_link(HPL.BATTON_VISUALISIROVATb_STRUCTURU, 'https://app.structura.app/registration?site_draft_query=')
    page_home.click_link(HPL.LINK_SITEMAPS_1, 'https://app.structura.app/neweditor/9933a5b5-f3d6-3312-a56b-79334ac2364a?utm_source=example')
    page_home.click_link(HPL.LINK_STRUCTURAaPP_1, 'https://app.structura.app/editor/cf870d1a-8388-89a2-2ffb-5cebf003396a')
    page_home.click_link(HPL.LINK_PRINCIP_RABOTI_KRAULERA, L.page_how_work_krauler)
    page_home.click_link(HPL.LINK_BLANK_AGENT, 'https://app.structura.app/editor/9f1cc020-b2e3-8155-ed96-d009e03ef148')
    page_home.click_link(HPL.LINK_BLANK_FRILANC, 'https://app.structura.app/editor/f18882ee-8cfa-59d6-a7c4-b08ab3b396f7')
    page_home.click_link(HPL.LINK_BLANK_CORPORAT, 'https://app.structura.app/editor/f1499c78-fed8-6b6d-979b-a6d045a2857f')
    page_home.click_link(HPL.LINK_BLANK_PROMOsITE, 'https://app.structura.app/editor/59bf2a03-2e52-7fe2-827b-812d0ea36bba')
    page_home.click_link(HPL.LINK_BLANK_INTERNETsTOR, 'https://app.structura.app/editor/a4330cfd-56cf-87f9-af48-93a7036355c6')
    page_home.click_link(HPL.LINK_BLANK_OTHER, L.page_login)
    page_home.click_link(HPL.BATTON_SOZDATb_IZ_SHABLONA, L.page_reg)
    page_home.click_link(HPL.BATTON_SOZDATb_S_NOLJA, L.page_reg)
    page_home.click_video_link(HPL.LINK_VIDEO_SlISTA)
    page_home.click_button_swich()
    page_home.click_link_simpl_click(HPL.LINK_OSNOVAT_STRUCTURA)
    page_home.click_link(HPL.BATTON_NACHATb_PROBNII, L.page_reg)
    page_home.click_link(HPL.BATTON_PODCLUCHITb_FREELANCER, L.page_reg)
    page_home.click_link(HPL.BATTON_PODCLUCHITb_COMANDA, L.page_reg)
    page_home.click_link(HPL.BATTON_PODCLUCHITb_COMPANIA, L.page_reg)
    time.sleep(2)
    page_home.click_link(HPL.LINK_BLOG_HEADER, L.page_blog)
    time.sleep(3)
    page_home.click_link(HPL.LINK_CONFIDENC, L. link_politica_confid)
    page_home.click_link(HPL.LINK_HOW_WORK_KRAULER_HEAD, L.page_how_work_krauler)
    page_home.click_link(HPL.LINK_HOW_WORK_KRAULER_2, L.page_how_work_krauler)
    time.sleep(1)
    page_home.click_link(HPL.LINK_NIZ_BLOG, L.page_blog)
    time.sleep(1)
    page_home.click_link(HPL.LINK_NIZ_CASE, 'https://structura.app/blog?slug=%D0%9A%D0%B5%D0%B9%D1%81%D1%8B')
    time.sleep(1)
    page_home.click_link(HPL.LINK_NIZ_HOW_WORK_KRAULER, L.page_how_work_krauler)
    time.sleep(1)
    page_home.click_link(HPL.LINK_NIZ_TARIFI, L.link_tarifs)
    page_home.click_link(HPL.LINK_POLZOVAT_SOGLAS, L.link_polsovat_soglas)
    page_home.click_link(HPL.LINK_TARIFI_1, L.link_tarifs)
    page_home.click_link(HPL.LINK_TG_GROUP, L.page_tg_bot)
    page_home.click_link(HPL.LINK_VK_GROUP, L.page_vk_blog)
    page_home.click_link(HPL.LINK_YOUTUBE_GROUP, L.page_youtub_blog)
