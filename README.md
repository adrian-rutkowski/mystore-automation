# Test Automation Framework

This is an example testing framework which I have built during my learning journey to present the automation skills using Python with Selenium WebDriver. The tests are meant to cover various functionalities of [automationpractice.com](http://automationpractice.com/index.php) website.

## How is it organised?
The project is structured as follows:
- [base](base) - contains the basepage that is inherited by other pages and also Selenium WebDriver calls
- [pages](pages) - contains methods for user interactions on a given page along with locators
- [tests](tests) - contains tests (more of them to come!)
- [utilities](utilities) - contains useful ways to improve the interaction (eg. logging functionaity)

There are also two other local directories which I do not publish on github:
- logs - contains log files
- reports - contains report files that are used for allure reporting

## What does it offer?
- The framework is based on page object model
![POM](https://imgur.com/U2eWdpD "POM")
- Default test runner is pytest
![Pytest](https://i.imgur.com/KaxBPBo.jpg "Pytest")
- Selenium methods are wrapped in a reusable way
![Selenium](https://imgur.com/J3KrVVm "Selenium")
- Log files take today's date in the file name
![Log](https://imgur.com/WzeOEcX "Log")
- Content of the log file shows detailed info about what is going on in the test according to the debug level
![Content](https://imgur.com/fhMMUJw "Content")
- [Allure](https://docs.qameta.io/allure/) reports can be generated
![Report](https://imgur.com/z3XfWv8 "Report")
- Screenshots are taken automatically if the test fails
![Screen](https://imgur.com/mvcMtnF "Screen")

## What is planned?
- Support for multiple locator types
- Further improvement of selenium wrappers
- Data driven tests
- More tests
