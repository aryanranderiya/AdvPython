
import logging

# 1. Basic Logging Example
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Logging messages
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

# 2. Logging to a File
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

# Reconfigure logging for file
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Logging messages to file
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')

# Reading the log file
with open('example.log', 'r', encoding='utf-8') as f:
    print(f.read())

# 3. Logging an Exception
try:
    result = 10 / 0
except ZeroDivisionError:
    logging.exception('An exception occurred')

# 4. Logging Flow with Custom Logger
logger = logging.getLogger('example_logger')
logger.setLevel(logging.DEBUG)

# Create handlers
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('example.log')

# Set levels for handlers
console_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.ERROR)

# Create formatters and set them for handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Logging messages
logger.debug('This is a debug message')
logger.error('This is an error message')
