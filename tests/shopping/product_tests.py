import unittest

import pytest

from pages.shopping.product_page import ProductPage
from utilities.additional_functions import AdditionalFunctions
from utilities.test_case_status import ProgressOfTestingStatus


@pytest.mark.usefixtures("setUpBeforeTest")
class ProductTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, setUpBeforeTest):
        self.product_page = ProductPage(self.driver)
        self.test_status = ProgressOfTestingStatus(self.driver)
        self.additional_functions = AdditionalFunctions()

    @pytest.mark.run(order=1)
    def test_addReviewToProduct(self):
        """
        Test sprawdza, czy po zalogowaniu uzytkownika i po dodaniu recenzji
        na stronie produktu recenzja pojawi sie ona na stronie.
        """

        comment = f'Comment {self.additional_functions.getRandomString()}'
        title = f'Title {self.additional_functions.getRandomString()}'
        self.product_page.performAddCommentToProduct(
            product_name='nike',
            review_comment=comment,
            review_title=title
        )

        self.product_page.refreshPage()

        test_result_1 = self.product_page.verifyIfTitleIsPresent(title)

        self.test_status.setTestResult(
            test_result=test_result_1,
            result_message='Expected title of review '
                           'is present on product page.'
        )

        test_result_2 = self.product_page.verifyIfCommentIsPresent(comment)

        self.test_status.setFinalTestResult(
            test_result=test_result_2,
            result_message='Expected comment of review '
                           'is present on product page.',
            test_name='test_addReviewToProduct'
        )

    @pytest.mark.run(order=2)
    def test_addReviewToProductWithoutTitle(self):
        """
        Test sprawdza, czy po zalogowaniu uzytkownika i po probie dodania
        recenzji produktu bez tytułu recenzja nie zostanie dodana.
        """

        comment = f'Comment {self.additional_functions.getRandomString()}'
        title = ''
        self.product_page.performAddCommentToProductWithoutTitle(
            review_comment=comment,
            review_title=title
        )

        self.product_page.refreshPage()

        test_result_1 = self.product_page.verifyIfReviewWithoutTitleIsPresent(
            comment=comment,
        )

        self.test_status.setFinalTestResult(
            test_result=test_result_1,
            result_message='Review without title '
                           'is not present on product page.',
            test_name='test_addReviewToProductWithoutTitle'
        )
