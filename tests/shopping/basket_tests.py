import unittest

import pytest

from pages.shopping.basket_page import BasketPage
from utilities.additional_functions import AdditionalFunctions
from utilities.test_case_status import TestCaseStatus


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

        self.basket_page.performAddProductFromHomePageToBasket()
        name_in_product_page = self.basket_page.getNameOfProductInProductPage()
        self.basket_page.performCheckProductInBasket()
        name_in_basket_page = self.basket_page.getNameOfProductHomeInBasket()

        test_result_1 = self.basket_page.checkBasketTitle(
            title='Koszyk',
        )

        self.test_status.setTestResult(
            result_message="Titles are equals to each other.",
            test_result=test_result_1,
        )

        test_result_2 = self.additional_functions.getResultOfCompareStrings(
            string1=name_in_product_page,
            string2=name_in_basket_page
        )

        self.test_status.setFinalTestResult(
            test_result=test_result_2,
            test_name="test_addProductFromHomeToBasket",
            result_message="Product found in home page"
                           " correctly added to basket.",
        )

    @pytest.mark.run(order=2)
    def test_addProductFromSearchToBasket(self):
        """
        Test sprawdza, czy po dodaniu produktu wyszukanego
        z search zostanie dodany do koszyka.
        """

        self.basket_page.performAddProductFromSearchPageToBasket(
            text='nike',
        )
        name_in_product_page = self.basket_page.getNameOfProductInProductPage()
        self.basket_page.performCheckProductInBasket()
        name_in_basket_page = self.basket_page.getNameOfProductNikeInBasket()

        test_result_1 = self.basket_page.checkBasketTitle(
            title='Koszyk',
        )

        self.test_status.setTestResult(
            result_message="Titles are equals to each other.",
            test_result=test_result_1,
        )

        test_result_2 = self.additional_functions.getResultOfCompareStrings(
            string1=name_in_product_page,
            string2=name_in_basket_page
        )

        self.test_status.setFinalTestResult(
            test_result=test_result_2,
            test_name="test_addProductFromSearchToBasket",
            result_message="Product found from searchbox "
                           "correctly added to basket.",
        )

    @pytest.mark.run(order=3)
    def test_removeProductsFromBasket(self):
        """
        Test sprawdza czy po usunieciu wszystkich
        produktow z koszyka zostaly one usuniete.
        """

        self.basket_page.performRemoveAllProductsFromBasket()

        test_result_1 = self.basket_page.checkBasketTitle(
            title='Koszyk',
        )

        self.test_status.setTestResult(
            result_message="Titles are equals to each other.",
            test_result=test_result_1,
        )

        test_result_2 = self.basket_page.isBacketEmpty()
        self.test_status.setFinalTestResult(
            test_result=test_result_2,
            test_name="test_removeProductsFromBasket",
            result_message="ALl products are removed from the basket.",
        )
