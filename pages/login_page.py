from base.core import Core


class LoginPage(Core):
    """
    Manipuluje elementami na stronie logowania
    ktore sa wykorzystywane w testach.
    """

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    # Locators
    email_input_xpath = '//input[@id="field-email"]'
    password_input_xpath = '//input[@id="field-password"]'
    show_password_button_xpath = '//button[@type="button"]'
    forgot_passwd_button_xpath = '//div[@class="forgot-password"]/a'
    create_account_button_xpath = \
        '//a[@data-link-action="display-register-form"]'
    login_link_button_xpath = \
        "//span[@class='hidden-sm-down'][contains(text(),'Zaloguj się')]"
    submit_login_button_xpath = "//button[@id='submit-login']"

    def clickLoginButton(self):
        """Klika w odsylacz do logowania."""

        self.getElementAndClick(locator=self.login_link_button_xpath)

    def enterEmail(self, email):
        """Wpisuje dane do email input."""

        self.getElementAndEnterText(locator=self.email_input_xpath, text=email)

    def enterPassword(self, password):
        """Wpisuje dane do password input."""

        self.getElementAndEnterText(
            locator=self.password_input_xpath,
            text=password
        )

    def clickShowPassword(self):
        """Klika w show password button."""

        self.getElementAndClick(locator=self.show_password_button_xpath)

    def clickForgotPassword(self):
        """Klika w forgot password button."""

        self.getElementAndClick(locator=self.forgot_passwd_button_xpath)

    def clickSubmitLogin(self):
        """Klika w submit login button."""

        self.getElementAndClick(locator=self.submit_login_button_xpath)

    def clickCreateAccount(self):
        """Klika w create account button."""

        self.getElementAndClick(locator=self.create_account_button_xpath)

    def performLogin(self, email, password):
        self.clickLoginButton()
        self.clickShowPassword()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickSubmitLogin()
