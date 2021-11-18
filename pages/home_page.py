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

    def clickLoginButton(self):
        self.getElementAndClick(
            type_of_locator="xpath",
            locator=self.login_button_xpath
        )
