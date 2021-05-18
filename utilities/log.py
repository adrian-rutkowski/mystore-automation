import inspect
import logging
from datetime import datetime


def log_util(logLevel=logging.DEBUG):
	# Gets the name of the class / method from where this method is called
	logger_name = inspect.stack()[1][3]
	logger = logging.getLogger(logger_name)
	# By default, log all messages
	logger.setLevel(logging.DEBUG)

	fh = logging.FileHandler('C:\\Users\\adrian.rutkowski\\Projects\\PycharmProjects\\mystore-automation\\logs\\automation {:%d-%m-%Y}.log'.format(datetime.now()), mode='a')
	fh.setLevel(logLevel)
	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
								  datefmt='%d-%m-%Y %H:%M:%S')
	fh.setFormatter(formatter)
	logger.addHandler(fh)
	return logger
