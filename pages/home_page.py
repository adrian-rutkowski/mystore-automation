from base.basepage import BasePage


class HomePage(BasePage):

	def __init__(self, driver):
		super().__init__(driver)
		self.driver = driver

	# Locators
	_search_box = "//input[@id='search_query_top']"
	_search_btn= "//button[@name='submit_search']"
	_cat_dresses = "//a[@class='sf-with-ul'][contains(text(),'Women')]"
	_subcat_summer_dresses = "//li[@class='sfHover']//a[contains(text(),'Summer Dresses')]"

	def enter_search_text(self, phrase):
		self.send_keys(phrase, self._search_box)

	def click_search_button(self):
		self.element_click(self._search_btn)

	def search_for_product(self, phrase):
		self.enter_search_text(phrase)
		self.click_search_button()

	def go_to_cat_summer_dresses(self):
		self.hover_over(self._cat_dresses, self._subcat_summer_dresses)
