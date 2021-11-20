import unittest

import pytest

from pages.login.login_page import LoginPage


@pytest.mark.usefixtures("setUpBeforeTest")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, setUpBeforeTest):
        self.login_page = LoginPage(self.driver)

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        """
        Test sprawdzajacy, czy po wpisaniu zlego loginu i hasla
        uzytkownik sie nie zaloguje i zostanie zwrocony komunikat.
        """

        self.login_page.performLogin(
            email="niepoprawnyemail@email.com",
            password="niepoprawnehaslo",
        )
        expected_result = True
        result = self.login_page.ifLoginFailed()
        assert result == expected_result

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

        excepted_result = True
        result = self.login_page.ifLoginSuccessful()
        assert result == excepted_result
