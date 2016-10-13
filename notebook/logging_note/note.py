# coding: utf8
import logging

日志的目的：
1.
诊断日志：记录与应用程序操作相关的日志
2.
审计日志：为商业分析而记录的日志。


# coding: utf8

import logging

logging.debug('debug message')
logging.info('info message')
logging.warn('warn message')
logging.error('error message')
logging.critical('error message')

输出是：
WARNING:root:warn
message
ERROR:root:error
message
CRITICAL:root:critical
message

默认情况下，logging模块将日志打印在屏幕上(stdout), 日志级别为WARNING（即只有日志级别高于WARNING的日志信息才会输出）


日志级别：
debug
info
warn
error
critical

日志输出格式：
WARNING: root: warn
message
日志级别: loggger实例名称 ：日志消息内容

日志级别：
DEBUG
详细信息，典型地调试问题
INFO
证明事情按预期工作
WARNING
表明发生了一些意外，或者不久的将来会发生问题（如：磁盘满了）。软件还是在正常工作。
ERROR ： 由于严重的问题，软件已不能执行一些功能了
CRITICAL
严重问题，表明软件已不能正常继续运行了

logging.basicConfig(filename='logger.log', level=logging.INFO)

logging.debug('debug message')
logging.info('info message')
logging.warn('warn message')
logging.error('error message')
logging.critical('error message')

INFO:root:info
message
WARNING:root:warn
message
ERROR:root:error
message
CRITICAL:root:error
message

因为在
logging.basicConfig()
中level = logging.INFO, 所以在文件中只记录INFO及以上的

重要的概念：
logger记录器，暴露了应用程序代码能直接使用的接口
Handler处理器，将记录器产生的日志记录发送至合适的目的地
Filter过滤器, 提供了更好的粒度控制，他可以决定输出哪些日志记录
Formatter格式化器，指明了最终输出中日志的记录格式的布局

Logger记录器
logger是一个树形层级结构，在使用接口debug，info，warn，error，critical之前必须创建Logger实例
即创建一个记录器，如果没有显式的进行创建，则默认创建一个root
logger，并应用默认的日志级别为(WARN),
处理器Handler(StreamHadler, 即将日志信息打印在输出在标准输出上)
和格式化器Formatter(默认格式即为第一个简单程序输出的格式)

创建方法：
import logging

logger = logging.getLogger(name=logger_name)
创建完logger实例以后，可以使用以下方法进行日志级别设置，增加处理器Handler

logger.setLevel(logging.ERROR)
设置日志级别
logger.addHandler(handler_name)
添加一个处理器
logger.removeHandler(handler_name)
为logger实例伤处一个处理器

Handler处理器
handler处理器类型有很多种，比较常用的有三个
StreamHandler,
FileHandler
NUllHandler

创建StreamHandler之后，可以通过使用以下方法设置日志级别，设置格式化器Formatter, 增加或删除过滤器Filter。
ch = logging.StreamHandler(stream=)
ch.setLevel(logging.ERROR)
指定日志级别
ch.setFormatter(formatter_name)
设置一个格式化器
ch.addFilter(filter_name)
增加一个过滤器，可以增加多个
ch.removeFilter(filter=filter_name)

fh = logging.FileHandler(filename, mode='a', encoding=None, delay=False)

NUllHandler
NUllHnadler类位于核心的logging包，不做任何的格式或者输出
本质上它是个
"什么都不做"
的handler，由库开发者使用。


Formatter格式化器
使用Formatter对象设置日志信息最后的规则，结构和内容，默认格式为 % Y - % m - % d - % d % H: % M: % S

formatter = logging.Formatter(fmt=None, datefmt=None)
其中，fmt是消息的格式化字符串，datefmt是日期字符串。如果不指明fmt，将使用'%(message)s'。如果不指明datefmt，将使用ISO8601日期格式。



Filter过滤器
Handlers和Loggers可以使用Filters来完成比级别更复杂的过滤。Filter基类只允许特定Logger层次以下的事件。
例如用‘A.B’初始化的Filter允许Logger ‘A.B’, ‘A.B.C’, ‘A.B.C.D’, ‘A.B.D’等记录的事件，logger‘A.BB’, ‘B.A.B’ 等就不行。 如果用空字符串来初始化，所有的事件都接受。

filter = logging.Filter(name='')

熟悉了这些概念之后，有另外一个比较重要的事情必须清楚，即Logger是一个树形层级结构;
Logger可以包含一个或多个Handler和Filter，即Logger与Handler或Fitler是一对多的关系;
一个Logger实例可以新增多个Handler，一个Handler可以新增多个格式化器或多个过滤器，而且日志级别将会继承。

Logger  ---(一对多)---> Filter
Logger  -----(一对多)--->Handler
Handler -----(一对一)----->Formatter

Logging的工作流程
logging模块使用过程
1.第一次导入logging模块或使用reload函数重新导入logging模块，logging模块中的代码将被执行，
这个过程中将产生logging日志系统的默认配置。

2.自定义配置(可选)。logging标准模块支持三种配置方式: dictConfig，fileConfig，listen。其中，dictConfig是通过一个字典进行配置Logger，Handler，Filter，Formatter；
fileConfig则是通过一个文件进行配置；而listen则监听一个网络端口，通过接收网络数据来进行配置。当然，除了以上集体化配置外，也可以直接调用Logger，Handler等对象中的方法在代码中来显式配置。

3.使用logging模块的全局作用域中的getLogger函数来得到一个Logger对象实例(其参数即是一个字符串，表示Logger对象实例的名字，即通过该名字来得到相应的Logger对象实例)。






