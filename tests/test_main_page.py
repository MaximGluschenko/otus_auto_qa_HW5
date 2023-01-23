import allure
from locators import *
from page_objects.MainPage import MainPage


@allure.feature('Check page elements')
@allure.story('Main page')
@allure.title('Check main page elements')
def test_check_main_page_elements(browser, base_url):
    main_page = MainPage(browser)
    main_page.open(base_url)

    main_page.element(MP_TOP)
    main_page.element(MP_SEARCH)
    main_page.element(MP_MENU)
    main_page.element(MP_SLIDESHOW)
    main_page.element(MP_FOOTER)
    main_page.element(MP_ABOUT_AS_LINK_TEXT)
