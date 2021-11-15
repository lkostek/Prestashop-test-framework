import traceback

import utilities.logger as logger
from selenium import webdriver
from selenium.webdriver.common.by import By


class Core:
    """
    Klasa zawierajaca low-levelowe zwrapowane
    metody do interakcji z elementami.
    """

    log = logger.loggerInstance()

    def __init__(self, driver):
        self.driver = driver

    def getTypeOfLocator(self, type):
        """Zwraca element By.X w zaleznosci od podanego parametru."""

        dict = {  # slownik zawierajacy wszystkie obslugiwane locatory
            "id": By.ID,
            "xpath": By.XPATH,
            "css": By.CSS_SELECTOR,
            "classname": By.CLASS_NAME,
            "linktext": By.LINK_TEXT,
        }

        try:
            return dict.get(f"{type.lower()}")
        except Exception:
            self.log.error(f"Locator's type '{type}' is not supported")
            traceback.print_stack()
        return False


