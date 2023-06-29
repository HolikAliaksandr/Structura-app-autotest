import pytest
from link_test_site import Links
from pages.blog_page import BlogPageClass
from locators.blog_page_locators import BlogPageLocatorsLinks as B



@pytest.mark.smoke
@pytest.mark.regression
def test_click_link_home_page(browser):
    link = Links.page_blog
    page_blog = BlogPageClass(browser, link, 1)
    page_blog.open()


    page_blog.click_link(B.BATTON_NACHATb_BESPLATNO_HEADER)
    page_blog.scroll_down()
    page_blog.click_link(B.LINK_HOW_WORK_KRAULER_HEADER)
    page_blog.scroll_down()
    page_blog.click_link(B.LINK_TARIFI_HEADER)
    page_blog.scroll_down()
    page_blog.click_link_simpl_click(B.LINK_BLOG_HEADER)
    page_blog.click_link(B.LINK_SOOBSHTESTVO)
    page_blog.click_link(B.LINK_KANAL)

    page_blog.click_link_simpl_click(B.LINK_SELECT_CASE)

    page_blog.click_link(B.LINK_INNERinfo_1_PICT)
    page_blog.click_link(B.LINK_INNERinfo_1_CHITATb_DALEE)
    page_blog.click_link(B.LINK_INNERinfo_2_PICT)
    page_blog.click_link(B.LINK_INNERinfo_2_CHITATb_DALEE)
    page_blog.click_link(B.LINK_INNERinfo_3_PICT)
    page_blog.click_link(B.LINK_INNERinfo_3_CHITATb_DALEE)

    page_blog.click_link_simpl_click(B.LINK_SELECT_STATII)

    page_blog.click_link(B.LINK_INNERinfo_1_PICT)
    page_blog.click_link(B.LINK_INNERinfo_1_CHITATb_DALEE)
    page_blog.click_link(B.LINK_INNERinfo_2_PICT)
    page_blog.click_link(B.LINK_INNERinfo_2_CHITATb_DALEE)
    page_blog.click_link(B.LINK_INNERinfo_3_PICT)
    page_blog.click_link(B.LINK_INNERinfo_3_CHITATb_DALEE)

    page_blog.click_link_simpl_click(B.LINK_SELECT_VSE)

    page_blog.click_link(B.LINK_INNERinfo_1_PICT)
    page_blog.click_link(B.LINK_INNERinfo_1_CHITATb_DALEE)
    page_blog.click_link(B.LINK_INNERinfo_2_PICT)
    page_blog.click_link(B.LINK_INNERinfo_2_CHITATb_DALEE)
    page_blog.click_link(B.LINK_INNERinfo_3_PICT)
    page_blog.click_link(B.LINK_INNERinfo_3_CHITATb_DALEE)

    page_blog.click_link(B.LINK_TARIFI_NIZ)
    page_blog.click_link(B.LINK_PRINZIP_RABOTI_KRAULERA_NIZ)
    page_blog.click_link_simpl_click(B.LINK_BLOG_NIZ)
    page_blog.click_link(B.LINK_CONFIDENC)
    page_blog.click_link(B.LINK_POLZOVAT_SOGLAS)