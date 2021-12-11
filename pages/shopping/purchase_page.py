import time

from base.core import Core
from pages.shopping.basket_page import BasketPage

class PurchasePage(Core):
    """
    Manipuluje elementami na stronie glownej, koszyka i stron
    realizujacych transakcje w celu wykorzystania ich w testach.
    """

    def __init__(self, driver):
        self.driver = driver
        self.basket_page = BasketPage(driver) # albo tu albo nizej
        super().__init__(driver)

    # Locators
    home_page_button_xpath = "//img[@class='logo img-responsive']"
    enter_to_purchase_button_xpath = "//a[@class='btn btn-primary']"
    personal_data_button_xpath = "//body[@id='checkout']/main/section[@id='w" \
                                 "rapper']/div[@class='container']/div[@id='" \
                                 "content-wrapper']/section[@id='content']/d" \
                                 "iv[@class='row']/div[@class='cart-grid-bod" \
                                 "y col-xs-12 col-lg-8']/section[@id='checko" \
                                 "ut-personal-information-step']/h1[1]"
    personal_data_go_further_button_xpath = "//form[@method='GET']//button[@" \
                                            "type='submit'][contains(text()" \
                                            ",'Dalej')]"
    address_go_further_button_xpath = "//form[@method='POST']//div[@class='" \
                                      "clearfix']//button[@type='submit'][c" \
                                      "ontains(text(),'Dalej')]"
    select_delivery_radio_xpath = "//input[@id='delivery_option_2']"
    delivery_go_furher_button_xpath = "//form[@id='js-delivery']//button[@ty" \
                                      "pe='submit'][contains(text(),'Dalej')]"
    pay_via_transfer_online_radio_xpath = "//input[@id='payment-option-2']"
    agree_rules_checkbox_xpath = "//input[@id='conditions_to_approve[terms-a" \
                                 "nd-conditions]']"
    submit_order_button_xpath = "//button[contains(text(),'Złóż zamówienie')]"

    def clickGoToPurchasePage(self):
        """
        Klika w przycisk "przejdz do realizacji zamowien" na stronie koszyka.
        """

        return self.getElementAndClick(
            locator=self.enter_to_purchase_button_xpath,
        )

    def clickAddressFurtherButton(self):
        """
        Klika w przycisk "Dalej" w zakladce
        "Adresy" na stronie transakcji.
        """

        return self.getElementAndClick(
            locator=self.address_go_further_button_xpath,
        )

    def clickDeliveryMethodRadio(self):
        """
        Klika w radio "My carrier" w zakladce "Sposób dostawy"
        na stronie transakcji.
        """

        return self.getElementAndClick(
            locator=self.select_delivery_radio_xpath,
        )

    def clickDeliveryMethodFurtherButton(self):
        """
        Klika w przycisk "Dalej" w zakladce
        "Sposob dostawy" na stronie transakcji.
        """

        return self.getElementAndClick(
            locator=self.delivery_go_furher_button_xpath,
        )

    def clickOnlineTransferRadio(self):
        """
        Klika na "zaplac przelewem" z lity dostepnych platnosci.
        """

        return self.getElementAndClick(
            locator=self.pay_via_transfer_online_radio_xpath,
        )

    def clickAcceptRulesCheckbox(self):
        """
        Klika w checkbox z regulaminem w zakładce "Platnosc".
        """

        return self.getElementAndClick(
            locator=self.agree_rules_checkbox_xpath
        )

    def performPurchase(self, text):
        """
        Wykonuje cala sekwencje zakupu produktu Nike.
        """
