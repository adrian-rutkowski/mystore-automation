from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver import ActionChains
import utilities.log as log
import logging
from selenium.webdriver.support.select import Select


class SeleniumDriver:

	log = log.log_util(logging.DEBUG)

	def __init__(self, driver):
		self.driver = driver

	def get_title(self):
		return self.driver.title

	def get_url(self):
		return self.driver.current_url

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

	def hover_over_and_click(self, parent_locator, child_locator, locator_type="xpath"):
		try:
			parent = self.get_element(parent_locator, locator_type)
			actions = ActionChains(self.driver)
			actions.move_to_element(parent).perform()
			self.log.debug("Hovered over the parent element.")
			child = self.get_element(child_locator, locator_type)
			actions.move_to_element(child).click().perform()
			self.log.debug("Clicked on child element.")
		except:
			self.log.critical("Mouse hover failed.")

	def drag_and_drop(self, source_locator, target_locator, locator_type="xpath"):
		try:
			source = self.get_element(source_locator, locator_type)
			target = self.get_element(target_locator, locator_type)
			actions = ActionChains(self.driver)
			actions.drag_and_drop(source, target).perform()
			self.log.debug("Drag and drop successful.")
		except:
			self.log.critical("Drag and drop failed.")

	def dropdown_value_select_by_text(self, locator, text, locator_type="xpath"):
		try:
			dropdown = self.get_element(locator, locator_type)
			self.log.debug("Dropdown found.")
			sel = Select(dropdown)
			sel.select_by_visible_text(text)
			self.log.debug("Dropdown value selected by visible text: " + text)
		except:
			self.log.critical("Cannot find the dropdown.")

	def dropdown_value_select_by_value(self, locator, value, locator_type="xpath"):
		try:
			dropdown = self.get_element(locator, locator_type)
			self.log.debug("Dropdown found.")
			sel = Select(dropdown)
			sel.select_by_value(value)
			self.log.debug("Dropdown value selected by value: " + value)
		except:
			self.log.critical("Cannot find the dropdown.")

	def dropdown_value_select_by_index(self, locator, index, locator_type="xpath"):
		try:
			dropdown = self.get_element(locator, locator_type)
			self.log.debug("Dropdown found.")
			sel = Select(dropdown)
			sel.select_by_index(index)
			self.log.debug("Dropdown value selected by index: " + index)
		except:
			self.log.critical("Cannot find the dropdown.")

	def switch_to_iframe(self, id="", name="", index=None):
		try:
			if id:
				self.driver.switch_to.frame(id)
				self.log.debug("Entering the iframe using ID: " + id)
			elif name:
				self.driver.switch_to.frame(name)
				self.log.debug("Entering the iframe using NAME: " + name)
			else:
				self.driver.switch_to.frame(index)
				self.log.debug("Entering the iframe using INDEX: " + str(index))
		except:
			self.log.critical("Cannot enter the iframe.")

	def switch_to_default_content(self):
		try:
			self.driver.switch_to.default_content()
			self.log.debug("Switching back to default content.")
		except:
			self.log.critical("Cannot switch back to default content.")

	def accept_js_alert(self):
		alert = self.driver.switch_to.alert
		alert.accept()
		self.log.debug("JavaScript alert accepted.")

	def dismiss_js_alert(self):
		alert = self.driver.switch_to.alert
		alert.dismiss()
		self.log.debug("JavaScript alert dismissed.")

	def is_element_present(self, locator, locator_type="xpath"):
		element = self.get_element(locator, locator_type)
		if element is not None:
			self.log.debug("Element is present.")
			return True
		else:
			self.log.debug("Element not present.")
			return False

	def is_element_displayed(self, locator, locator_type="xpath"):
		element = self.get_element(locator, locator_type)
		if element is not None:
			is_displayed = element.is_displayed()
			self.log.debug("Element is displayed.")
			return is_displayed
		else:
			self.log.debug("Element not displayed.")
			return False

	def is_element_clickable(self, locator, locator_type="xpath"):
		element = self.get_element(locator, locator_type)
		if element is not None:
			is_clickable = element.is_clickable()
			self.log.debug("Element is clickable.")
			return is_clickable
		else:
			self.log.debug("Element not clickable.")
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
			self.log.debug("Element appeared on the web page.")
		except:
			self.log.debug("Element not appeared on the web page.")
		return element