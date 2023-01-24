import allure
from locators import *
from page_objects.BasePage import BasePage


class MainPage(BasePage):
    endpoint = "/index.php?route=common/home"

    @allure.step("Switch currency to {currency}")
    def switch_currency_to(self, currency):
        self.logger.info(f"Switch currency to {currency}")

        self.click(MP_DROPDOWN_SWITCH_CURRENCY)

        if currency == "USD":
            self.click(MP_SWITCH_CURRENCY_USD)

        elif currency == "EUR":
            self.click(MP_SWITCH_CURRENCY_EUR)

        elif currency == "GBP":
            self.click(MP_SWITCH_CURRENCY_GBP)
