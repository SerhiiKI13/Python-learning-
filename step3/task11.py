import logging

logging.basicConfig(level=logging.INFO)

try:
    age = int(input("Enter the number: "))
    if age < 0:
        logging.warning("Age cannot be negative")
    else:
     logging.info("Age accepted")
except ValueError:
    logging.error("Invalid age")