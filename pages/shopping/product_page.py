from base.core import Core

class ProductPage(Core):
    """
    Manipuluje elementami na stronie glownej i koszyku
    w celu wykorzystania ich w testach.
    """

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    # locators
    home_page_button_xpath = "//img[@class='logo img-responsive']"
    search_input_xpath = "//form[@method='get']//input[@type='text']"
    select_product_nike_button_xpath = "//a[contains(text(),'Nike Air Max " \
                                       "270')]"

    def clickHomePageButton(self):
        """Klika w website logo button ktore przenosi do Home page."""

        self.getElementAndClick(locator=self.home_page_button_xpath)

    def inputProductNameToSearchBox(self, text):
        """
        Wprowadza text do searchboxa.
        """

        self.getElementAndEnterText(
            locator=self.search_input_xpath,
            text=text,
            pressEnter=True
        )

    def clickProductNikeFromSearchBox(self):
        """Klika w produkt Nike."""

        self.getElementAndClick(locator=self.select_product_nike_button_xpath)

    def performAddCommentToProduct(self):
        """
        Dodaje komentarz do produktu Nike.
        """


        