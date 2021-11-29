import unittest

import pytest

from pages.login.register_page import RegisterPage
from utilities.test_case_status import TestCaseStatus
from utilities.additional_functions import AdditionalFunctions

@pytest.mark.usefixtures("setUpBeforeTest")
class RegisterTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, setUpBeforeTest):
        self.register_page = RegisterPage(self.driver)
        self.test_status = TestCaseStatus(self.driver)
        self.additional_functions = AdditionalFunctions()

    def test_registerValid(self):
        """
        Test sprawdza, czy po wprowadzeniu poprawnie wszystkich danych w
        formularzu rejestracji nowy uzytkownik zostanie utworzony i zalogowany
        do swojego konta.
        Test sprawdza, czy po rejestracji wyswietli sie strona glowna.
        """

        random_email_name = self.additional_functions.getRandomString(
            length=5
        )
        random_password = self.additional_functions.getRandomString(
            type_of_string='digits',
            length=8,
        )

        self.register_page.performRegister(
            first_name='Adam',
            last_name='Testowy',
            email=f'{random_email_name}@email.com',
            password=f'{random_password}',
            birthday='1999-08-08',
        )

        test_result_1 = self.register_page.checkRegisterTitle(
            title='Sklep internetowy',
        )
        self.test_status.setTestResult(
            test_result=test_result_1,
            result_message="Titles are equals to each other.",
        )

        test_result_2 = self.register_page.ifRegisterSuccessful()
        self.test_status.setFinalTestResult(
            test_result=test_result_2,
            result_message='Attempt to register success',
            test_name='test_registerValid',
        )

    # def test_registerExistingEmail(self):
    #     None
    #
    # def test_regitserInvalidBirthdayFormat(self):
    #     None
