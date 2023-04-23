import logging
import re

class CriticalErrorException(Exception):
    pass

def configure_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.ERROR)

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.CRITICAL)
    console_handler.setFormatter(formatter)

    file_handler = logging.FileHandler("found_errors.log")
    file_handler.setLevel(logging.ERROR)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    return logger

def read_logs(file_name):

    try:
        with open(file_name, "r") as logs:
            log_text = logs.readlines()
        return log_text
    except FileNotFoundError:
        logger.FileNotFoundError("File or directory does not exist")

def found_errors(file_name):
    logger = configure_logger()
    counter = 0
    for line in read_logs(file_name):
        testLine = line.lower()
        if "critical error" in testLine:
            counter += 1
            try:
                raise CriticalErrorException
            except CriticalErrorException:
                logger.critical(line)
        elif "error" in testLine:
            logger.error(line)
            counter += 1
    return counter



def all_file_lines(file_name):
    lines = 0
    log_lines = re.compile(r'^\d+')
    for line in read_logs(file_name):
        if log_lines.findall(line):
            lines += 1
    return lines


def count_errors(file_name):
    try:
        return f"The number that will be equal to the ratio: {all_file_lines(file_name)/found_errors(file_name)}"
    except ZeroDivisionError:
        logger.error("ZeroDivisionError")


if __name__ == "__main__":
   file = "yupdate.log"
   print(count_errors(file))
