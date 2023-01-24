from faker import Faker
from page_objects.MainPage import *


class UserRegistrationPage(MainPage):
	endpoint = "/index.php?route=account/register"

	@allure.step("Getting fake user {data_name}")
	def get_reg_data(self, data_name):
		self.logger.info(f"Getting fake user {data_name}")
		fake = Faker()
		if data_name == "firstname":
			self.firstname = fake.first_name()
			return self.firstname
		elif data_name == "lastname":
			self.lastname = fake.last_name()
			return self.lastname
		elif data_name == "email":
			self.email = fake.email()
			return self.email
		elif data_name == "telephone":
			self.telephone = fake.phone_number()
			return self.telephone
		elif data_name == "password":
			self.password = fake.password()
			return self.password
