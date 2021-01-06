from base.basepage import BasePage
import utilities.log as log
import logging
import allure

class LoginPage(BasePage):

	log = log.log_util(logging.INFO)

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

	@allure.step("Click on sign in button.")
	def click_sign_in_link(self):
		self.log.info("Click on sign in button.")
		self.element_click(self._sign_in_link)

	@allure.step("Enter e-mail address. [{1}]")
	def enter_email(self, email):
		self.log.info("Enter e-mail address. [" + email + "]")
		self.send_keys(email, self._email_field)

	@allure.step("Enter password. [{1}]")
	def enter_password(self, password):
		self.log.info("Enter password. [" + password + "]")
		self.send_keys(password, self._password_field)

	@allure.step("Sign in.")
	def click_sign_in_btn(self):
		self.log.info("Sign in.")
		self.element_click(self._sign_in_btn)

	def login(self, email="", password=""):
		self.click_sign_in_link()
		self.enter_email(email)
		self.enter_password(password)
		self.click_sign_in_btn()

	@allure.step("Verify successful login.")
	def verify_login_successful(self):
		self.log.info("Verify successful login.")
		result = self.is_element_present(self._username_link)
		return result

	@allure.step("Verify failed login.")
	def verify_login_failed(self):
		self.log.info("Verify failed login.")
		result = self.is_element_present(self._error_box)
		return result
