from locators import *
from page_objects.BasePage import BasePage


class MainPage(BasePage):
    endpoint = "/index.php?route=common/home"

    def __init__(self, browser):
        self.browser = browser

    def switch_currency_to(self, currency):

        self.element(MP_DROPDOWN_SWITCH_CURRENCY).click()

        if currency == "USD":
            self.element(MP_SWITCH_CURRENCY_USD).click()

        elif currency == "EUR":
            self.element(MP_SWITCH_CURRENCY_EUR).click()

        elif currency == "GBP":
            self.element(MP_SWITCH_CURRENCY_GBP).click()
