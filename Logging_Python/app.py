import logging

from Logging_Python.log import my_log


def main():
    module_name = __name__.split(".")[-1]
    logger = logging.getLogger(module_name)

    logger.debug("A Debug Message")
    logger.info("An Info Message")
    logger.warning("A Warning Message")
    logger.error("An Error Message")
    logger.critical("A Critical Message")

    try:
        print(5 / 0)
    except ZeroDivisionError:
        logger.exception("An Exception Message")
