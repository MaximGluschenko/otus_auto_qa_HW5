import allure
from locators import *
from faker import Faker
from page_objects.BasePage import BasePage
from conftest import admin_username, admin_password
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AdminPage(BasePage):
	endpoint = "/admin"


	def admin_login(self, base_url):
		self.logger.info(f"==> Admin authorization started")
		self.input_text(admin_username, AP_INPUT_USERNAME)
		self.input_text(admin_password, AP_INPUT_PASSWORD)
		self.click(AP_LOGIN_BUTTON)
		self.logger.info(f"==> Admin authorization finished")

	@allure.step("Adding a product by an Admin")
	def admin_add_product(self):
		self.logger.info(f"==> Adding a product by an Admin started")
		fake = Faker()
		product_name = fake.lexify()
		product_meta_tag = fake.lexify()
		product_model = fake.lexify()

		self.click(AP_CATALOG_MENU)
		self.click(AP_PRODUCTS_LIST)
		self.click(AP_ADD_NEW_BUTTON)

		self.input_text(product_name, AP_INPUT_ADD_PRODUCT_NAME)
		self.input_text(product_meta_tag, AP_INPUT_ADD_META_TAG_TITLE)
		self.click(AP_DATA_TAB)
		self.input_text(product_model, AP_INPUT_ADD_MODEL)
		self.click(AP_SAVE_BUTTON)
		self.logger.info(f"==> Adding a product by an Admin finished")

		return product_name

	@allure.step("Product filtering")
	def admin_filter_products(self, product_name):
		self.logger.info(f"==> Product filtering started")
		self.click(AP_CATALOG_MENU)
		self.click(AP_PRODUCTS_LIST)
		self.input_text(product_name, AP_INPUT_SEARCH_PRODUCT_NAME)
		self.click(AP_BUTTON_FILTER_PRODUCT)
		self.logger.info(f"==> Product filtering finished")

	@allure.step("Uninstalling a product by an Admin")
	def admin_del_product(self, product_name):
		self.logger.info(f"==> Uninstalling a product by an Admin started")
		self.admin_filter_products(product_name)
		self.click(AP_SELECT_PRODUCT_CHECKBOX)
		self.click(AP_DELETE_PRODUCT_BUTTON)

		alert = WebDriverWait(self.browser, 5).until(EC.alert_is_present())
		alert.accept()
		WebDriverWait(self.browser, 5).until_not(EC.alert_is_present())
		self.logger.info(f"==> Uninstalling a product by an Admin finished")
