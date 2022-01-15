import time

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
    add_review_button_xpath = "//body[@id='product']/main/section[" \
                              "@id='wrapper']/div[@class='container'" \
                              "]/div[@id='content-wrapper']/section[" \
                              "@id='main']/div[@class='row']/div[@id" \
                              "='product-comments-list-footer']/butt" \
                              "on[1]"
    title_comment_input_xpath = "//div[@class='col-md-12 col-sm-12']" \
                                "//input[@type='text']"
    review_comment_input_xpath = "//textarea[@name='comment_content']"
    five_stars_button_xpath = "//body[@id='product']/main/section[@id='wra" \
                              "pper']/div[@class='container']/div[@id='cont" \
                              "ent-wrapper']/section[@id='main']/div[@id='p" \
                              "ost-product-comment-modal']/div[@class='mod" \
                              "al-dialog']/div[@class='modal-content']/div" \
                              "[@class='modal-body']/form[@id='post-product" \
                              "-comment-form']/div[@class='row']/div[@class=" \
                              "'col-md-6 col-sm-6']/ul[@id='criterions_list'" \
                              "]/li/div[@class='criterion-rating']/div[@clas" \
                              "s='grade-stars']/div[@class='star-content sta" \
                              "r-full clearfix']/div[5]"
    send_review_button_xpath = "//button[contains(text(),'Wyślij')]"
    cancel_review_button_xpath = "//div[@class='col-md-6 col-sm-6 post-comme" \
                                 "nt-buttons']//button[@type='button'][cont" \
                                 "ains(text(),'Anuluj')]"
    confirm_popup_button_xpath = "//div[@id='product-comment-posted-modal']" \
                                 "//div[contains(@class,'modal-dialog')]//" \
                                 "div[contains(@class,'modal-content')]//d" \
                                 "iv[contains(@class,'modal-body')]//div[co" \
                                 "ntains(@class,'row')]//div[contains(@cla" \
                                 "ss,'col-sm-12 post-comment-buttons')]//b" \
                                 "utton[contains(@type,'button')][contains" \
                                 "(text(),'Tak')]"
    review_popup_xpath = "//div[@id='post-product-comment-modal']//div[@" \
                         "class='modal-dialog']//div[@class='modal-content']"
    select_product_home_button_xpath = "//div[@class='products row']//div[@" \
                                       "class='product']//article[@class='" \
                                       "product-miniature js-product-mini" \
                                       "ature']//div[@class='thumbnail-con" \
                                       "tainer reviews-loaded']//div[@class" \
                                       "='product-description']//h3[@class='" \
                                       "h3 product-title']//a[contains(text" \
                                       "(),'Hummingbird printed t-shirt')]"
    add_first_review_button_xpath = "//button[@class='btn btn-comment btn-co" \
                                    "mment-big post-product-comment']"

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

    def clickAddReviewButton(self):
        """Klika w guzik ktory wywoluje review popup."""

        self.getElementAndClick(
            locator=self.add_review_button_xpath,
        )

    def clickFiveStarButton(self):
        """
        Klika w piątą gwiazdkę na review popup.
        """

        self.getElementAndClick(
            locator=self.five_stars_button_xpath,
        )

    def inputTextToTitleInput(self, text):
        """
        Wpisuje tekst do Title input na review popup.
        """

        self.getElementAndEnterText(
            locator=self.title_comment_input_xpath,
            text=text,
        )

    def inputTextToCommentInput(self, text):
        """
        Wpisuje tekst do Comment input na review popup.
        """

        self.getElementAndEnterText(
            locator=self.review_comment_input_xpath,
            text=text,
        )

    def clickSendReviewButton(self):
        """
        Klika w send review button na review popup.
        """

        self.getElementAndClick(
            locator=self.send_review_button_xpath,
        )

    def clickCancelSendReviewButton(self):
        """
        Klika w cancel send review button na review popup.
        """

        self.getElementAndClick(
            locator=self.cancel_review_button_xpath,
        )

    def scrollDownOnProductPage(self):
        """
        Scrolluje do dolu strony.
        """

        self.fullScrollCurrentPage(direction="down")

    def clickConfirmPopup(self):
        """
        Klika w confirm button na popup po wyslaniu review.
        """
        self.explicitWaitForElement(
            locator=self.confirm_popup_button_xpath
        )
        self.getElementAndClick(
            locator=self.confirm_popup_button_xpath,
        )

    def performAddCommentToProduct(
            self,
            product_name,
            review_title,
            review_comment
    ):
        """
        Wykonuje cala sekwencje dodania komentarza produktu Nike.
        """

        self.clickHomePageButton()
        self.inputProductNameToSearchBox(product_name)
        self.clickProductNikeFromSearchBox()
        time.sleep(2)
        self.scrollDownOnProductPage()
        self.clickAddReviewButton()
        self.clickFiveStarButton()
        self.inputTextToTitleInput(
            text=review_title,
        )
        self.inputTextToCommentInput(
            text=review_comment,
        )
        self.clickSendReviewButton()
        self.clickConfirmPopup()
        time.sleep(3)

    def refreshPage(self):
        """
        Odswieza strone na ktorej jest aktualnie driver.
        """

        self.refreshCurrentPage()

    def waitForTheElement(self, locator, time=10):
        """
        Czeka na pojawienie sie elementu do 10 sekund.
        """

        self.explicitWaitForElement(locator=locator, timeout=time)

    def ifElementIsPresent(self, locator):
        """
        Zwraca boolean czy element znajduje sie na stronie.
        """

        return self.isElementPresent(locator=locator)

    def verifyIfTitleIsPresent(self, title):
        """
        Metoda weryfikuje czy na stronie znajduje
        sie spodziewany tytul komentarza i zwraca boolean.
        """

        expected_title_xpath = f"//h4[contains(text(),'{title}')]"
        self.waitForTheElement(locator=expected_title_xpath)
        return self.ifElementIsPresent(locator=expected_title_xpath)

    def verifyIfCommentIsPresent(self, comment):
        """
        Metoda weryfikuje czy na stronie znajduje
        sie spodziewany komentarz i zwraca boolean.
        """

        expected_comment_xpath = f"//p[contains(text(),'{comment}')]"
        self.waitForTheElement(locator=expected_comment_xpath)
        return self.ifElementIsPresent(locator=expected_comment_xpath)

    def waitForCancelButton(self):
        """
        Czeka do max 5 sekund na pojawienie sie cancel button.
        """

        self.explicitWaitForElement(
            locator=self.cancel_review_button_xpath,
            timeout=5,
        )

    def clickProductFromHomePage(self):
        """Klika w first product na home page."""

        self.getElementAndClick(locator=self.select_product_home_button_xpath)

    def clickAddFirstReviewButton(self):
        """Klika w guzik ktory wywoluje review popup."""

        self.getElementAndClick(
            locator=self.add_first_review_button_xpath,
        )

    def performAddCommentToProductWithoutTitle(
            self,
            review_title,
            review_comment
    ):
        """
        Wykonuje cala sekwencje dodania komentarza produktu Nike.
        """

        self.clickHomePageButton()
        self.clickProductFromHomePage()
        time.sleep(2)
        self.scrollDownOnProductPage()
        self.clickAddFirstReviewButton()
        self.clickFiveStarButton()
        self.inputTextToTitleInput(
            text=review_title,
        )
        self.inputTextToCommentInput(
            text=review_comment,
        )
        self.clickSendReviewButton()
        self.waitForCancelButton()
        self.clickCancelSendReviewButton()
        time.sleep(3)

    def verifyIfReviewWithoutTitleIsPresent(self, comment):
        """
        Metoda weryfikuje czy na stronie znajduje
        sie spodziewana tresc komentarza i zwraca boolean.
        """

        comment_xpath = f"//p[contains(text(),'{comment}')]"
        self.waitForTheElement(locator=comment_xpath, time=4)
        return self.isElementNotPresent(locator=comment_xpath)
