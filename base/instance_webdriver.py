from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class WebDriverInstance():
    """
    Klasa sluzy do tworzenia instancji webdrivera
    z uwzglednieniem customowych parametrow.
    """

    def __init__(self, browser):
        self.browser = browser

    def getWebDriverInstance(self, time_seconds=3):
        """Tworzy instancje webdrivera."""

        if self.browser == "chrome":
            driver = webdriver.Chrome(
                service=Service(".\\libs\\chromedriver97\\"
                                "chromedriver.exe")
            )
        else:
            driver = webdriver.Firefox(
                service=Service(".\\libs\\geckodriver\\"
                                "geckodriver.exe")
            )

        driver.maximize_window()
        driver.implicitly_wait(time_seconds)

        driver.get("https://lukaszkostek.pl")

        return driver
