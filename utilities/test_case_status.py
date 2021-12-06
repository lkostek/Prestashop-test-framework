import logging

from base.core import Core
from utilities.logger import loggerInstance


class TestCaseStatus(Core):
    """
    Klasa, ktora zbiera wyniki cząstkowe wykonywanego testcase i wypluwająca
    wynik całego testcase biorąc pod uwagę wszystkie resulty.
    """

    log = loggerInstance(console_level=logging.DEBUG)

    def __init__(self, driver):
        super(TestCaseStatus, self).__init__(driver)
        self.test_result_list = []

    def setTestResult(self, test_result, result_message):
        """
        Dodaje do test_result_list wynik czastkowy z testcase i wypluwa
        adekwatne logi.
        """

        try:
            if test_result is not None:
                if test_result is True:
                    self.log.info(f"%%%%% TEST PASSED: {result_message}")
                    self.test_result_list.append("PASSED")
                else:
                    self.log.error(f"%%%%% TEST FAILURE: {result_message}")
                    self.test_result_list.append("FAILURE")
            else:
                self.log.error("%%%%% SOMETHING WENT WRONG")
                self.test_result_list.append("FAILURE")
        except Exception:
            self.log.error("%%%%% SOMETHING WENT WRONG")
            self.test_result_list.append("FAILURE")

    def setFinalTestResult(self, test_result, result_message, test_name):
        """
        Obsluguje ostatni test w testcase i decyduje o
        tym, czy testcase jest fail czy pass.
        """

        #  dodanie ostaniego testu do test_result_list
        self.setTestResult(test_result, result_message)

        if "FAILURE" in self.test_result_list:
            self.log.error(f"%%%%%%%%% TESTCASE {test_name} FAILURE")
            self.test_result_list.clear()
            assert False == True # noqa E712
        else:
            self.log.info(f"%%%%%%%%% TESTCASE {test_name} PASSED")
            self.test_result_list.clear()
            assert True == True # noqa E712
