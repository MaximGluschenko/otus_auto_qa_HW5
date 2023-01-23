import allure
from locators import *
from page_objects.UserRegistrationPage import UserRegistrationPage


@allure.feature('Check page elements')
@allure.story('User registration page')
@allure.title('Check user registration page elements')
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


@allure.feature('User cases')
@allure.story('User registration page')
@allure.title('User registration')
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


    with allure.step('Check account success url'):
        try:
            assert browser.current_url == f"{base_url}/index.php?route=account/success"
        except:
            allure.attach(
                body=browser.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise
