from locators import *
from page_objects.MainPage import MainPage


class ProductPage(MainPage):
    endpoint = None

    def __init__(self, browser):
        self.browser = browser

    def get_product_price(self, currency):

        self.switch_currency_to(currency)

        if currency == "USD":
            USD_price = float((self.element(PP_PRODUCT_PRICE).text).replace("$", ""))
            return USD_price
        elif currency == "EUR":
            EUR_price = float((self.element(PP_PRODUCT_PRICE).text).replace("€", ""))
            return EUR_price
        elif currency == "GBP":
            GBP_price = float((self.element(PP_PRODUCT_PRICE).text).replace("£", ""))
            return GBP_price
