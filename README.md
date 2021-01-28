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
- Framework supports all the available locator types: id, name, xpath, css selector, class name and link text.

- The framework is based on page object model

![POM](https://i.imgur.com/U2eWdpD.jpg "POM")


- Default test runner is pytest

![Pytest](https://i.imgur.com/KaxBPBo.jpg "Pytest")


- Selenium methods are wrapped in a reusable way

![Selenium](https://i.imgur.com/J3KrVVm.jpg "Selenium")


- Log files take today's date in the file name

![Log](https://i.imgur.com/WzeOEcX.jpg "Log")


- Content of the log file shows detailed info about what is going on in the test according to the debug level

![Content](https://i.imgur.com/fhMMUJw.jpeg "Content")


- [Allure](https://docs.qameta.io/allure/) reports can be generated

![Report](https://i.imgur.com/z3XfWv8.jpeg "Report")


- Screenshots are taken automatically if the test fails

![Screen](https://i.imgur.com/mvcMtnF.jpeg "Screen")



## What is planned?
- Further improvement of selenium wrappers
- Data driven tests
- More tests
