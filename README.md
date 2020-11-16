An example testing framework that I've built to present my automation skills using Python with Selenium WebDriver.

Page Object Pattern currently supports the following pages:
- Home Page
- Login Page
- Category Page
- Product Page

Selenium API calls are wrapped in selenium_driver.py

Pytest is the main test runner now. 

There are currently 5 sample login tests.

Limitations:
- Currently the framework only supports XPATH locators
- There is no reporting functionality yet
- Utilities like taking a screenshot on failure are planned for the future 
