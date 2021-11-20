import logging

import pytest

from base.instance_webdriver import WebDriverInstance
from pages.login.login_page import LoginPage
from utilities.logger import loggerInstance

# @pytest.fixture()
# def setUp():
#     None

log = loggerInstance(console_level=logging.DEBUG)


@pytest.fixture(scope="class")
def setUpBeforeTest(request, browser="firefox", if_logged="false"):
    """
    Metoda uruchamia sie przy kazdej metodzie.
    Przyjmuje parametr browser, ktory weryfikuje na jakiej przegladarce
    ma sie test uruchomic.
    Przyjmuje parametr if_logged: jezeli True to metoda na starcie poprawnie
    loguje sie do testowanej strony.
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

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        help="Choose browser: chrome/firefox, default firefox"
    )
    parser.addoption(
        "--if_logged",
        help="Auto login: true/false, default true"
    )


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def if_logged(request):
    return request.config.getoption("--if_logged")
