from base.core import Core


class HomePage(Core):
    """
    Manipuluje elementami na stronie
    ktore sa wykorzystywane w testach.
    """

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    # Locators
    login_button_xpath = "//span[contains(text(),'Zaloguj się')]"
    search_input_xpath = "//form[@method='get']//input[@type='text']"

    def clickLoginButton(self):
        """Klika w login button."""

        self.getElementAndClick(
            type_of_locator="xpath",
            locator=self.login_button_xpath
        )

    def enterTextToSearchBox(self, text):
        """Wpisuje text do searchbox."""

        self.getElementAndEnterText(locator=self.search_input_xpath, text=text)
