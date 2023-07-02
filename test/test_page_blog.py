import pytest
from link_test_site import Links as L
from pages.blog_page import BlogPageClass
from locators.blog_page_locators import BlogPageLocatorsLinks as B
import time


@pytest.mark.smoke
@pytest.mark.regression
def test_click_link_home_page(browser):
    link = L.page_blog
    page_blog = BlogPageClass(browser, link, 1)
    page_blog.open()

    page_blog.click_link(B.BATTON_NACHATb_BESPLATNO_HEADER, L.page_reg)
    page_blog.scroll_down()
    page_blog.click_link(B.LINK_HOW_WORK_KRAULER_HEADER, L.page_how_work_krauler)
    time.sleep(2)
    page_blog.scroll_down()
    page_blog.click_link(B.LINK_TARIFI_HEADER, L.link_tarifs)
    time.sleep(2)
    page_blog.scroll_down()
    page_blog.click_link_simpl_click(B.LINK_BLOG_HEADER)

    page_blog.click_link(B.LINK_SOOBSHTESTVO, L.page_tg_bot)
    page_blog.click_link(B.LINK_KANAL, L.page_youtub_blog)

    page_blog.click_link_simpl_click_filtr(B.LINK_SELECT_CASE, 'https://structura.app/blog?slug=%D0%9A%D0%B5%D0%B9%D1%81%D1%8B')

    page_blog.click_link_read_blog(B.LINK_INNERinfo_1_PICT, 'https://structura.app/blog/besplatnye-shablony-saytov')
    page_blog.click_link_read_blog(B.LINK_INNERinfo_1_CHITATb_DALEE, 'https://structura.app/blog/besplatnye-shablony-saytov')
    page_blog.click_link_read_blog(B.LINK_INNERinfo_2_PICT, 'https://structura.app/blog/gramotnaya-proraboka-struktury-saita-pomogla')
    page_blog.click_link_read_blog(B.LINK_INNERinfo_2_CHITATb_DALEE, 'https://structura.app/blog/gramotnaya-proraboka-struktury-saita-pomogla')
    page_blog.click_link_read_blog(B.LINK_INNERinfo_3_PICT, 'https://structura.app/blog/keys_uvelichenie_konversii_cherez_issledovanie_auditorii')
    page_blog.click_link_read_blog(B.LINK_INNERinfo_3_CHITATb_DALEE, 'https://structura.app/blog/keys_uvelichenie_konversii_cherez_issledovanie_auditorii')

    page_blog.click_link_simpl_click_filtr(B.LINK_SELECT_STATII, 'https://structura.app/blog?slug=%D0%A1%D1%82%D0%B0%D1%82%D1%8C%D0%B8')

    page_blog.click_link_read_blog(B.LINK_INNERinfo_1_PICT,'https://structura.app/blog/chto-takoe-prototype-saita-zachem-nuzhen-i-kak-sozdat')
    page_blog.click_link_read_blog(B.LINK_INNERinfo_1_CHITATb_DALEE, 'https://structura.app/blog/chto-takoe-prototype-saita-zachem-nuzhen-i-kak-sozdat')
    page_blog.click_link_read_blog(B.LINK_INNERinfo_2_PICT, 'https://structura.app/blog/podborka-sovetov-pri-razrabotke-saita')
    page_blog.click_link_read_blog(B.LINK_INNERinfo_2_CHITATb_DALEE, 'https://structura.app/blog/podborka-sovetov-pri-razrabotke-saita')
    page_blog.click_link_read_blog(B.LINK_INNERinfo_3_PICT, 'https://structura.app/blog/intervue-dlya-kanala-reestr-russkogo-po')
    page_blog.click_link_read_blog(B.LINK_INNERinfo_3_CHITATb_DALEE, 'https://structura.app/blog/intervue-dlya-kanala-reestr-russkogo-po')

    page_blog.click_link_simpl_click_filtr(B.LINK_SELECT_VSE, L.page_blog)

    page_blog.click_link_read_blog(B.LINK_INNERinfo_1_PICT, 'https://structura.app/blog/chto-takoe-prototype-saita-zachem-nuzhen-i-kak-sozdat')
    page_blog.click_link_read_blog(B.LINK_INNERinfo_1_CHITATb_DALEE, 'https://structura.app/blog/chto-takoe-prototype-saita-zachem-nuzhen-i-kak-sozdat')
    page_blog.click_link_read_blog(B.LINK_INNERinfo_2_PICT, 'https://structura.app/blog/besplatnye-shablony-saytov')
    page_blog.click_link_read_blog(B.LINK_INNERinfo_2_CHITATb_DALEE, 'https://structura.app/blog/besplatnye-shablony-saytov')
    page_blog.click_link_read_blog(B.LINK_INNERinfo_3_PICT, 'https://structura.app/blog/podborka-sovetov-pri-razrabotke-saita')
    page_blog.click_link_read_blog(B.LINK_INNERinfo_3_CHITATb_DALEE, 'https://structura.app/blog/podborka-sovetov-pri-razrabotke-saita')
    time.sleep(1)
    page_blog.click_link(B.LINK_TARIFI_NIZ, L.link_tarifs)
    time.sleep(1)
    page_blog.click_link(B.LINK_PRINZIP_RABOTI_KRAULERA_NIZ, L.page_how_work_krauler)
    time.sleep(1)
    page_blog.click_link_simpl_click(B.LINK_BLOG_NIZ)
    time.sleep(2)
    page_blog.click_link(B.LINK_CONFIDENC, L.link_politica_confid)
    page_blog.click_link(B.LINK_POLZOVAT_SOGLAS, L.link_polsovat_soglas)