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
        self.driver = webdriver.Firefox() #TODO zmienic na driver

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

    def getElement(self, type_of_locator, locator):
        """Zwraca znaleziony element po podanych parametrach na stronie."""

        try:
            by_type = self.getTypeOfLocator(type_of_locator)
            element = self.driver.find_element(by_type, locator)
            self.log.info(
                f'FOUND element with locator type: '
                f'{type_of_locator} and locator: {locator}')
        except Exception:
            self.log.error(
                f'NOT FOUND element with locator type: '
                f'{type_of_locator} and locator: {locator}')
            return None


