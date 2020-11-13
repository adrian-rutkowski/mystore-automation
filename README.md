An example testing framework that I've built to present my automation skills using Python with Selenium WebDriver.

Page Object Pattern currently supports the following pages:
- Home Page
- Login Page
- Category Page
- Product Page

Selenium API calls are wrapped in selenium_driver.py

There are 4 sample login tests as of now.

Limitations:
- Currently the framework only supports XPATH locators
- There is no reporting functionality yet
- Utilities like taking a screenshot on failure are planned for the future 
- Test runner in use is Python's built-in unittest but it's going to be replaced by pytest in the future
