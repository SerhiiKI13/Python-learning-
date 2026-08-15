import logging

logging.basicConfig(level=logging.INFO)

try:
    logging.info("Asking user for a number")
    num = int(input(""))
    logging.info("Number accepted")
except ValueError:
    logging.error("Invalid number")
