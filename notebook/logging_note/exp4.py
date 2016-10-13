# coding: utf8
import logging
import logging.config

logging.config.fileConfig(fname='logging.conf')

# create logger
logger_name = 'youdi'
logger = logging.getLogger(name=logger_name)

# print log info
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('error message')

