import unittest

import pytest
from utilities.test_case_status import TestCaseStatus
from pages.shopping.basket_page import BasketPage
from utilities.additional_functions import AdditionalFunctions

@pytest.mark.usefixtures("setUpBeforeTest")
class BasketTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, setUpBeforeTest):
        self.basket_page = BasketPage(self.driver)
        self.test_status = TestCaseStatus(self.driver)
        self.additional_functions = AdditionalFunctions()

    @pytest.mark.run(order=1)
    def test_addProductFromHomeToBasket(self):
        """
        Test sprawdza, czy po dodaniu produktu wybranego z home page
        zostanie dodany do koszyka.
        """

        self.basket_page.performAddProductFromHomePageToBasket() # wchodzi w produkt na stronie home
        product_name_in_product_page = self.basket_page.getNameOfProductInProductPage() # pobiera nazwe produktu ze strony produktu
        self.basket_page.performCheckProductInBasket() # wchodzi w koszyk
        product_name_in_basket_page = self.basket_page.getNameOfProductHomeInBasket()

        test_result_1 = self.basket_page.checkBasketTitle(
            title='Koszyk',
        )

        self.test_status.setTestResult(
            result_message="Titles are equals to each other.",
            test_result=test_result_1,
        )

        test_result_2 = self.additional_functions.getResultOfCompareStrings( # porownanie nazwy produktu ze product page i basket page
            string1=product_name_in_product_page,
            string2=product_name_in_basket_page
        )

        self.test_status.setFinalTestResult(
            test_result=test_result_2,
            test_name="test_addProductFromHomeToBasket",
            result_message="Product correctly added to basket.",
        )


    # def test_addProductFromSearchToBasket(self):
    #     """
    #     Test sprawdza, czy po dodaniu produktu wyszukanego
    #     z search zostanie dodany do koszyka.
    #     """
    #
    # def test_removeProductsFromBasket(self):
    #     """
    #     Test sprawdza czy po usunieciu wszystkich
    #     produktow z koszyka zostaly one usuniete.
    #     """

