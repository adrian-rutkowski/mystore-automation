from pages.login_page import LoginPage
import pytest
import allure

@pytest.mark.usefixtures("setup")
class TestLogin:

	@pytest.fixture(autouse=True)
	def class_setup(self, setup):
		self.lp = LoginPage(self.driver)

	@allure.title("Login with valid credentials.")
	@allure.description("Test is meant to log the user in with valid credentials.")
	@allure.severity(severity_level="CRITICAL")
	def test_login_valid(self):
		self.lp.login("aadrianthetranslator@gmail.com", "L3arn!ng")
		self.result = self.lp.verify_login_successful()
		assert self.result

	@allure.title("Login with invalid password.")
	def test_login_invalid_wrong_password(self):
		self.lp.login("adrianthetranslator@gmail.com", "abcdefgh")
		self.result = self.lp.verify_login_failed()
		assert self.result

	@allure.title("Login with invalid e-mail.")
	def test_login_invalid_wrong_email(self):
		self.lp.login("dummyemail@gmail.com", "abcdefgh")
		self.result = self.lp.verify_login_failed()
		assert self.result

	@allure.title("Login with blank e-mail.")
	def test_login_invalid_blank_email(self):
		self.lp.login(password="L3arn!ng")
		self.result = self.lp.verify_login_failed()
		assert self.result

	@allure.title("Login with blank password.")
	def test_login_invalid_blank_password(self):
		self.lp.login(email="adrianthetranslator@gmail.com")
		self.result = self.lp.verify_login_failed()
		assert self.result
