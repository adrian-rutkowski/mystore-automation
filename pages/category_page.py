from base.basepage import BasePage


class CategoryPage(BasePage):

	def __init__(self, driver):
		super().__init__(driver)
		self.driver = driver
