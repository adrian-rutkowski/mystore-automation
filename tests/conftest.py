from selenium import webdriver
import pytest


@pytest.yield_fixture()
def setUp(request):
	base_url = "http://automationpractice.com/index.php"
	driver = webdriver.Firefox()
	driver.maximize_window()
	driver.get(base_url)
	request.cls.driver = driver
	yield driver
	driver.quit()
