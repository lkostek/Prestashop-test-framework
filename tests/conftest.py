import logging

import pytest

from base.instance_webdriver import WebDriverInstance
from pages.login.login_page import LoginPage
from utilities.logger import loggerInstance

log = loggerInstance(console_level=logging.DEBUG)


# zmienione na function zeby przy kazdym testcase sie wlacza
# przegladarka i wylaczala na koncu
@pytest.fixture(scope="function")
def setUpBeforeTest(request, browser, if_logged):
    """
    Metoda uruchamia sie przy kazdej metodzie.
    Przyjmuje parametr browser, ktory weryfikuje na jakiej przegladarce
    ma sie test uruchomic.
    Przyjmuje parametr if_logged: true/false - jezeli true to metoda na starcie
    poprawnie loguje sie do testowanej strony.
    """

    log.info("### Running setUp method")
    log.info(f"Tests will be executed in browser: {browser}")
    log.info("Creating webdriver instance")
    web_driver_instance = WebDriverInstance(browser)
    driver = web_driver_instance.getWebDriverInstance()

    if if_logged == "true":
        """
        Jezeli podano w parametrze True w
        if_logged to automatycznie sie zaloguje.
        """

        log.info("Auto login: True, executing login to account.")
        login = LoginPage(driver)
        login.performLogin(
            email='testowekonto@lukaszkostek.pl',
            password='Testowekonto1',
        )  # TODO sprawdzic czy w ogole to dziala

    if request.cls is not None:
        request.cls.driver = driver
    yield driver

    driver.quit()# po wykonaniu kodu wylacz przegladarke


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        help="Choose browser: chrome/firefox"
    )
    parser.addoption(
        "--if_logged",
        help="Auto login: true/false"
    )


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def if_logged(request):
    return request.config.getoption("--if_logged")
