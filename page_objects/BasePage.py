from locators import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():

    def __init__(self, browser):
        self.browser = browser

    def page_url(self, base_url, endpoint=None):
        if self.endpoint == None:
            self.browser.get(base_url)
            self.element(PP_PRODUCT_IMG).click()
            return self.browser.current_url
        else:
            return f"{base_url}{self.endpoint}"

    def open(self, base_url):
        self.browser.get(self.page_url(base_url, endpoint=None))

    def element(self, locator: tuple):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(locator))

    def element_not_found(self, locator: tuple):
        return WebDriverWait(self.browser, 5).until_not(EC.visibility_of_element_located(locator))

    def input_text(self, text, locator: tuple):
        form_to_input = self.element(locator)
        form_to_input.click()
        form_to_input.clear()
        form_to_input.send_keys(text)
