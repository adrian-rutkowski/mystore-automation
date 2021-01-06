from selenium import webdriver
import pytest

def pytest_addoption(parser):
	parser.addoption(
		"--browser", action="store", default="firefox")


@pytest.fixture()
def setup(request):
	browser = request.config.getoption("--browser")
	base_url = "http://automationpractice.com/index.php"
	if browser == "firefox":
		driver = webdriver.Firefox()
	elif browser == "chrome":
		driver = webdriver.Chrome()

	driver.maximize_window()
	driver.get(base_url)
	request.cls.driver = driver
	yield driver
	driver.quit()
