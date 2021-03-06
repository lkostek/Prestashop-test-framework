from base.core import Core
from pages.login.login_page import LoginPage


class RegisterPage(Core):
    """
    Manipuluje elementami na stronie rejestracji
    ktore sa wykorzystywane w testach.
    """

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)
        self.login_page = LoginPage(driver)

    # Locators
    male_selector_xpath = "//body[@id='authentication']/main/" \
                          "section[@id='wrapper']/div[@class='container']" \
                          "/div[@id='content-wrapper']/section[@id='main']" \
                          "/div[@id='content']" \
                          "/section[@class='register-form']" \
                          "/form[@id='customer-form']/div" \
                          "/div[contains(@class," \
                          "'form-group row')]/div[@class='col-md-6 " \
                          "form-control-valign']/label[1]"
    female_selector_xpath = "//input[@id='field-id_gender-2']"
    firstname_input_id = "field-firstname"
    lastname_input_id = "field-lastname"
    email_input_id = "field-email"
    password_input_id = "field-password"
    birthday_input_id = "field-birthday"
    required_checkbox_xpath = "//body[@id='authentication']/main" \
                              "/section[@id='wrapper']" \
                              "/div[@class='container']" \
                              "/div[@id='content-wrapper']" \
                              "/section[@id='main']/div[@id='content']" \
                              "/section[@class='register-form']" \
                              "/form[@id='customer-form']/div/div[8]" \
                              "/div[1]/span[1]/label[1]/input[1]"
    required_2_checkbox_xpath = "//body[@id='authentication']/main" \
                                "/section[@id='wrapper']" \
                                "/div[@class='container']" \
                                "/div[@id='content-wrapper']" \
                                "/section[@id='main']/div[@id='content']" \
                                "/section[@class='register-form']" \
                                "/form[@id='customer-form']/div/div[10]" \
                                "/div[1]/span[1]/label[1]/input[1]"
    submit_register_button_xpath = "//button[@type='submit']"
    logout_button_xpath = '//a[@class="logout hidden-sm-down"]'
    error_email_xpath = "//li[@class='alert alert-danger']"
    error_birthday_xpath = "//li[contains(text(),'Format " \
                           "powinien by?? 1970-05-31.')]"

    def selectMaleCheckBox(self):
        """Klika w male checkbox."""

        self.getElementAndClick(locator=self.male_selector_xpath)

    def selectFemaleCheckBox(self):
        """Klika w famale checkbox."""

        self.getElementAndClick(locator=self.female_selector_xpath)

    def enterFirstName(self, first_name):
        """Wpisuje text do first_name input."""

        self.getElementAndEnterText(
            type_of_locator="id",
            locator=self.firstname_input_id,
            text=first_name
        )

    def enterLastName(self, last_name):
        """Wpisuje text do last_name input."""

        self.getElementAndEnterText(
            type_of_locator="id",
            locator=self.lastname_input_id,
            text=last_name
        )

    def enterEmail(self, email):
        """Wpisuje text do email input."""

        self.getElementAndEnterText(
            type_of_locator="id",
            locator=self.email_input_id,
            text=email
        )

    def enterPassword(self, password):
        """Wpisuje text do password input."""

        self.getElementAndEnterText(
            type_of_locator="id",
            locator=self.password_input_id,
            text=password,
        )

    def enterBirthday(self, birthday):
        """Wpisuje text do birthday input."""

        self.getElementAndEnterText(
            type_of_locator="id",
            locator=self.birthday_input_id,
            text=birthday
        )

    def clickRequiredCheckBox1(self):
        """Klika w pierwszy checkbox."""

        self.getElementAndClick(
            locator=self.required_checkbox_xpath
        )

    def clickRequiredCheckBox2(self):
        """Klika w pierwszy checkbox."""

        self.getElementAndClick(
            locator=self.required_2_checkbox_xpath
        )

    def clickSubmitRegister(self):
        """Klika w submit register button."""

        self.getElementAndClick(locator=self.submit_register_button_xpath)

    def ifRegisterSuccessful(self):
        """
        Zwraca boolean czy element Logout jest widoczny na stronie,
        co jest rownoznaczne z tym, ze uzytkownik sie pomyslnie zarejestrowal.
        """

        result = self.isElementPresent(locator=self.logout_button_xpath)
        return result

    def ifRegisterFailed(self):
        """
        Zwraca boolean czy element blad o istniejacym mailu w systemie jest
        wyswietlony, co jest rownoznaczne z tym, ze proba rejestracji sie
        nie powiodla.
        """

        result = self.isElementPresent(locator=self.error_email_xpath)
        return result

    def ifDateOfBirthInvalid(self):
        result = self.isElementPresent(locator=self.error_birthday_xpath)
        return result

    def checkRegisterTitle(self, title):
        """
        Weryfikuje czy podany title jest taki sam jak tytul strony
        na ktorej aktualnie znajduje sie webdriver.
        """

        result = self.compareCurentTitlePageWithProvidedTitle(title)

        return result

    def performRegister(
            self,
            first_name,
            last_name,
            email,
            password,
            birthday=None
    ):
        """
        Wykonuje cala sekwencje metod do proby zarejestrowania nowego konta.
        """

        self.login_page.clickLoginButton()
        self.login_page.clickCreateAccount()
        self.selectMaleCheckBox()
        self.enterFirstName(first_name=first_name)
        self.enterLastName(last_name=last_name)
        self.enterEmail(email=email)
        self.enterPassword(password=password)
        if birthday is not None:
            self.enterBirthday(birthday)
        self.clickRequiredCheckBox1()
        self.clickRequiredCheckBox2()
        self.clickSubmitRegister()
