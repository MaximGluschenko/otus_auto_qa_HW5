import os
import allure
import logging
from locators import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:

    if not os.path.isdir("logs"):
        os.mkdir("logs")
    def __init__(self, browser):
        self.browser = browser

        self.logger = logging.getLogger(type(self).__name__)
        file_handler = logging.FileHandler(f"logs/{self.browser.test_name}.log")
        file_handler.setFormatter(logging.Formatter('%(asctime)s %(name)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(file_handler)
        self.logger.setLevel(level=self.browser.log_level)

    @allure.step("Getting page url")
    def page_url(self, base_url, endpoint=None):
        self.logger.info(f"Getting {type(self).__name__} url")
        if self.endpoint == None:
            self.browser.get(base_url)
            self.click(PP_PRODUCT_IMG)
            return self.browser.current_url
        else:
            return f"{base_url}{self.endpoint}"

    @allure.step("Opening page url")
    def open(self, base_url):
        page_url = self.page_url(base_url, endpoint=None)
        self.logger.info(f"Opening {type(self).__name__} url: {page_url}")
        self.browser.get(page_url)

    @allure.step("Clicking element {locator}")
    def click(self, locator: tuple):
        self.logger.info(f"Clicking element {locator}")
        WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Check if element {locator} is present")
    def element(self, locator: tuple):
        self.logger.info(f"Check if element {locator} is present")
        try:
            return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(locator))
        except TimeoutException as error:
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise AssertionError(error.msg)

    @allure.step("Check that the {locator} element not found")
    def element_not_found(self, locator: tuple):
        self.logger.info(f"Check that the {locator} element not found")
        try:
            return WebDriverWait(self.browser, 5).until_not(EC.visibility_of_element_located(locator))
        except TimeoutException as error:
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise AssertionError(error.msg)

    @allure.step("Input '{text}' in input {locator}")
    def input_text(self, text, locator: tuple):
        form_to_input = self.element(locator)
        self.logger.info(f"Input '{text}' in input {locator}")
        form_to_input.click()
        form_to_input.clear()
        form_to_input.send_keys(text)
