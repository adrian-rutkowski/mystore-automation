from selenium import webdriver
import pytest
import allure
from allure_commons.types import AttachmentType

def pytest_addoption(parser):
	parser.addoption(
		"--browser", action="store", default="firefox")


# @pytest.fixture()
# def setup(request):
# 	browser = request.config.getoption("--browser")
# 	base_url = "http://automationpractice.com/index.php"
# 	if browser.lower() == "firefox":
# 		driver = webdriver.Firefox()
# 	elif browser.lower() == "chrome":
# 		driver = webdriver.Chrome()
#
# 	driver.maximize_window()
# 	driver.get(base_url)
# 	request.cls.driver = driver
# 	yield driver
# 	driver.quit()

@pytest.fixture()
def setup(request):
	browser = request.config.getoption("--browser")
	base_url = "http://automationpractice.com/index.php"
	if browser.lower() == "firefox":
		driver = webdriver.Firefox()
	elif browser.lower() == "chrome":
		driver = webdriver.Chrome()

	driver.maximize_window()
	driver.get(base_url)
	request.cls.driver = driver
	before_failed = request.session.testsfailed
	yield
	if request.session.testsfailed != before_failed:
		allure.attach(driver.get_screenshot_as_png(), name="Test failed", attachment_type=allure.attachment_type.PNG)
	driver.quit()