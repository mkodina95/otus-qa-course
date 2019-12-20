"""
Logging module
"""

import logging

LOG_FILE = "/Users/m.kodina/otus-qa-course/lesson_12/opencart_tests.log"

logging.basicConfig(format="%(levelname)s:%(asctime)s %(message)s",
                    filemode='w',
                    datefmt="%d-%b-%y %H:%M:%S",
                    filename="/Users/m.kodina/otus-qa-course/lesson_12/opencart_tests.log",
                    level=logging.NOTSET)

logger = logging.getLogger('this-is-my-logger')


"""
Functions to print different log messages
"""


def print_browser_logs(logs):
    for l in logs:
        level = l["level"]
        if level == "WARNING":
            logger.log(logging.WARNING, "Message from browser: " + str(l))
        elif level == "SEVERE":
            logger.log(logging.ERROR, "Message from browser: " + str(l))
        elif level == "ERROR":
            logger.log(logging.ERROR, "Message from browser: " + str(l))
        else:
            logger.log(logging.INFO, "Message from browser: " + str(l))


def print_proxy_log(logs):
    logger.log(logging.INFO, "Message from proxy: " + str(logs))
