from selenium import webdriver
import unittest
from pages.home_page import HomePage


class MyTestCase(unittest.TestCase):

	def setUp(self):
		global driver
		driver = webdriver.Firefox()
		driver.get("http://automationpractice.com/index.php")
		driver.maximize_window()
		self.hp = HomePage(driver)

	def test_something(self):
		# self.hp.enter_search_text("dress")
		# self.hp.click_search_button()
		self.hp.go_to_cat_summer_dresses()


if __name__ == '__main__':
	unittest.main()
