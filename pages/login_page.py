from base.basepage import BasePage


class LoginPage(BasePage):

	def __init__(self, driver):
		super().__init__(driver)
		self.driver = driver

	# Locators
	_sign_in_link = "//a[@class='login']"
	_email_field = "//input[@id='email']"
	_password_field = "//input[@id='passwd']"
	_sign_in_btn = "//p[@class='submit']//span[1]"
	_username_link = "//span[contains(text(),'Adrian Tester')]"
	_error_box = "//p[contains(text(),'There is 1 error')]"

	def click_sign_in_link(self):
		self.element_click(self._sign_in_link)

	def enter_email(self, email):
		self.send_keys(email, self._email_field)

	def enter_password(self, password):
		self.send_keys(password, self._password_field)

	def click_sign_in_btn(self):
		self.element_click(self._sign_in_btn)

	def login(self, email="", password=""):
		self.click_sign_in_link()
		self.enter_email(email)
		self.enter_password(password)
		self.click_sign_in_btn()

	def verify_login_successful(self):
		result = self.is_element_present(self._username_link)
		return result

	def verify_login_failed(self):
		result = self.is_element_present(self._error_box)
		return result
