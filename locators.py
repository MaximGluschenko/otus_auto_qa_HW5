from selenium.webdriver.common.by import By

URP_INPUT_FIRSTNAME = (By.CSS_SELECTOR, '#input-firstname')
URP_INPUT_LASTNAME = (By.CSS_SELECTOR, '#input-lastname')
URP_INPUT_EMAIL = (By.CSS_SELECTOR, '#input-email')
URP_INPUT_TELEPHONE = (By.CSS_SELECTOR, '#input-telephone')
URP_INPUT_PASSWORD = (By.CSS_SELECTOR, '#input-password')
URP_INPUT_CONFIRM = (By.CSS_SELECTOR, '#input-confirm')
URP_PRIVACY_POLICY = (By.LINK_TEXT, "Privacy Policy")
URP_CHECKBOX_AGREE = (By.CSS_SELECTOR, 'input[type="checkbox"][name="agree"]')
URP_CONTINUE_BUTTON = (By.CSS_SELECTOR, 'input[type="submit"][value="Continue"]')


AP_INPUT_USERNAME = (By.CSS_SELECTOR, "#input-username")
AP_INPUT_PASSWORD = (By.CSS_SELECTOR, "#input-password")
AP_LOGIN_BUTTON = (By.CSS_SELECTOR, "[type='submit']")
AP_FORGOTTEN_PASSWORD = (By.LINK_TEXT, "Forgotten Password")
AP_OPEN_CART_LINK_TEXT = (By.LINK_TEXT, "OpenCart")
AP_CATALOG_MENU = (By.CSS_SELECTOR, "#menu-catalog")
AP_PRODUCTS_LIST = (By.CSS_SELECTOR, "#collapse1 > li:nth-child(2)")
AP_ADD_NEW_BUTTON = (By.CSS_SELECTOR, '[data-original-title="Add New"]')
AP_INPUT_ADD_PRODUCT_NAME = (By.CSS_SELECTOR, '#input-name1')
AP_INPUT_ADD_META_TAG_TITLE = (By.CSS_SELECTOR, '#input-meta-title1')
AP_DATA_TAB = (By.CSS_SELECTOR, '[href="#tab-data"]')
AP_INPUT_ADD_MODEL = (By.CSS_SELECTOR, '#input-model')
AP_SAVE_BUTTON = (By.CSS_SELECTOR, '[data-original-title="Save"]')
AP_ALERT_SUCCESS = (By.CSS_SELECTOR, '[class="alert alert-success alert-dismissible"]')
AP_INPUT_SEARCH_PRODUCT_NAME = (By.CSS_SELECTOR, '#input-name')
AP_BUTTON_FILTER_PRODUCT = (By.CSS_SELECTOR, '#button-filter')
AP_SELECT_PRODUCT_CHECKBOX = (By.CSS_SELECTOR, '[name = "selected[]"]')
AP_DELETE_PRODUCT_BUTTON = (By.CSS_SELECTOR, '[data-original-title="Delete"]')


CP_LIST_VIEW = (By.CSS_SELECTOR, "#list-view")
CP_INPUT_SORT = (By.CSS_SELECTOR, "#input-sort")
CP_INPUT_LIMIT = (By.CSS_SELECTOR, "#input-limit")
CP_COMPARE_TOTAL = (By.CSS_SELECTOR, "#compare-total")
CP_LT_NB_LINK_TEXT = (By.LINK_TEXT, "Laptops & Notebooks")


MP_TOP = (By.CSS_SELECTOR, "#top")
MP_SEARCH = (By.CSS_SELECTOR, "#search")
MP_MENU = (By.CSS_SELECTOR, "#menu")
MP_SLIDESHOW = (By.CSS_SELECTOR, "#slideshow0")
MP_FOOTER = (By.CSS_SELECTOR, "footer")
MP_ABOUT_AS_LINK_TEXT = (By.LINK_TEXT, "About Us")
MP_DROPDOWN_SWITCH_CURRENCY = (By.CSS_SELECTOR, 'button[class="btn btn-link dropdown-toggle"][data-toggle="dropdown"]')
MP_SWITCH_CURRENCY_USD = (By.CSS_SELECTOR,
                          'button[class="currency-select btn btn-link btn-block"][type="button"][name="USD"]')
MP_SWITCH_CURRENCY_EUR = (By.CSS_SELECTOR,
                          'button[class="currency-select btn btn-link btn-block"][type="button"][name="EUR"]')
MP_SWITCH_CURRENCY_GBP = (By.CSS_SELECTOR,
                          'button[class="currency-select btn btn-link btn-block"][type="button"][name="GBP"]')


PP_PRODUCT_IMG = (By.CSS_SELECTOR, 'div[class="image"]')
PP_BUTTON_CART = (By.CSS_SELECTOR, "#button-cart")
PP_INPUT_QUANTITY = (By.CSS_SELECTOR, "#input-quantity")
PP_TWEET_LINK_TEXT = (By.LINK_TEXT, "Tweet")
PP_PRODUCT_PRICE = (By.CSS_SELECTOR, '#content > div > div.col-sm-4 > ul:nth-child(4) > li:nth-child(1) > h2')
PP_ADD_TO_WISH_LIST = (By.CSS_SELECTOR,
                       "button[type='button'][class='btn btn-default'][data-original-title='Add to Wish List']")
PP_COMPARE_THIS_PRODUCT = (By.CSS_SELECTOR,
                           "button[type='button'][class='btn btn-default'][data-original-title='Compare this Product']")
