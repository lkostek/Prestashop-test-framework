from selenium import webdriver

class WebDriverInstance():
    """
    Klasa sluzy do tworzenia instancji webdrivera
    z uwzglednieniem customowych parametrow.
    """

    def __init__(self, browser):
        self.browser = browser

    def getWebDriverInstance(self, time_seconds=3):
        """Tworzy instancje webdrivera."""

        if self.browser == "firefox":
            driver = webdriver.Firefox(
                executable_path="D:\\Studia\\pracownia-dyplomowa\\"
                                "projekt-inzynierka\\libs\\geckodriver\\"
                                "geckodriver.exe"
            )
        elif self.browser == "chrome":
            driver = webdriver.Chrome(
                executable_path="D:\\Studia\\pracownia-dyplomowa\\"
                                "projekt-inzynierka\\libs\\chromedriver95\\"
                                "chromedriver.exe"
            )
        else:
            driver = webdriver.Firefox(
                executable_path="D:\\Studia\\pracownia-dyplomowa\\"
                                "projekt-inzynierka\\libs\\geckodriver\\"
                                "geckodriver.exe"
            )

        driver.maximize_window()
        driver.implicitly_wait(time_seconds)

        driver.get("https://lukaszkostek.pl")

        return driver
