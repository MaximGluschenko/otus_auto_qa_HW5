from locators import *
from page_objects.UserRegistrationPage import UserRegistrationPage


def test_check_user_reg_page_elements(browser, base_url):
    user_reg_page = UserRegistrationPage(browser)
    user_reg_page.open(base_url)

    user_reg_page.element(URP_INPUT_FIRSTNAME)
    user_reg_page.element(URP_INPUT_LASTNAME)
    user_reg_page.element(URP_INPUT_EMAIL)
    user_reg_page.element(URP_INPUT_TELEPHONE)
    user_reg_page.element(URP_INPUT_PASSWORD)
    user_reg_page.element(URP_INPUT_CONFIRM)
    user_reg_page.element(URP_PRIVACY_POLICY)
    user_reg_page.element(URP_CHECKBOX_AGREE)
    user_reg_page.element(URP_CONTINUE_BUTTON)


def test_user_reg(browser, base_url):
    user_reg_page = UserRegistrationPage(browser)
    user_reg_page.open(base_url)

    user_reg_page.input_text(user_reg_page.get_reg_data("firstname"), URP_INPUT_FIRSTNAME)
    user_reg_page.input_text(user_reg_page.get_reg_data("lastname"), URP_INPUT_LASTNAME)
    user_reg_page.input_text(user_reg_page.get_reg_data("email"), URP_INPUT_EMAIL)
    user_reg_page.input_text(user_reg_page.get_reg_data("telephone"), URP_INPUT_TELEPHONE)

    password = user_reg_page.get_reg_data("password")
    user_reg_page.input_text(password, URP_INPUT_PASSWORD)
    user_reg_page.input_text(password, URP_INPUT_CONFIRM)

    user_reg_page.element(URP_CHECKBOX_AGREE).click()
    user_reg_page.element(URP_CONTINUE_BUTTON).click()

    assert browser.current_url == f"{base_url}/index.php?route=account/success"
