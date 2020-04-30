from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver import ActionChains


class SeleniumDriver():

	def __init__(self, driver):
		self.driver = driver

	def get_title(self):
		return self.driver.title

	def get_element(self, locator):
		element = None
		try:
			element = self.driver.find_element(By.XPATH, locator)
			print("Element found with locator: " + locator)
		except:
			print("Element not found. Locator: " + locator)
		return element

	def element_click(self, locator):
		try:
			element = self.get_element(locator)
			element.click()
			print("Clicked on element.")
		except:
			print("Cannot click on the element. Locator: " + locator)

	def send_keys(self, data, locator):
		try:
			element = self.get_element(locator)
			element.click()
			element.clear()
			element.send_keys(data)
			print("Sent data on element.")
		except:
			print("Cannot send data on the element. Locator: " + locator)

	def clear_field(self, locator):
		element = self.get_element(locator)
		element.clear()
		print("Field clear.")

	def is_element_present(self, locator):
		element = self.get_element(locator)
		if element is not None:
			print("Element present.")
			return True
		else:
			print("Element not present.")
			return False

	def is_element_displayed(self, locator):
		element = self.get_element(locator)
		if element is not None:
			is_displayed = element.is_displayed()
			print("Element is displayed")
			return is_displayed
		else:
			print("Element not displayed")
			return False

	def wait_for_element(self, locator, timeout=10, poll_frequency=0.5):
		element = None
		try:
			print("Waiting for maximum " + str(timeout) + " seconds for element to be clickable")
			wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency,
								 ignored_exceptions=[NoSuchElementException,
													 ElementNotVisibleException,
													 ElementNotSelectableException])
			element = wait.until(EC.element_to_be_clickable((locator)))
			print("Element appeared on the web page")
		except:
			print("Element not appeared on the web page")
		return element

	def switch_to_iframe(self, id="", name="", index=None):
		if id:
			self.driver.switch_to.frame(id)
		elif name:
			self.driver.switch_to.frame(name)
		else:
			self.driver.switch_to.frame(index)

	def switch_to_default_content(self):
		self.driver.switch_to.default_content()

	def hover_over(self, cat, subcat):
		category = self.get_element(cat)
		subcategory = self.get_element(subcat)
		actions = ActionChains(self.driver)
		actions.move_to_element(category).perform()
		actions.move_to_element(subcategory).click().perform()
