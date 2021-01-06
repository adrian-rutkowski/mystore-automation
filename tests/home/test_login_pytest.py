from pages.login_page import LoginPage
import pytest


@pytest.mark.usefixtures("setup")
class TestLogin:

	@pytest.fixture(autouse=True)
	def class_setup(self, setup):
		self.lp = LoginPage(self.driver)

	def test_login_valid(self):
		self.lp.login("adrianthetranslator@gmail.com", "L3arn!ng")
		self.result = self.lp.verify_login_successful()
		assert self.result

	def test_login_invalid_wrong_password(self):
		self.lp.login("adrianthetranslator@gmail.com", "abcdefgh")
		self.result = self.lp.verify_login_failed()
		assert self.result

	def test_login_invalid_wrong_email(self):
		self.lp.login("dummyemail@gmail.com", "abcdefgh")
		self.result = self.lp.verify_login_failed()
		assert self.result

	def test_login_invalid_blank_email(self):
		self.lp.login(password="L3arn!ng")
		self.result = self.lp.verify_login_failed()
		assert self.result

	def test_login_invalid_blank_password(self):
		self.lp.login(email="adrianthetranslator@gmail.com")
		self.result = self.lp.verify_login_failed()
		assert self.result
