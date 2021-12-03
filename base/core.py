import logging
import time

from selenium.common.exceptions import (ElementNotSelectableException,
                                        ElementNotVisibleException,
                                        NoSuchElementException)
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

import utilities.logger as logger


class Core:
    """
    Klasa zawierajaca low-levelowe zwrapowane
    metody do interakcji z elementami.
    """

    log = logger.loggerInstance(console_level=logging.DEBUG)

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
            self.log.info(f"Returning type of locator: {type}")
            return dict.get(f"{type.lower()}")
        except Exception:
            self.log.error(f"NOT SUPPORTED Provided Locator's type: '{type}'")
        return False

    def getElement(self, type_of_locator, locator):
        """Zwraca znaleziony element po podanych parametrach na stronie."""

        try:
            by_type = self.getTypeOfLocator(type_of_locator)
            element = self.driver.find_element(by_type, locator)
            self.log.info(
                f'FOUND element with locator type: '
                f'{type_of_locator} and locator: {locator}')
            return element
        except Exception:
            self.log.error(
                f'NOT FOUND element with locator type: '
                f'{type_of_locator} and locator: {locator}')
            return None

    def getElements(self, type_of_locator, locator):
        """
        Zwraca liste znalezionych elementow po podanych parametrach na stronie.
        """

        try:
            by_type = self.getTypeOfLocator(type_of_locator)
            elements = self.driver.find_elements(by_type, locator)
            if len(elements) == 0:
                raise Exception
            self.log.info(
                f'FOUND elements with locator type: '
                f'{type_of_locator} and locator: {locator}')
            return elements
        except Exception:
            self.log.error(
                f'NOT FOUND elements with locator type: '
                f'{type_of_locator} and locator: {locator}')
            return None

    def getElementAndClick(self, locator, type_of_locator="xpath"):
        """Znajduje element lub przyjmuje element i klika go."""

        try:
            element = self.getElement(type_of_locator, locator)
            element.click()
            self.log.info(
                f"CLICKED ON ELEMENT with locator type: "
                f"{type_of_locator} and locator: {locator}"
            )

        except Exception:
            self.log.error(
                f"FAILED TO CLICK on element with locator type: "
                f"{type_of_locator} and locator: {locator}"
            )

    def clickOnElement(self, element):
        """Klika podany w parametrze element."""

        try:
            element.click()
            self.log.info(
                "CLICKED ON ELEMENT provided in parameter."
            )
        except Exception:
            self.log.error(
                "FAILED TO CLICK on provided in parameter element."
            )

    def getElementAndEnterText(
            self,
            locator,
            text,
            type_of_locator="xpath",
            pressEnter=False
    ):
        """Znajduje element i wpisuje w nim podany w parametrze tekst."""

        try:
            element = self.getElement(type_of_locator, locator)
            element.send_keys(text)
            self.log.info(
                f"SENT KEYS to element with locator type: "
                f"{type_of_locator} and locator: {locator}"
            )

            if pressEnter:
                self.log.info(f'pressEnter:{pressEnter} - pressing enter key.')
                element.send_keys(Keys.ENTER)
        except Exception:
            self.log.error(
                f"FAILED TO SEND KEYS to element with locator type: "
                f"{type_of_locator} and locator: {locator}"
            )

    def enterTextToElement(self, element, text):
        """Wpisuje podany w parametrze tekst do wskazanego elementu"""

        try:
            element.send_keys(text)
            self.log.info("SENT KEYS to element provided in parameter.")
        except Exception:
            self.log.error(
                "FAILED TO SEND KEYS to element provided in parameter."
            )

    def isElementPresent(self, locator, type_of_locator="xpath"):
        """Zwraca bool czy element istnieje na stronie."""
        is_present = False
        try:
            element = self.getElement(type_of_locator, locator)
            if element is not None:
                self.log.info(
                    f"ELEMENT IS PRESENT with locator type: "
                    f"{type_of_locator} and locator: {locator}"
                )
                is_present = True
            else:
                self.log.error(
                    f"ELEMENT NOT PRESENT with locator type: "
                    f"{type_of_locator} and locator: {locator}"
                )
            return is_present
        except Exception:
            self.log.error(
                f"ELEMENT NOT PRESENT with locator type: "
                f"{type_of_locator} and locator: {locator}"
            )
            return is_present

    def isElementDisplayed(self, locator, type_of_locator="xpath"):
        """Zwraca boolean czy element jest wyswietlany."""

        try:
            element = self.getElement(type_of_locator, locator)
            if element is not None:
                if element.is_displayed():
                    self.log.info(
                        f"ELEMENT IS DISPLAYED with locator type: "
                        f"{type_of_locator} and locator: {locator}"
                    )
                    return True
            self.log.error(
                f"ELEMENT NOT DISPLAYED with locator type: "
                f"{type_of_locator} and locator: {locator}"
            )
            return False
        except Exception:
            self.log.error(
                f"ELEMENT NOT DISPLAYED with locator type: "
                f"{type_of_locator} and locator: {locator}"
            )
            return False

    def getTitleOfCurrentPage(self):
        """Zwraca tytul strony na ktorej aktualnie driver sie znajduje."""

        self.log.info("Returning title of current page.")
        return self.driver.title

    def compareCurentTitlePageWithProvidedTitle(self, title):
        """
        Zwraca wynik porownywania current title page z
        wprowadzonym w parametrze title.
        """

        self.log.info(f"Comparing current page title with provided: {title}")
        if self.getTitleOfCurrentPage() == title:
            self.log.info(
                "TITLES ARE EQUAL to each other.")
            return True
        self.log.error("TITLES ARE NOT EQUAL to each other.")
        return False

    def backToPreviousPage(self):
        """Driver cofa sie do poprzedniej strony."""

        try:
            self.driver.back()
            self.log.info("Backing to the previous page.")
        except Exception:
            self.log.error("FAILED TO BACK to previous page.")

    def explicitWaitForElement(
            self,
            locator,
            type_of_locator="xpath",
            timeout=10,
            poll_frequency=0.5,
    ):
        """Zwraca element webDriverWait o podanych parametrach."""

        try:
            self.log.info(
                f"Waiting for the element max "
                f"time '{timeout}' seconds to appear")

            wait = WebDriverWait(
                driver=self.driver,
                timeout=timeout,
                poll_frequency=poll_frequency,
                ignored_exceptions=[
                    NoSuchElementException,
                    ElementNotVisibleException,
                    ElementNotSelectableException,
                ])

            element = wait.until(
                expected_conditions.visibility_of_element_located((
                    type_of_locator, locator
                )))

            self.log.info(
                f"APPEARED ELEMENT with locator type: "
                f"{type_of_locator} and locator: {locator}")
            return element
        except Exception:
            self.log.error(
                f"FAILED TO LOCATE ELEMENT with locator type: "
                f"{type_of_locator} and locator: {locator}")
            return None

    def makeScreenShot(self, name):
        """
        Metoda wykonuje zrzut ekranu strony na
        ktorej aktualnie driver sie znajduje.
        """

        file_name = name + "." + str(round(time.time()*1000)) + ".png"
        ss_dir = \
            "D:\\Studia\\pracownia-dyplomowa" \
            "\\projekt-inzynierka\\screenshots\\"

        try:
            self.driver.save_screenshot(f'{ss_dir}{file_name}')
            self.log.info(
                f"Screenshot saved to directory: "
                f"{ss_dir}{file_name}"
            )
        except Exception:
            self.log.error("FAILED to save screenshot.")

    def getCurrentLink(self):
        """
        Zwraca adres aktualnej strony internetowej
        na ktorej driver sie znajduje.
        """

        return self.driver.current_url

    def compareProvidedLinkWithActual(self, link):
        """
        Zwraca boolean czy aktualny link w ktorym
        znajduje sie driver rowna sie linkowi podanemu w parametrze.
        """

        driver_link = self.getCurrentLink()
        self.log.info(f"Comparing {link} with {driver_link}")

        if driver_link == link:
            self.log.info("Both links are equal")
            return True
        self.log.error("Both links are not equal together")
        return False

    def fullScrollCurrentPage(self, direction):
        """
        Scrolluj element w gore lub dol w zaleznosci od podanego parametru.
        """

        dict = {
            "up": self.driver.execute_script("window.scrollBy(0, -1000);"),
            "down": self.driver.execute_script("window.scrollBy(0, 1000);"),
        }
        try:
            dict.get(f'{direction}')
            self.log.info(f"SCROLLED PAGE to {direction} direction.")
        except Exception:
            self.log.error("Not supported direction provided in parameter.")

    def getElementAndScroll(self, locator, type_of_locator="xpath"):
        """Scrolluje strone do wskazanego elementu"""

        try:
            element = self.getElement(type_of_locator, locator)
            self.driver.execute_script(
                "arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("window.scrollBy(0,-150);")
            self.log.info(f"Scrolled to element with locator type: "
                          f"{type_of_locator} and locator: {locator}")
        except Exception:
            self.log.error(f"FAILED TO SCROLL to element with locator type: "
                           f"{type_of_locator} and locator: {locator}")

    def getElementAndGetTextFromElement(
            self,
            locator,
            type_of_locator="xpath"
    ):
        """Zwraca tekst ktory element contains."""

        try:
            element = self.getElement(type_of_locator, locator)
            self.log.info("Trying to get text from element.")
            text_from_element = element.text
            self.log.info(f"Text from element: {text_from_element}")
            return text_from_element
        except Exception:
            self.log.error("FAILED TO TAKE TEXT from element")

    def clickOnElementsFromList(self, locator, type_of_locator="xpath"):
        """
        Pobiera liste elementow i klika w kazdego po kolei.
        """

        try:
            self.log.info("Performing clicking on all elements from the list.")
            elements = self.getElements(type_of_locator, locator)
            for element in elements:
                self.clickOnElement(element)
        except Exception:
            self.log.error("FAILED TO PERFORM CLICKING on "
                           "all elements from the list.")
