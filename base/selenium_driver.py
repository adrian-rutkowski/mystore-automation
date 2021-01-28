from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver import ActionChains
import utilities.log as log
import logging


class SeleniumDriver():

	log = log.log_util(logging.DEBUG)

	def __init__(self, driver):
		self.driver = driver

	def get_title(self):
		return self.driver.title

	def get_by_type(self, locator_type):
		locator_type = locator_type.lower()
		if locator_type == "id":
			return By.ID
		elif locator_type == "name":
			return By.NAME
		elif locator_type == "xpath":
			return By.XPATH
		elif locator_type == "css":
			return By.CSS_SELECTOR
		elif locator_type == "class":
			return By.CLASS_NAME
		elif locator_type == "link":
			return By.LINK_TEXT
		else:
			self.log.critical("Locator type [" + locator_type + "] not supported.")
		return False

	def get_element(self, locator, locator_type="xpath"):
		element = None
		try:
			locator_type = locator_type.lower()
			by_type = self.get_by_type(locator_type)
			element = self.driver.find_element(by_type, locator)
			self.log.debug("Element found with locator: " + "[" + locator_type + "] " + locator)
		except:
			self.log.critical("Element not found. Locator: " + "[" + locator_type + "] " + locator)
		return element

	def element_click(self, locator, locator_type="xpath"):
		try:
			element = self.get_element(locator, locator_type)
			element.click()
			self.log.debug("Clicked on element.")
		except:
			self.log.critical("Cannot click on the element. Locator: " + "[" + locator_type + "] " + locator)

	def send_keys(self, data, locator, locator_type="xpath"):
		try:
			element = self.get_element(locator, locator_type)
			element.click()
			element.clear()
			element.send_keys(data)
			self.log.debug("Sent data on element.")
		except:
			self.log.critical("Cannot send data on the element. Locator: " + "[" + locator_type + "] " + locator)

	def clear_field(self, locator, locator_type="xpath"):
		element = self.get_element(locator, locator_type)
		element.clear()
		self.log.debug("Field clear.")

	def is_element_present(self, locator, locator_type="xpath"):
		element = self.get_element(locator, locator_type)
		if element is not None:
			self.log.debug("Element present.")
			return True
		else:
			self.log.debug("Element not present.")
			return False

	def is_element_displayed(self, locator, locator_type="xpath"):
		element = self.get_element(locator, locator_type)
		if element is not None:
			is_displayed = element.is_displayed()
			self.log.debug("Element is displayed")
			return is_displayed
		else:
			self.log.debug("Element not displayed")
			return False

	def wait_for_element(self, locator, locator_type="xpath", timeout=10, poll_frequency=0.5):
		element = None
		try:
			by_type = self.get_by_type(locator_type)
			print("Waiting for maximum " + str(timeout) + " seconds for element to be clickable")
			wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency,
								 ignored_exceptions=[NoSuchElementException,
													 ElementNotVisibleException,
													 ElementNotSelectableException])
			element = wait.until(EC.element_to_be_clickable((by_type, locator)))
			self.log.debug("Element appeared on the web page")
		except:
			self.log.debug("Element not appeared on the web page")
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
		try:
			category = self.get_element(cat)
			subcategory = self.get_element(subcat)
			actions = ActionChains(self.driver)
			actions.move_to_element(category).perform()
			actions.move_to_element(subcategory).click().perform()
		except:
			self.log.debug("Cannot hover over an element.")
