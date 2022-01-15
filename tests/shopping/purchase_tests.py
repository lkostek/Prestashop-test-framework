import unittest

import pytest

from pages.shopping.purchase_page import PurchasePage
from utilities.additional_functions import AdditionalFunctions
from utilities.test_case_status import TestCaseStatus

@pytest.mark.usefixtures("setUpBeforeTest")
class PurchaseTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, setUpBeforeTest):
        self.purchase_page = PurchasePage(self.driver)
        self.test_status = TestCaseStatus(self.driver)
        self.additional_functions = AdditionalFunctions()

    @pytest.mark.run(order=1)
    def test_PurchaseProduct(self):
        """
        Test weryfikuje czy po przejsciu calego procesu zakupu przedmiotu
        wyswietli sie strona z potwierdzeniem zamowienia co jest
        rownoznaczne z pomyslnym zlozeniem zamowienia.
        """

        self.purchase_page.performPurchase("nike")

        test_result_1 = self.purchase_page.ifOrderedProductStringIsDisplayed()

        self.test_status.setTestResult(
            test_result=test_result_1,
            result_message='Ordered product is displayed on page.',
        )

        test_result_2 = self.purchase_page.ifTitleIsOrderConfirmation(
            text='Potwierdzenie zamówienia',
        )

        self.test_status.setTestResult(
            test_result=test_result_2,
            result_message="Title of page is 'Potwierdzenie zamowienia'",
        )

        test_result_3 = self.purchase_page.ifOrderConfirmationIsDisplayed()

        self.test_status.setFinalTestResult(
            result_message='Confirmation of order is displayed on page',
            test_result=test_result_3,
            test_name='test_PurchaseProduct',
        )