# coding: utf8
import logging


日志的目的：
1.诊断日志：记录与应用程序操作相关的日志
2.审计日志：为商业分析而记录的日志。


# coding: utf8

import logging

logging.debug('debug message')
logging.info('info message')
logging.warn('warn message')
logging.error('error message')
logging.critical('error message')

输出是：
WARNING:root:warn message
ERROR:root:error message
CRITICAL:root:critical message

默认情况下，logging模块将日志打印在屏幕上(stdout),日志级别为WARNING（即只有日志级别高于WARNING的日志信息才会输出）


日志级别：
debug
info
warn
error
critical

日志输出格式：
WARNING : root : warn message
日志级别 : loggger实例名称 ：日志消息内容



