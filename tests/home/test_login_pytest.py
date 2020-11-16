from selenium import webdriver
from pages.login_page import LoginPage
import unittest
import pytest


@pytest.mark.usefixtures("setUp")
class TestLogin(unittest.TestCase):

	@pytest.fixture(autouse=True)
	def classSetup(self, setUp):
		self.lp = LoginPage(self.driver)

	def test_login_valid(self):
		self.lp.login("adrianthetranslator@gmail.com", "L3arn!ng")
		result = self.lp.verify_login_successful()
		self.assertTrue(result)

	def test_login_invalid_wrong_password(self):
		self.lp.login("adrianthetranslator@gmail.com", "abcdefgh")
		result = self.lp.verify_login_failed()
		self.assertTrue(result)

	def test_login_invalid_wrong_email(self):
		self.lp.login("dummemail@gmail.com", "abcdefgh")
		result = self.lp.verify_login_failed()
		self.assertTrue(result)

	def test_login_invalid_blank_email(self):
		self.lp.login(password="L3arn!ng")
		result = self.lp.verify_login_failed()
		self.assertTrue(result)

	def test_login_invalid_blank_password(self):
		self.lp.login(email="adrianthetranslator@gmail.com")
		result = self.lp.verify_login_failed()
		self.assertTrue(result)