from base.core import Core

class RegisterPage(Core):
    """
    Manipuluje elementami na stronie rejestracji
    ktore sa wykorzystywane w testach.
    """

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    # Locators
    male_selector_xpath = "//body[@id='authentication']/main/" \
                          "section[@id='wrapper']/div[@class='container']" \
                          "/div[@id='content-wrapper']/section[@id='main']" \
                          "/div[@id='content']/section[@class='register-form']" \
                          "/form[@id='customer-form']/div/div[contains(@class," \
                          "'form-group row')]/div[@class='col-md-6 " \
                          "form-control-valign']/label[1]"
    female_selector_xpath = "//input[@id='field-id_gender-2']"
    firstname_input_id = "field-firstname"
    lastname_input_id = "field-lastname"
    email_input_id = "field-email"
    password_input_id = "field-password"
    birthday_input_id = "field-birthday"
    required_checkbox_xpath = "//body[@id='authentication']/main" \
                              "/section[@id='wrapper']/div[@class='container']" \
                              "/div[@id='content-wrapper']/section[@id='main']" \
                              "/div[@id='content']" \
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

