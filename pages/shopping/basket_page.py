from base.core import Core


class BasketPage(Core):
    """
    Manipuluje elementami na stronie glownej i koszyku
    w celu wykorzystania ich w testach.

    -dodanie pierwszego produktu ze strony glownej do koszyka,
    sprawdzenie czy jest w koszyku
    -wyszukaj konkretny produkt w wyszukiwarce, dodaj do koszyka
    i sprawdz czy jest w koszyku
    -wejscie do koszyka i wszystkich produktow z koszyka,
    sprawdzenie czy jest w koszyku
    """

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    # Locators
    home_page_button_xpath = "//img[@class='logo img-responsive']"
    select_product_home_button_xpath = "//div[@class='products row']//div[@" \
                                       "class='product']//article[@class='" \
                                       "product-miniature js-product-mini" \
                                       "ature']//div[@class='thumbnail-con" \
                                       "tainer reviews-loaded']//div[@class" \
                                       "='product-description']//h3[@class='" \
                                       "h3 product-title']//a[contains(text" \
                                       "(),'Hummingbird printed t-shirt')]"
    add_to_basket_button_xpath = "//body[@id='product']/main/section[@id=" \
                                 "'wrapper']/div[@class='container']/div" \
                                 "[@id='content-wrapper']/section[@id='main'" \
                                 "]/div[@class='row product-container js-pr" \
                                 "oduct-container']/div[@class='col-md-6']/" \
                                 "div[@class='product-information']/div[@cl" \
                                 "ass='product-actions js-product-actions']/" \
                                 "form[@id='add-to-cart-or-refresh']/div[@cl" \
                                 "ass='product-add-to-cart js-product-add-to" \
                                 "-cart']/div[@class='product-quantity clear" \
                                 "fix']/div[@class='add']/button[1]"
    basket_button_xpath = "//span[contains(text(),'Koszyk')]"
    product_name_home_xpath = "//h1[@class='h1']"
    product_name_home_in_basket_xpath = "//a[contains(text()," \
                                        "'Hummingbird printed t-shirt')]"
    trash_button_xpath = "//i[@class='material-icons float-xs-left']"
    search_input_xpath = "//form[@method='get']//input[@type='text']"
    select_product_nike_button_xpath = "//a[contains(text(),'Nike Air Max " \
                                       "270')]"
    basket_popup_button_xpath = "//a[contains(text(),'Przejdź do realizacji" \
                                " zamówienia')]"
    basket_empty_string_xpath = "//span[@class='no-items']"

    def clickBasketPopUpButton(self):
        """
        Klika w basket button ktory znajduje sie na
        pop-up kiedy dodamy produkt do koszyka.
        """

        self.explicitWaitForElement(
            locator=self.basket_popup_button_xpath,
        )
        self.getElementAndClick(locator=self.basket_popup_button_xpath)

    def clickHomePageButton(self):
        """Klika w website logo button ktore przenosi do Home page."""

        self.getElementAndClick(locator=self.home_page_button_xpath)

    def clickProductFromHomePage(self):
        """Klika w first product na home page."""

        self.getElementAndClick(locator=self.select_product_home_button_xpath)

    def clickProductNikeFromSearchBox(self):
        """Klika w produkt Nike."""

        self.getElementAndClick(locator=self.select_product_nike_button_xpath)

    def clickAddToBasketButton(self):
        """Klika w basket button na selected product page."""

        self.getElementAndClick(locator=self.add_to_basket_button_xpath)

    def clickBasketButton(self):
        """Klika w basket button po to aby przeniesc na basket page."""

        self.getElementAndClick(locator=self.basket_button_xpath)

    def getNameOfProductInProductPage(self):
        """Zwraca nazwe produktu z product page."""

        return self.getElementAndGetTextFromElement(
            locator=self.product_name_home_xpath
        )

    def getNameOfProductNikeInBasket(self):
        """Zwraca nazwe produktu Nike w basket page."""

        return self.getElementAndGetTextFromElement(
            locator=self.select_product_nike_button_xpath
        )

    def getNameOfProductHomeInBasket(self):
        """Zwraca nazwe produktu z home w basket page."""

        return self.getElementAndGetTextFromElement(
            locator=self.product_name_home_in_basket_xpath
        )

    def inputProductNameToSearchBox(self, text):
        """
        Wprowadza text do searchboxa.
        """

        self.getElementAndEnterText(
            locator=self.search_input_xpath,
            text=text,
            pressEnter=True
        )

    def removeProductsFromBasket(self):
        """Usuwa wszystkie produkty z koszyka."""

        self.clickOnElementsFromList(
            locator=self.trash_button_xpath
        )

    def checkBasketTitle(self, title):
        """
        Zweryfikuj czy podany title is equals to current page title.
        """

        result = self.compareCurentTitlePageWithProvidedTitle(title)

        return result

    def performAddProductFromHomePageToBasket(self):
        """
        Wchodzi na strone produktu z home page i dodaje go do koszyka.
        """

        self.clickHomePageButton()
        self.clickProductFromHomePage()
        self.clickAddToBasketButton()

    def performCheckProductInBasket(self):
        """
        Wchodzi do koszyka.
        """

        self.clickBasketPopUpButton()

    def performAddProductFromSearchPageToBasket(self, text):
        """
        Wpisuje w searchbox nazwe produktu wyszukuje go, wchodzi na strone
        tego produktu i dodaje go do koszyka.
        """

        self.clickHomePageButton()
        self.inputProductNameToSearchBox(text)
        self.clickProductNikeFromSearchBox()
        self.clickAddToBasketButton()

    def performRemoveAllProductsFromBasket(self):
        """
        Wchodzi do koszyka i usuwa wszystkie produkty z koszyka.
        """

        self.clickHomePageButton()
        self.clickBasketButton()
        self.removeProductsFromBasket()

    def performOpenBasketWhenIsEmpty(self):
        """
        Probuje wejsc do koszyka kiedy jest pusty.
        """

        self.clickHomePageButton()
        self.clickBasketButton()

    def isBacketEmpty(self):
        """
        Zwraca boolean czy koszyk jest pusty (pojawil sie napis).
        """

        return self.isElementPresent(
            locator=self.basket_empty_string_xpath,
        )
