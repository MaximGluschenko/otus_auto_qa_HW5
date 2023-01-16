from locators import *
from faker import Faker
from page_objects.BasePage import BasePage
from conftest import admin_username, admin_password
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AdminPage(BasePage):
	endpoint = "/admin"

	def __init__(self, browser):
		self.browser = browser

	def admin_login(self, base_url):
		self.open(base_url)
		self.input_text(admin_username, AP_INPUT_USERNAME)
		self.input_text(admin_password, AP_INPUT_PASSWORD)
		self.element(AP_LOGIN_BUTTON).click()

	def admin_add_product(self):
		fake = Faker()
		product_name = fake.lexify()
		product_meta_tag = fake.lexify()
		product_model = fake.lexify()

		self.element(AP_CATALOG_MENU).click()
		self.element(AP_PRODUCTS_LIST).click()
		self.element(AP_ADD_NEW_BUTTON).click()

		self.input_text(product_name, AP_INPUT_ADD_PRODUCT_NAME)
		self.input_text(product_meta_tag, AP_INPUT_ADD_META_TAG_TITLE)
		self.element(AP_DATA_TAB).click()
		self.input_text(product_model, AP_INPUT_ADD_MODEL)
		self.element(AP_SAVE_BUTTON).click()

		return product_name

	def admin_filter_products(self, product_name):
		self.element(AP_CATALOG_MENU).click()
		self.element(AP_PRODUCTS_LIST).click()
		self.input_text(product_name, AP_INPUT_SEARCH_PRODUCT_NAME)
		self.element(AP_BUTTON_FILTER_PRODUCT).click()

	def admin_del_product(self, product_name):
		self.admin_filter_products(product_name)
		self.element(AP_SELECT_PRODUCT_CHECKBOX).click()
		self.element(AP_DELETE_PRODUCT_BUTTON).click()

		alert = WebDriverWait(self.browser, 5).until(EC.alert_is_present())
		alert.accept()
		WebDriverWait(self.browser, 5).until_not(EC.alert_is_present())
