import allure
from locators import *
from page_objects.CatalogPage import CatalogPage


@allure.feature('Check page elements')
@allure.story('Catalog page')
@allure.title('Check catalog page elements')
def test_check_catalog_page_elements(browser, base_url):
    catalog_page = CatalogPage(browser)
    catalog_page.open(base_url)

    catalog_page.element(CP_LIST_VIEW)
    catalog_page.element(CP_INPUT_SORT)
    catalog_page.element(CP_INPUT_LIMIT)
    catalog_page.element(CP_COMPARE_TOTAL)
    catalog_page.element(CP_LT_NB_LINK_TEXT)
