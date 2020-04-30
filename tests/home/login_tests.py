from selenium import webdriver
import unittest
from pages.login_page import LoginPage


class LoginTests(unittest.TestCase):

	def setUp(self):
		global driver
		base_url = "http://automationpractice.com/index.php"
		driver = webdriver.Firefox()
		driver.maximize_window()
		driver.get(base_url)

	def test_login_valid(self):
		lp = LoginPage(driver)
		lp.login("adrianthetranslator@gmail.com", "L3arn!ng")
		result = lp.verify_login_successful()
		self.assertTrue(result)

	def test_login_invalid(self):
		lp = LoginPage(driver)
		lp.login("adrianthetranslator@gmail.com", "abcdefgh")
		result = lp.verify_login_failed()
		self.assertTrue(result)

	def test_login_invalid_2(self):
		lp = LoginPage(driver)
		lp.login(password="abcdefgh")
		result = lp.verify_login_failed()
		self.assertTrue(result)

	def test_login_invalid_3(self):
		lp = LoginPage(driver)
		lp.login(email="adrianthetranslator@gmail.com")
		result = lp.verify_login_failed()
		self.assertTrue(result)

	def tearDown(self):
		driver.quit()


if __name__ == '__main__':
	unittest.main()
