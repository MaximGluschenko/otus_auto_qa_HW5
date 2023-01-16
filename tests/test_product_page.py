from locators import *
from page_objects.ProductPage import ProductPage
from conftest import USD_to_EUR_ratio, USD_to_GBP_ratio


def test_check_product_page_elements(browser, base_url):
    product_page = ProductPage(browser)
    product_page.open(base_url)

    product_page.element(PP_BUTTON_CART)
    product_page.element(PP_INPUT_QUANTITY)
    product_page.element(PP_TWEET_LINK_TEXT)
    product_page.element(PP_ADD_TO_WISH_LIST)
    product_page.element(PP_COMPARE_THIS_PRODUCT)


def test_switch_currency(browser, base_url):
    product_page = ProductPage(browser)
    product_page.open(base_url)

    product_page.switch_currency_to("USD")
    assert product_page.element(MP_DROPDOWN_SWITCH_CURRENCY).text == "$ Currency "
    USD_price = product_page.get_product_price("USD")

    product_page.switch_currency_to("EUR")
    assert product_page.element(MP_DROPDOWN_SWITCH_CURRENCY).text == "€ Currency "
    EUR_price = product_page.get_product_price("EUR")
    assert EUR_price == round((USD_price * USD_to_EUR_ratio), 2)

    product_page.switch_currency_to("GBP")
    assert product_page.element(MP_DROPDOWN_SWITCH_CURRENCY).text == "£ Currency "
    GBP_price = product_page.get_product_price("GBP")
    assert GBP_price == round((USD_price * USD_to_GBP_ratio), 2)
