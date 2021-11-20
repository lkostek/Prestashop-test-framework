from pages.login.login_page import LoginPage
import unittest
import pytest

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
