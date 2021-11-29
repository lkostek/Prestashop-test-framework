import string
import random
import logging
from utilities.logger import loggerInstance

# log = loggerInstance(console_level=logging.DEBUG)

class AdditionalFunctions:

    log = loggerInstance(console_level=logging.DEBUG)

    def generateRandomString(self, type_of_string, length):
        """
        Zwraca random string zlozony z wybranego typu znakow i dlugosci.
        """

        generated_string = ''
        type_dict = {
            'lower_strings': string.ascii_lowercase,
            'upper_strings': string.ascii_uppercase,
            'digits': string.digits,
            'digits_letters': string.digits + string.ascii_letters,
        }

        generated_string = generated_string.join(
            random.choice(type_dict[f'{type_of_string}']) for i in range(length)
        )

        self.log.info(f"Returning generated string: {generated_string}")

        return generated_string

    def getRandomString(self, type_of_string="digits_letters",length="6"):
        """
        Uzywa funkcji generateRandomString po to aby zwrocic random string
        """

        self.log.info("Generating string...")
        return self.generateRandomString(type_of_string,length)