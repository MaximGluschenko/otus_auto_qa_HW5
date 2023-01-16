from random import choice
from conftest import catalog_section
from page_objects.MainPage import MainPage


class CatalogPage(MainPage):
	endpoint = f"/{choice(catalog_section)}"

	def __init__(self, browser):
		self.browser = browser
