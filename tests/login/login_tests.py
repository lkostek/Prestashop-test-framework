import unittest

import pytest
from pages.login.login_page import LoginPage
from utilities.test_case_status import TestCaseStatus


@pytest.mark.usefixtures("setUpBeforeTest")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, setUpBeforeTest):
        self.login_page = LoginPage(self.driver)
        self.test_status = TestCaseStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        """
        Test sprawdzajacy, czy po wpisaniu zlego loginu i hasla
        uzytkownik sie nie zaloguje i zostanie zwrocony komunikat
        i porownuje wyswietlony title page z spodziewanym title.
        """

        self.login_page.performLogin(
            email="niepoprawnyemail@email.com",
            password="niepoprawnehaslo",
        )

        test_result_1 = self.login_page.checkLoginTitle(
            title="Nazwa użytkowika"
        )
        self.test_status.setTestResult(
            test_result=test_result_1,
            result_message="Titles are equals to each other."
        )

        test_result_2 = self.login_page.ifLoginFailed()
        self.test_status.setFinalTestResult(
            test_result=test_result_2,
            result_message="Attempt to login has failed.",
            test_name="test_invalidLogin"
        )

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        """
        Test sprawdzajacy, czy po wpisaniu loginu i hasla do instniejacego
        konta uzytkownik sie zaloguje i zostanie przeniesiony na strone glowna.
        """

        self.login_page.performLogin(
            email="testowekonto@lukaszkostek.pl",
            password="Testowekonto1",
        )

        test_result_1 = self.login_page.checkLoginTitle('Moje konto')
        self.test_status.setTestResult(
            test_result=test_result_1,
            result_message="Titles are equals to each other.",
        )

        test_result_2 = self.login_page.ifLoginSuccessful()
        self.test_status.setFinalTestResult(
            test_result=test_result_2,
            result_message="Correctly performed login to site.",
            test_name="test_validLogin",
        )
