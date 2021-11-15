import logging
import inspect
import datetime

def loggerInstance(
    file_level=logging.DEBUG, console_level=None, logger_level=logging.DEBUG
):
    """Metoda tworzy instancje loggera na podstawie podanych parametrow."""

    # Creating instance of logging
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)
    logger.setLevel(logger_level)

    # Setting format of logs
    handler_format = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%d/%m/%Y %H:%M:%S",
    )

    # creating instance of file handler
    file_name = datetime.datetime.now().strftime("%m-%d_%H-%M")
    file_handler = logging.FileHandler(
        filename=f".\\logs\\selenium-webdriver_{file_name}.log", mode="a"
    )
    file_handler.setLevel(file_level)
    file_handler.setFormatter(handler_format)
    logger.addHandler(file_handler)

    # creating instance of console handler
    if console_level is not None:  # if console_level is provided in parameter
        console_handler = logging.StreamHandler()
        console_handler.setLevel(console_level)
        console_handler.setFormatter(handler_format)
        logger.addHandler(console_handler)

    return logger
