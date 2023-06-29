import pytest
from link_test_site import Links
from pages.home_page import HomePageClass
from locators.home_page_locators import HomePageLocatorsLinks as HPL



@pytest.mark.smoke
@pytest.mark.regression
def test_click_link_home_page(browser):
    link = Links.page_main
    page_home = HomePageClass(browser, link, 1)
    page_home.open()

    page_home.click_link(HPL.BATTON_NACHATb_BESPLATNO)
    page_home.click_link(HPL.LINK_GO_TO_BLOG)
    page_home.click_link(HPL.BATTON_POPROBOVATb)
    page_home.click_link(HPL.BATTON_POPROBOVATb_BESPLATNO)
    page_home.test_video_link(HPL.LINK_VIDEO_WORK)
    page_home.click_link(HPL.LINK_ONAS_BLOG)
    page_home.click_link(HPL.LINK_ONAS_TG)
    page_home.click_link(HPL.LINK_ONAS_VCRU)
    page_home.click_link(HPL.LINK_ONAS_VK)
    page_home.click_link(HPL.BATTON_VISUALISIROVATb_STRUCTURU)
    page_home.click_link(HPL.LINK_SITEMAPS_1)
    page_home.click_link(HPL.LINK_STRUCTURAaPP_1)
    page_home.click_link(HPL.LINK_PRINCIP_RABOTI_KRAULERA)
    page_home.click_link(HPL.LINK_BLANK_AGENT)
    page_home.click_link(HPL.LINK_BLANK_FRILANC)
    page_home.click_link(HPL.LINK_BLANK_CORPORAT)
    page_home.click_link(HPL.LINK_BLANK_PROMOsITE)
    page_home.click_link(HPL.LINK_BLANK_INTERNETsTOR)
    page_home.click_link(HPL.LINK_BLANK_OTHER)
    page_home.click_link(HPL.BATTON_SOZDATb_IZ_SHABLONA)
    page_home.click_link(HPL.BATTON_SOZDATb_S_NOLJA)
    page_home.test_video_link(HPL.LINK_VIDEO_SlISTA)
    page_home.test_button_swich()
    page_home.click_link_simpl_click(HPL.LINK_OSNOVAT_STRUCTURA)
    page_home.click_link(HPL.BATTON_NACHATb_PROBNII)
    page_home.click_link(HPL.BATTON_PODCLUCHITb_FREELANCER)
    page_home.click_link(HPL.BATTON_PODCLUCHITb_COMANDA)
    page_home.click_link(HPL.BATTON_PODCLUCHITb_COMPANIA)
    page_home.click_link(HPL.LINK_BLOG_1)
    page_home.click_link(HPL.LINK_CONFIDENC)
    page_home.click_link(HPL.LINK_HOW_WORK_KRAULER_HEAD)
    page_home.click_link(HPL.LINK_HOW_WORK_KRAULER_2)
    page_home.click_link(HPL.LINK_NIZ_BLOG)
    page_home.click_link(HPL.LINK_NIZ_CASE)
    page_home.click_link(HPL.LINK_NIZ_HOW_WORK_KRAULER)
    page_home.click_link(HPL.LINK_NIZ_TARIFI)
    page_home.click_link(HPL.LINK_POLZOVAT_SOGLAS)
    page_home.click_link(HPL.LINK_TARIFI_1)
    page_home.click_link(HPL.LINK_TG_GROUP)
    page_home.click_link(HPL.LINK_VK_GROUP)
    page_home.click_link(HPL.LINK_YOUTUBE_GROUP)
