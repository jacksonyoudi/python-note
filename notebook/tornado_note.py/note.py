# coding: utf8

Tornado是一个python
web框架和异步网络库, 通过使用非阻塞网络I / O, tornado可以支持上万及级的连接
处理长连接，WebScokets, 和其他需要与每个用户保持长久连接的应用。

import tornado.websocket
import tornado.ioloop
import tornado.iostream

ioloop.py
主要的是将底层的epoll或者说是其他的IO多路复用封装作异步事件来处理
iostream.py主要是对于下层的异步事件的进一步封装，为其封装了更上一层的buffer（IO）事件

ioloop.py底层使用select事件处理和threading

import SocketServer

SocketServer的异步非阻塞的实现
import socket
import select
import sys
import os
import errno

try:
    import threading
except ImportError:
    import dummy_threading as threading

tornado是一个python
web框架和异步网络库，通过使用非网络IO
Tornado可以支持上万级连接，处理长连接，websocket和其他需要与每个用户保持长久连接的应用。

Tornado大体可以分为4个部分。
web框架（包括创建web应用的requestHandler类，还有很多其他的支持类）
HTTP的客户端和服务端实现（HTTPServer and AsyncHTTPClient）
异步网络库(IOLoop and IOStream), 为HTTP组件提供构建模块，也可以用来实现其他协议。
协程库(tornado.gen)
允许异步代码写的更直接而不用链式回调的方式

Tornado
web框架和HTTP
server一起为WSGI提供了一个全栈式的选择，在WSGI容器(WSGIAdapter)
中使用tornado
web

异步和非阻塞I / O
实时web功能需要为每个用户提供一个多数时间被闲置的长连接, 在传统的同步web服务器中，这意味着要为每个用户提供一个线程, 当然每个线程的开销都是很昂贵的.
为了尽量减少并发连接造成的开销，Tornado使用了
一种单线程事件循环的方式.这就意味着所有的应用代码都应该是异步非阻塞的, 因为在同一时间只有一个操作是有效的.

阻塞
一个函数在等待某些事情的返回值的时候会被
阻塞.
函数被阻塞的原因有很多: 网络I / O, 磁盘I / O, 互斥锁等.
事实上
每个
函数在运行和使用CPU的时候都或多或少
会被阻塞
(举个极端的例子来说明为什么对待CPU阻塞要和对待一般阻塞一样的严肃:
比如密码哈希函数
bcrypt, 需要消耗几百毫秒的CPU时间, 这已
经远远超过了一般的网络或者磁盘请求时间了).
一个函数可以在某些方面阻塞在另外一些方面不阻塞.例如, tornado.httpclient
在默认的配置下, 会在
DNS解析上面阻塞, 但是在其他网络请
求的时候不阻塞(为了减轻这种影响，可以用
ThreadedResolver
或者是
通过正确配置
libcurl
用
tornado.curl_httpclient
来做).在Tornado的上下文中, 我们一般讨论网络I / O上下文的阻塞, 尽管各种阻塞已经被最小化.

import tornado.httpclient
import tornado.curl_httpclient

异步
异步
函数在会在完成之前返回，在应用中触发下一个动作之前通常会在后
台执行一些工作
(和正常的
同步
函数在返回前就执行完所有的事情不同).这里列
举了几种风格的异步接口:

回调参数
返回一个占位符(Future, Promise, Deferred)
传送给一个队列
回调注册表(POSIX信号)

不论使用哪种类型的接口, 按照定义
异步函数与它们的调用者都有着不同的交互方
式;
也没有什么对调用者透明的方式使得同步函数异步(类似
gevent
使用轻量级线程的系统性能虽然堪比异步系统, 但它们并
没有真正的让事情异步).

“阻塞”与
"非阻塞"
与
"同步"
与“异步
"不能简单的从字面理解，提供一个从分布式系统角度的回答。
1.
同步与异步
同步和异步关注的是消息通信机制(synchronous
communication / asynchronous
communication)
所谓同步，就是在发出一个 * 调用 * 时，在没有得到结果之前，该 * 调用 * 就不返回。但是一旦调用返回，就得到返回值了。
换句话说，就是由 * 调用者 * 主动等待这个 * 调用 * 的结果。

而异步则是相反，*调用 * 在发出之后，这个调用就直接返回了，所以没有返回结果。换句话说，当一个异步过程调用发出后，调用者不会立刻得到结果。而是在 * 调用 * 发出后，*被调用者 * 通过状态、通知来通知调用者，或通过回调函数处理这个调用。

典型的异步编程模型比如Node.js

举个通俗的例子：
你打电话问书店老板有没有《分布式系统》这本书，如果是同步通信机制，书店老板会说，你稍等，”我查一下
"，然后开始查啊查，等查好了（可能是5秒，也可能是一天）告诉你结果（返回结果）。
而异步通信机制，书店老板直接告诉你我查一下啊，查好了打电话给你，然后直接挂电话了（不返回结果）。然后查好了，他会主动打电话给你。在这里老板通过“回电”这种方式来回调。

2.
阻塞与非阻塞
阻塞和非阻塞关注的是程序在等待调用结果（消息，返回值）时的状态.

阻塞调用是指调用结果返回之前，当前线程会被挂起。调用线程只有在得到结果之后才会返回。
非阻塞调用指在不能立刻得到结果之前，该调用不会阻塞当前线程。

还是上面的例子，
你打电话问书店老板有没有《分布式系统》这本书，你如果是阻塞式调用，你会一直把自己“挂起”，直到得到这本书有没有的结果，如果是非阻塞式调用，你不管老板有没有告诉你，你自己先一边去玩了， 当然你也要偶尔过几分钟check一下老板有没有返回结果。
在这里阻塞与非阻塞与是否同步异步无关。跟老板通过什么方式回答你结果无关。

例子：
一个简单的同步函数

from tornado.httpclient import HTTPClient


def synchronous_fetch(url):
    http_client = HTTPClient()
    response = http_client.fetch(url)
    return response


注意：在没有fetch到值的时候，不会返回调用

使用回调参数重写的异步函数
from tornado.httpclient import AsyncHTTPClient


def asynchrous_fetch(url, callback):
    http_client = AsyncHTTPClient()

    def handle_response(response):
        callback(response.body)

    http_client.fetch(url, callback=handle_response)


使用
Future
代替回调:
from tornado.concurrent import Future


def aync_fetch_future(url):
    http_client = AsyncHTTPClient()
    my_future = Future()
    fetch_future = http_client.fetch()
    fetch_future.add_done_callback(lambda f: my_future.set_result(f.result())))
    return my_funture


from tornado import gen


@gen.coroutine
def fetch_coroutine(url):
    http_client = AsyncHTTPClient()
    response = yield http_client.fetch(url)
    raise gen.Return(response.body)


Tornado是一个强大可扩展的web服务器，它在处理严峻的网络流量时表现得足够强
健，但却在创建和编写时有着足够的轻量级，并能够被用在大量的应用和工具中。
不同于那些最多只能达到10, 000
个并发连接的传统网络服务器，Tornado在设
计之初就考虑到了性能因素，旨在解决C10K问题，这样的设计使得其成为一个拥有非常高性能的框架。
还拥有处理安全性、用户验证、社交网络以及与外部服务（如数据库和网站API）进行异步交互的工具。

异步服务器在这一场景中的应用相对较新，但他们正是被设计用来减轻基于线程的服务器的限制的。当负载增加
时，诸如Node.js，lighttpd和Tornodo这样的服务器使用协作的多任务的方式进行优雅的扩展。也就是说，如果
当前请求正在等待来自其他资源的数据（比如数据库查询或HTTP请求）时，一个异步服务器可以明确地控制以
挂起请求。异步服务器用来恢复暂停的操作的一个常见模式是当合适的数据准备好时调用回调函数。我们将会在
异步Web服务()
讲解回调函数模式以及一系列Tornado异步功能的应用。


# coding: utf8
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

define("port", default=80, help="run on the given port", type=int)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        greeting = self.get_argument('greeting', 'Hello')
        self.write(greeting + ',friendly user!')


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

# python hello.py --port=8000

必须导入的四个模块
import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver

tornado.options从命令行中读取设置。
Tornado包括了一个有用的模块（tornado.options）来从命令行中读取设置。我们在这里使用这个模块指定我
们的应用监听HTTP请求的端口。它的工作流程如下：如果一个与define语句中同名的设置在命令行中被给
出，那么它将成为全局options的一个属性。如果用户运行程序时使用了 - -help
选项，程序将打印出所有你定义
的选项以及你在define函数的help参数中指定的文本。如果用户没有为这个选项指定值，则使用default的值进行
代替。Tornado使用type参数进行基本的参数类型验证，当不合适的类型被给出时抛出一个异常。因此，我们允
许一个整数的port参数作为options.port来访问程序。如果用户没有指定值，则默认为8000。


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        pass


这是Tornado的请求处理函数类，当处理一个请求时，tornado将这个类实例化，并调用与HTTP请求方法所对应的方法。

self.write('string')
响应的字符

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r'/', IndexHandler)])

使用tornado的options模块来解析命令行。
创建一个Application类的实例。传递给Application类init方法最重要的参数是handlers，它告诉tornado应该用
那个类去响应请求。

静态文件：
application = web.Application([
    (r"/static/(.*)", web.StaticFileHandler, {"path": "/var/www"}),
])

虚拟主机
application.add_handlers(r"www\.myhost\.com", [
    (r"/article/([0-9]+)", ArticleHandler),
])

http_server = tornado.httpserver.HTTPServer(app)
http_server.listen(options.port)
tornado.ioloop.IOLoop.instance().start()

一旦Application对象被创建，我们可以将其传递给tornado的HTTPServer对象，然后使用我们在命令行指定的端口进行监听
最后，在程序准备好接收HTTP请求，我们创建一个Tornado的IOLoop的实例。


app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
它应该是一个元组组成的列表，其中每个元组的第一
个元素是一个用于匹配的正则表达式，第二个元素是一个RequestHanlder类。
如果一个正则表达式包含一个捕获分组（即，正则表达式中的部分被括号括起来），匹配的内容将作为相应HTT
P请求的参数传到RequestHandler对象中。我们将在下个例子中看到它的用法。

RequestHandler对象的基础：如何从一个传入的HTTP请求中获得信息（使用ge
t_argument和传入到get和post的参数）以及写HTTP响应（使用write方法）。除此之外，还有很多需要学习
的，我们将在接下来的章节中进行讲解。同时，还有一些关于RequestHandler和Tornado如何使用它的只是需
要记住。



每个RequestHandler类都只定义了一个HTTP方法的行为。但是，在同一个处理函数
中定义多个方法是可能的，并且是有用的。把概念相关的功能绑定到同一个类是一个很好的方法。比如，你可能
会编写一个处理函数来处理数据库中某个特定ID的对象，既使用GET方法，也使用POST方法。想象GET方法来
返回这个部件的信息，而POST方法在数据库中对这个ID的部件进行改变：

restful


# matched with (r"/widget/(\d+)", WidgetHandler)
class WidgetHandler(tornado.web.RequestHandler):
    def get(self, widget_id):
        widget = retrieve_from_db(widget_id)
        self.write(widget.serialize())

    def post(self, widget_id):
        widget = retrieve_from_db(widget_id)
        widget['foo'] = self.get_argument('foo')
        save_to_db(widget)


但Tornado支持任何合法的HTTP请求（GET、POST、PUT、DELETE、HEAD、OPTIONS）
你可以非常容易地定义上述任一种方法的行为，只需要在RequestHandler类中使用同名的方法。
# matched with (r"/frob/(\d+)", FrobHandler)
class FrobHandler(tornado.web.RequestHandler):
    def head(self, frob_id):
        frob = retrieve_from_db(frob_id)
        if frob is not None:
            self.set_status(200)
        else:
            self.set_status(404)

    def get(self, frob_id):
        frob = retrieve_from_db(frob_id)
        self.write(frob.serialize())


注意： 设置状态码，self.set_status(200)

从上面的代码可以看出，你可以使用RequestHandler类的set_status()
方法显式地设置HTTP状态码。然
而，你需要记住在某些情况下，Tornado会自动地设置HTTP状态码。下面是一个常用情况的纲要：

404
Not
Found
Tornado会在HTTP请求的路径无法匹配任何RequestHandler类相对应的模式时返回404（Not
Found）响应
码。
400
Bad
Request
如果你调用了一个没有默认值的get_argument函数，并且没有发现给定名称的参数，Tornado将自动返回一个
400（Bad
Request）响应码。
405
Method
Not
Allowed
如果传入的请求使用了RequestHandler中没有定义的HTTP方法（比如，一个POST请求，但是处理函数中只
有定义了get方法），Tornado将返回一个405（Methos
Not
Allowed）响应码。
500
Internal
Server
Error
当程序遇到任何不能让其退出的错误时，Tornado将返回500（Internal
Server
Error）响应码。你代码中任何
没有捕获的异常也会导致500响应码。

# coding: utf8
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

define("port", default=80, type=int, help='default port')


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        greeting = self.get_argument('greeting', 'Hello')
        self.write(greeting + ',friendly user!')

    def write_error(self, status_code, **kwargs):
        self.write('Gosh darnit,user! you caused a %d error' % status_code)


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r'/', IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


def write_error(self, status_code, **kwargs):
    pass


只是提交数据的时候会报错。




2.
表单和模板

self.get_argument()

self.render('index.html')

self.render('index.html', name=name, age=age)

另外, 模板配置
template_path = os.path.join(os.path.dirname(__file__), 'templates')

os.path.dirname(__file__)
os.path.join(path=, )

template_path参数告诉在哪里寻找模板文件。

self.render('index.html')

2.1
.2
填充
{{}}
变量

2.2
模板语法

from tornado.template import Template

content = Template("<html><body><h1>{{ header }}</h1></body></html>")
print content.generate(header="welcome")

控制语句
{ % if page is none %}
{ % end %}

{ %
for i in a %}
{{i}}
{ % end %}

设置变量
{ % set
foo = 'bar' %}

模板中使用的函数（过滤器）
escape(s)

url_escape(s)
json_encode(val)
squeeze(s)

自动转义：
在Application构造函数中使用autoscaping = None关闭

template_path = os.path.join(os.path.dirname(__file__), "templates")
static_path = os.path.join(os.path.dirname(__file__), "static")

app = tornado.web.Application(
    handlers=[(r'/', IndexHandler), (r'/poem', MungedPageHandler)],
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    debug=True
)

< link
rel = "stylesheet"
href = "{{ static_url("
style.css
") }}" >

将Python标准库的random.choice函数传入模板，这个函数以一个列表作为输入，返回列表中的任
一元素。


debug = True

if self.settings.get('debug'):
    self.settings.setdefault('autoreload', True)
    self.settings.setdefault('compiled_template_cache', False)
    self.settings.setdefault('static_hash_cache', False)
    self.settings.setdefault('serve_traceback', True)

# Automatically reload modified modules
if self.settings.get('autoreload'):
    from tornado import autoreload

    autoreload.start()

它调用了一个便利的测试模式：tornado.autoreload模
块，此时，一旦主要的Python文件被修改，Tornado将会尝试重启服务器，并且在模板改变时会进行刷新。对于
快速改变和实时更新这非常棒，但不要再生产上使用它，因为它将防止Tornado缓存模板！

static_path = os.path.join(os.path.dirname(__file__), "static"),
我们设置了一个当前应用目录下名为static的子目录作为static_path的参数。现在应用将以读取static目
录下的filename.ext来响应诸如 / static / filename.ext的请求，并在响应的主体中返回。

Tornado模板模块提供了一个叫作staticurl的函数来生成static目录下文件的URL。让我们来看看在index.html
中staticurl的调用的示例代码：
< link
rel = "stylesheet"
href = "{{ static_url("
style.css
") }}" >

static_url生成URL的值
这个对static_url的调用生成了URL的值，并渲染输出类似下面的代码：
< link
rel = "stylesheet"
href = "/static/style.css?v=ab12" >

模板扩展

继承
{ % extends
"main.html" %}

{ % block
header %}{ % end %}

{ % block
header %}
< h1 > Hello
world! < / h1 >
{ % end %}

自动转义：

{ % autoescape
None %}
{{mailLink}}

{ % raw
mailLink %}


linkify()
xsrf_form_html()

{ % raw
linkify("https://fb.me/burtsbooks", extra_params='ref=website') %}.
这样，你可以既利用linkify()
简记的好处，又可以保持在其他地方自动转义的好处。


UI模板
UI模块是封装模板中包含的标记、样式以及行为的可复用组件。它所定义的元素通常用于多个模板交叉复用或在
同一个模板中重复使用。模块本身是一个继承自Tornado的UIModule类的简单Python类，并定义了一个render
方法。当一个模板使用
{ % module
Foo(...) %}标签引用一个模块时，Tornado的模板引擎调用模块的render方
法，然后返回一个字符串来替换模板中的模块标签。UI模块也可以在渲染后的页面中嵌入自己的JavaScript和C
SS文件，或指定额外包含的JavaScript或CSS文件。你可以定义可选的embedded_javascript、embedde
d_css、javascript_files和css_files方法来实现这一方法

3.2
.1
基础模块使用


class HelloModule(tornado.web.UIModule):
    def render(self):
        return '<h1>Hello,world</h1>'


app = tornado.web.Application(
    handlers=[(r'/', HelloHandler)],
    template_path=os.path.join(os.path.dirname(__file__), 'templates'),
    ui_modules={'Hello': HelloModule}
)

self.ui_modules = {'linkify': _linkify,
                   'xsrf_form_html': _xsrf_form_html,
                   'Template': TemplateModule,
                   }
self.ui_methods = {}
self._load_ui_modules(settings.get("ui_modules", {}))
self._load_ui_methods(settings.get("ui_methods", {}))

定义一个UIModule的类, 把他名为Hello的模块的引用和我们定义的HelloModule类结合了起来。
现在，当调用HelloHandler并渲染hello.html时，我们可以使用
{ % module
Hello() %}模板标签来包含HelloMo
dule类中render方法返回的字符串。

class BookModule(tornado.web.UIModule):
    def render(self, book):
        return self.render_string('modules/book.html', book=book)


{{locale.format_date(book["date"])}}

为了给这些模块提供更高的灵活性，Tornado允许你使用embedded_css和embedded_javascript方法嵌入其
他的CSS和JavaScript文件。举个例子，如果你想在调用模块时给DOM添加一行文字，你可以通过从模块中嵌
入JavaScript来做到：
class BookModule(tornado.web.UIModule):
    def render(self, book):
        return self.render_string(
            "modules/book.html",
            book=book,
        )


def embedded_javascript(self):
    return "document.write(\"hi!\")"


当调用模块时，document.write(\"hi!\")将被<script> 包围，并被插入到的闭标签中：
                       < script
type = "text/javascript" >
// < ![CDATA[
           document.write("hi!")
           //]] >
      < / script >

          4.
数据库

pymongo - --MongoDB

conn = pymongo.MongoClient("mongodb://user:password@staff.mongohq.com:10066/your_mongohq_db")

db = conn.database_names()

db = conn['youdi']
db.collection_names()

youdi.insert()
插入数据
youdi.find_one("key":"value")

请注意id域。当你创建任何文档时，MongoDB都会自动添加这个域。它的值是一个ObjectID，一种保证文档唯
一的BSON对象。你可能已经注意到，当我们使用insert方法成功创建一个新的文档时，这个ObjectID同样被返
回了。（当你创建文档时，可以通过给id键赋值来覆写自动创建的ObjectID值。）

doc['quantity'] = 4

，字典的改变并不会自动保存到数据库中。如果你希望把字典的改变保存，需要调用集合的save方法，并将
修改后的字典作为参数进行传递：
db.youdi.save(doc)

删除
widgets.remove({"name": "flibnip"})

4.1
.3
MongoDB文档和JSON

import json

json.dumps(obj=obj)
ObjectId('57ff4d5012ca78041d7e3329') is not JSON
serializable
这里的问题是Python的json模块并不知道如何转换MongoDB的ObjectID类型到JSON
有很多方法可以处理
这个问题。其中最简单的方法（也是我们在本章中采用的方法）是在我们序列化之前从字典里简单地删除_id键。
del doc["_id"]

一个更复杂的方法是使用PyMongo的json_util库，它同样可以帮你序列化其他MongoDB特定数据类型到JSON

4.2
一个简单的持久化web服务

5
异步web服务

大部分Web应用（包括我们之前的例子）都是阻塞性质的，也就是说当一个请求被处理时，这个进程就会被挂起
直至请求完成。在大多数情况下，Tornado处理的Web请求完成得足够快使得这个问题并不需要被关注。然
而，对于那些需要一些时间来完成的操作（像大数据库的请求或外部API），这意味着应用程序被有效的锁定直至
处理结束，很明显这在可扩展性上出现了问题。

不过，Tornado给了我们更好的方法来处理这种情况。应用程序在等待第一个处理完成的过程中，让I / O循环打开
以便服务于其他客户端，直到处理完成时启动一个请求并给予反馈，而不再是等待请求完成的过程中挂起进程。

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient

import urllib
import json
import datetime
import time

from tornado.options import define, options

define("port", default=80, type=int)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        query = self.get_argument('q')
        client = tornado.httpclient.HTTPClient()
        response = client.fetch("http://search.twitter.com/search.json?" + \
                                urllib.urlencode({"q": query, "result_type": "recent", "rpp": 100}))
        body = json.loads(response)
        result_count = len(body['result'])
        now = datetime.datetime.utcnow()
        raw_oldest_tweet_at = body['result'][-1]['created_at']
        oldest_tweet_at = datetime.datetime.strptime(raw_oldest_tweet_at,
                                                     "%a, %d %b %Y %H:%M:%S +0000")
        seconds_diff = time.mktime(now.timetuple()) - \
                       time.mktime(oldest_tweet_at.timetuple())
        tweets_per_second = float(result_count) / seconds_diff
        self.write("""
        <div style="text-align: center">
        <div style="font-size: 72px">%s</div>
        <div style="font-size: 144px">%.02f</div>
        <div style="font-size: 24px">tweets per second</div>
        </div>""" % (query, tweets_per_second))


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r'/', IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

client = tornado.httpclient.HTTPClient()
response = client.fetch("http://search.twitter.com/search.json?" + \
                        urllib.urlencode({"q": query, "result_type": "recent", "rpp": 100}))
body = json.loads(response.body)

这里我们实例化了一个Tornado的HTTPClient类，然后调用结果对象的fetch方法。fetch方法的同步版本使用要
获取的URL作为参数。这里，我们构建一个URL来抓取Twitter搜索API的相关搜索结果（rpp参数指定我们想获
得搜索结果首页的100个推文，而result_type参数指定我们只想获得匹配搜索的最近推文）。fetch方法会返回一
个HTTPResponse对象，其
body属性包含我们从远端URL获取的任何数据。Twitter将返回一个JSON格式的
结果，所以我们可以使用Python的json模块来从结果中创建一个Python数据结构。

5.1
.2
阻塞的困扰

到目前为止，我们已经编写了
一个请求Twitter
API并向浏览器返回结果的简单Tornado应用。尽管应用程序本
身响应相当快，但是向Twitter发送请求到获得返回的搜索数据之间有相当大的滞后。在同步（到目前为止，我们
假定为单线程）应用，这意味着同时只能提供一个请求。所以，如果你的应用涉及一个2秒的API请求，你将每间
隔一秒才能提供（最多！）一个请求。这并不是你所称的高可扩展性应用，即便扩展到多线程和 / 或多服务器 。
为了更具体的看出这个问题，我们对刚编写的例子进行基准测试。你可以使用任何基准测试工具来验证这个应用
的性能，不过在这个例子中我们使用优秀的Siege
utility(http: // www.joedog.org / siege - home /) 工具进行测
试。它可以这样使用：

$ siege
http: // localhost:8000 /?q = pants - c10 - t10s

5.1
.3
基础异步调用

幸运的是，Tornado包含一个AsyncHTTPClient类，可以执行异步HTTP请求


class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        query = self.get_argument('q')
        client = tornado.httpclient.AsyncHTTPClient()
        client.fetch("http://search.twitter.com/search.json?" + \
                     urllib.urlencode({"q": query, "result_type": "recent", "rpp": 100}),
                     callback=self.on_response)

    def on_response(self, response):
        body = json.loads(response.body)

    result_count = len(body['results'])
    now = datetime.datetime.utcnow()
    raw_oldest_tweet_at = body['results'][-1]['created_at']
    oldest_tweet_at = datetime.datetime.strptime(raw_oldest_tweet_at,
                                                 "%a, %d %b %Y %H:%M:%S +0000")
    seconds_diff = time.mktime(now.timetuple()) - \
                   time.mktime(oldest_tweet_at.timetuple())
    tweets_per_second = float(result_count) / seconds_diff
    self.write("""
    <div style="text-align: center">
    <div style="font-size: 72px">%s</div>
    <div style="font-size: 144px">%.02f</div>""")


在这个例子中，我们指定on_response方法作为回调函数。我们之前使用期望的输出转化Twitter搜索API请求到
网页中的所有逻辑被搬到了on_response函数中。还需要注意的是 @ tornado.web.asynchronous装饰器的使
用（在get方法的定义之前）以及在回调方法结尾处调用的self.finish()。我们稍后将简要的讨论他们的细节。

5.1
.4
异步装饰器和finish方法

Tornado默认在函数处理返回时关闭客户端的连接。在通常情况下，这正是你想要的。但是当我们处理一个需要
回调函数的异步请求时，我们需要连接保持开启状态直到回调函数执行完毕。你可以在你想改变其行为的方法上
面使用 @ tornado.web.asynchronous装饰器来告诉Tornado保持连接开启，正如我们在异步版本的推率例子
记住当你使用 @ tornado.web.asynchonous装饰器时，Tornado永远不会自己关闭连接。你必须在你的Reque
stHandler对象中调用finish方法来显式地告诉Tornado关闭连接。（否则，请求将可能挂起，浏览器可能不会显
示我们已经发送给客户端的数据。）在前面的异步示例中，我们在on_response函数的write后面调用了finish方

self.finish()

现在，我们的推率程序的异步版本运转的不错并且性能也很好。不幸的是，它有点麻烦：为了处理请求 ，我们不
得不把我们的代码分割成两个不同的方法。当我们有两个或更多的异步请求要执行的时候，编码和维护都显得非
常困难，每个都依赖于前面的调用：不久你就会发现自己调用了一个回调函数的回调函数的回调函数。下面就是
一个构想出来的（但不是不可能的）例子：

def get(self):
    client = AsyncHTTPClient()
    client.fetch("http://example.com", callback=on_response)


def on_response(self, response):
    client = AsyncHTTPClient()
    client.fetch("http://another.example.com/", callback=on_response2)


def on_response2(self, response):
    client = AsyncHTTPClient()
    client.fetch("http://still.another.example.com/", callback=on_response3)


def on_response3(self, response):
    [etc., etc.]


幸运的是，Tornado
2.1
版本引入了tornado.gen模块，可以提供一个更整洁的方式来执行异步请求


class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self):
        query = self.get_argument('q')
        client = tornado.httpclient.AsyncHTTPClient()
        response = yield tornado.gen.Task(client.fetch,
                                          "http://search.twitter.com/search.json?" + \
                                          urllib.urlencode({"q": query, "result_type": "recent", "rpp": 100}))
        body = json.loads(response.body)
        result_count = len(body['results'])
        now = datetime.datetime.utcnow()
        raw_oldest_tweet_at = body['results'][-1]['created_at']
        oldest_tweet_at = datetime.datetime.strptime(raw_oldest_tweet_at,
                                                     "%a, %d %b %Y %H:%M:%S +0000")
        seconds_diff = time.mktime(now.timetuple()) - \
                       time.mktime(oldest_tweet_at.timetuple())
        self.write("""
        <div style="text-align: center">""")
        self.finish()


我们使用Python的yield关键字以及tornado.gen.Task对象的一个实例，将我们想要的调用和传给该调用函数的
参数传递给那个函数。这里，yield的使用返回程序对Tornado的控制，允许在HTTP请求进行中执行其他任
务。当HTTP请求完成时，RequestHandler方法在其停止的地方恢复。这种构建的美在于它在请求处理程序中
返回HTTP响应，而不是回调函数中

记住 @ tornado.gen.engine装饰器的使用需要刚好在get方法的定义之前；这将提醒Tornado这个方法将使用to
rnado.gen.Task类。tornado.gen模块还哟一些其他类和函数可以方便Tornado的异步编程

5.2
使用Tornado进行长轮询
Tornado异步架构的另一个优势是它能够轻松处理HTTP长轮询。这是一个处理实时更新的方法，它既可以应用
到简单的数字标记通知，也可以实现复杂的多用户聊天室。

部署提供实时更新的Web应用对于Web程序员而言是一项长期的挑战。更新用户状态、发送新消息提醒、或者任
何一个需要在初始文档完成加载后由服务器向浏览器发送消息方法的全局活动。一个早期的方法是浏览器以一个
固定的时间间隔向服务器轮询新请求。这项技术带来了新的挑战：轮询频率必须足够快以便通知是最新的，但又
不能太频繁，当成百上千的客户端持续不断的打开新的连接会使HTTP请求面临严重的扩展性挑战。频繁的轮询
使得Web服务器遭受
"凌迟"
之苦。
所谓的
"服务器推送"
技术允许Web应用实时发布更新，同时保持合理的资源使用以及确保可预知的扩展。对于一
个可行的服务器推送技术而言，它必须在现有的浏览器上表现良好。最流行的技术是让浏览器发起连接来模拟服
务器推送更新。这种方式的HTTP连接被称为长轮询或Comet请求。

5.2
.1
长轮询的好处
HTTP长轮询的主要吸引力在于其极大地减少了Web服务器的负载。相对于客户端制造大量的短而频繁的请
求（以及每次处理HTTP头部产生的开销），服务器端只有当其接收一个初始请求和再次发送响应时处理连
接。大部分时间没有新的数据，连接也不会消耗任何处理器资源。
浏览器兼容性是另一个巨大的好处。任何支持AJAX请求的浏览器都可以执行推送请求。不需要任何浏览器插件或
其他附加组件。对比其他服务器端推送技术，HTTP长轮询最终成为了被广泛使用的少数几个可行方案之一。
我们已经接触过长轮询的一些使用。实际上，前面提到的状态更新、消息通知以及聊天消息都是目前流行的网站
功能。像Google
Docs这样的站点使用长轮询同步协作，两个人可以同时编辑文档并看到对方的改变。Twitter使
用长轮询指示浏览器在新状态更新可用时展示通知。Facebook使用这项技术在其聊天功能中。长轮询如此流行
的一个原因是它改善了应用的用户体验：访客不再需要不断地刷新页面来获取最新的内容。


5.2
.3
长轮询的缺陷
正如我们所看到的，HTTP长轮询在站点或特定用户状态的高度交互反馈通信中非常有用。但我们也应该知道它
的一些缺陷。
当使用长轮询开发应用时，记住对于浏览器请求超时间隔无法控制是非常重要的。由浏览器决定在任何中断情况
下重新开启HTTP连接。另一个潜在的问题是许多浏览器限制了对于打开的特定主机的并发请求数量。当有一个
连接保持空闲时，剩下的用来下载网站内容的请求数量就会有限制。

5.3
Tornado与WebSockets
WebSockets是HTML5规范中新提出的客户 - 服务器通讯协议。这个协议目前仍是草案，只有最新的一些浏览器
可以支持它。但是，它的好处是显而易见的，随着支持它的浏览器越来越多，我们将看到它越来越流行。（和以
往的Web开发一样，必须谨慎地坚持依赖可用的新功能并能在必要时回滚到旧技术的务实策略。）
WebSocket协议提供了在客户端和服务器间持久连接的双向通信。协议本身使用新的ws: // URL格式，但它是在
标准HTTP上实现的。通过使用HTTP和HTTPS端口，它避免了从Web代理后的网络连接站点时引入的各种问
题。HTML5规范不只描述了协议本身，还描述了使用WebSockets编写客户端代码所需要的浏览器API。
由于WebSocket已经在一些最新的浏览器中被支持，并且Tornado为之提供了一些有用的模块，因此来看看如
何使用WebSockets实现应用是非常值得的。

5.3
.1
Tornado的WebSocket模块

Tornado在websocket模块中提供了一个WebSocketHandler类。这个类提供了和已连接的客户端通信的Web
Socket事件和方法的钩子。当一个新的WebSocket连接打开时，open方法被调用，而onmessage和onclose
方法分别在连接接收到新的消息和客户端关闭时被调用。

class EchoHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        self.write_message('connected!')

    def on_message(self, message):
        self.write_message(message)


6
编写安全应用
很多时候，安全应用是以牺牲复杂度（以及开发者的头痛）为代价的。Tornado
Web服务器从设计之初就在安全
方面有了很多考虑，使其能够更容易地防范那些常见的漏洞。安全cookies防止用户的本地状态被其浏览器中的
恶意代码暗中修改。此外，浏览器cookies可以与HTTP请求参数值作比较来防范跨站请求伪造攻击。在本章
中，我们将看到使防范这些漏洞更简单的Tornado功能，以及使用这些功能的一个用户验证示例。

6.1
Cookie漏洞

6.1
.1
Cookie伪造
有很多方式可以在浏览器中截获cookies。JavaScript和Flash对于它们所执行的页面的域有读写cookies的权
限。浏览器插件也可由编程方法访问这些数据。跨站脚本攻击可以利用这些访问来修改访客浏览器中cookies的
值。

6.1
.2
安全Cookies
Tornado的安全cookies使用加密签名来验证cookies的值没有被服务器软件以外的任何人修改过。因为一个恶
意脚本并不知道安全密钥，所以它不能在应用不知情时修改cookies。

6.1
.2
.1
使用安全Cookies
Tornado的setsecurecookie()
和getsecurecookie()
函数发送和取得浏览器的cookies，以防范浏览器中的恶
意修改。为了使用这些函数，你必须在应用的构造函数中指定cookie_secret参数。让我们来看一个简单的例
子。


应用将渲染一个统计浏览器中页面被加载次数的页面。如果没有设置cookie（或者cookie已经
被篡改了），应用将设置一个值为1的新cookie。否则，应用将从cookie中读到的值加1。
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        cookie = self.get_secure_cookie("count")
        count = int(cookie) + 1 if cookie else 1

        self.set_secure_cookie("count", str(count))


settings = {
    "cookie_secret": "bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E="
}
application = tornado.web.Application([
    (r'/', MainHandler)
], **settings)

传递给Application构造函数的cookie_secret值应该是唯一的随机字符串。在Python
shell下执行下面的代码片
段将产生一个你自己的值：
>> > import base64, uuid
>> > base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes)
'bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E='

6.1
.2
.2
HTTP - Only和SSL
Cookies
Tornado的cookie功能依附于Python内建的Cookie模块。因此，我们可以利用它所提供的一些安全功能。这些
安全属性是HTTP
cookie规范的一部分，并在它可能是如何暴露其值给它连接的服务器和它运行的脚本方面给予
浏览器指导。比如，我们可以通过只允许SSL连接的方式减少cookie值在网络中被截获的可能性。我们也可以让
浏览器对JavaScript隐藏cookie值。
为cookie设置secure属性来指示浏览器只通过SSL连接传递cookie。（这可能会产生一些困扰，但这不是Torn
ado的安全cookies，更精确的说那种方法应该被称为签名cookies。）从Python
2.6
版本开始，Cookie对象还
提供了一个httponly属性。包括这个属性指示浏览器对于JavaScript不可访问cookie，这可以防范来自读取cook
ie值的跨站脚本攻击。

既然我们已经探讨了一些保护存储在cookies中的持久数据的策略，下面让我们看看另一种常见的攻击载体。下
一节我们将看到一种防范向你的应用发送伪造请求的恶意网站。

任何Web应用所面临的一个主要安全漏洞是跨站请求伪造，通常被简写为CSRF或XSRF，发音为
"sea sur
f
"。这个漏洞利用了浏览器的一个允许恶意攻击者在受害者网站注入脚本使未授权请求代表一个已登录用户的安全
漏洞。让我们看一个例子。

6.2
.1
剖析一个XSRF
假设Alice是Burt
's Books的一个普通顾客。当她在这个在线商店登录帐号后，网站使用一个浏览器cookie标识
她。现在假设一个不择手段的作者，Melvin，想增加他图书的销量。在一个Alice经常访问的Web论坛中，他发
表了一个带有HTML图像标签的条目，其源码初始化为在线商店购物的URL。比如：
< img
src = "http://store.burts-books.com/purchase?title=Melvins+Web+Sploitz" / >
Alice的浏览器尝试获取这个图像资源，并且在请求中包含一个合法的cookies，并不知道取代小猫照片的是在线
商店的购物URL。

6.2
.2
防范请求伪造
有很多预防措施可以防止这种类型的攻击。首先你在开发应用时需要深谋远虑。任何会产生副作用的HTTP请
求，比如点击购买按钮、编辑账户设置、改变密码或删除文档，都应该使用HTTP
POST方法。无论如何，这是
良好的RESTful做法，但它也有额外的优势用于防范像我们刚才看到的恶意图像那样琐碎的XSRF攻击。但
是，这并不足够：一个恶意站点可能会通过其他手段，如HTML表单或XMLHTTPRequest
API来向你的应用发
送POST请求。保护POST请求需要额外的策略。
为了防范伪造POST请求，我们会要求每个请求包括一个参数值作为令牌来匹配存储在cookie中的对应值。我们
的应用将通过一个cookie头和一个隐藏的HTML表单元素向页面提供令牌。当一个合法页面的表单被提交时，它
将包括表单值和已存储的cookie。如果两者匹配，我们的应用认定请求有效。
由于第三方站点没有访问cookie数据的权限，他们将不能在请求中包含令牌cookie。这有效地防止了不可信网站
发送未授权的请求。正如我们看到的，Tornado同样会让这个实现变得简单。

6.2
.3
使用Tornado的XSRF保护

settings = {
    "cookie_secret": "bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
    "xsrf_cookies": True
}
application = tornado.web.Application([
    (r'/', MainHandler),
    (r'/purchase', PurchaseHandler),
], **settings)

"xsrf_cookie": True

当这个应用标识被设置时，Tornado将拒绝请求参数中不包含正确的xsrf值的POST、PUT和DELETE请求。T
ornado将会在幕后处理xsrf
cookies，但你必须在你的HTML表单中包含XSRF令牌以确保授权合法请求。
。要做
到这一点，只需要在你的模板中包含一个xsrfformhtml调用即可：

{ % raw
xsrf_form_html() %}


6.2
.3
.1
XSRF令牌和AJAX请求
AJAX请求也需要一个xsrf参数，但不是必须显式地在渲染页面时包含一个xsrf值，而是通过脚本在客户端查询浏
览器获得cookie值。下面的两个函数透明地添加令牌值给AJAX
POST请求。第一个函数通过名字获取cooki
e，而第二个函数是一个添加_xsrf参数到传递给postJSON函数数据对象的便捷函数。


6.3
用户验证
既然我们已经看到了如何安全地设置和取得cookies，并理解了XSRF攻击背后的原理，现在就让我们看一个简单
用户验证系统的演示示例。在本节中，我们将建立一个应用，询问访客的名字，然后将其存储在安全cookie
中，以便之后取出。后续的请求将认出回客，并展示给她一个定制的页面。你将学到login_url参数和tornado.we
b.authenticated装饰器的相关知识，这将消除在类似应用中经常会涉及到的一些头疼的问题。



class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie('username')


class LoginHandler(BaseHandler):
    def get(self):
        self.render('login.html')

    def post(self):
        self.set_secure_cookie('username',self.get_argument("username"))

class LogoutHandler(BaseHandler):
    def get(self):
        if self.get_argument("Logout",None):
            self.clear_cookie("username")
            self.redirect("/")


"login_url":"/login"

6.3.2 authenticated装饰器
为了使用Tornado的认证功能，我们需要对登录用户标记具体的处理函数。我们可以使用@tornado.web.authe
nticated装饰器完成它。当我们使用这个装饰器包裹一个处理方法时，Tornado将确保这个方法的主体只有在合
法的用户被发现时才会调用。让我们看看例子中的WelcomeHandler吧，这个类只对已登录用户渲染index.html
模板。

6.3.2.1 current_user属性
请求处理类有一个currentuser属性（同样也在处理程序渲染的任何模板中可用）可以用来存储为当前请求进行用
户验证的标识。其默认值为None。为了authenticated装饰器能够成功标识一个已认证用户，你必须覆写请求处
理程序中默认的getcurrent_user()方法来返回当前用户。

6.3.2.2 login_url设置
"login_url": "/login"

使用OAuth协议安全验证某人的身份，同时允许他们的用户保持第三方应用访问他们个人信息的控
制权。Tornado提供了一些Python mix-in来帮助开发者验证外部服务，既包括显式地支持流行服务，也包括通
过通用的OAuth支持。在本章中，我们将探讨两个使用Tornado的auth模块的示例应用：一个连接Twitter，另
一个连接Facebook。


7.1.1 认证流程
这些认证方法的工作流程虽然有一些轻微的不同，但对于大多数而言，都使用了authorize_redirect 和get_auth
enticated_user 方法。authorize_rediect 方法用来将一个未授权用户重定向到外部服务的验证页面。在验证页
面中，用户登录服务，并让你的应用拥有访问他账户的权限。通常情况下，你会在用户带着一个临时访问码返回
你的应用时使用get_authenticated_user 方法。调用get_authenticated_user 方法会把授权跳转过程提供的临
时凭证替换成属于用户的长期凭证。Twitter、Facebook、FriendFeed和Google的具体验证类提供了他们自己
的函数来使API调用它们的服务。

authorize_redirect
get_authenticated_user

7.1.2 异步请求
关于auth 模块需要注意的一件事是它使用了Tornado的异步HTTP请求。正如我们在异步Web服务() 所看到
的，异步HTTP请求允许Tornado服务器在一个挂起的请求等待传出请求返回时处理传入的请求。
我们将简单的看下如何使用异步请求，然后在一个例子中使用它们进行深入。每个发起异步调用的处理方法必须
在它前面加上@tornado.web.asynchronous 装饰器。
@tornado.web.asynchronous

7.2 示例：登录Twitter
让我们来看一个使用Twitter API验证用户的例子。这个应用将重定向一个没有登录的用户到Twitter的验证页
面，提示用户输入用户名和密码。然后Twitter会将用户重定向到你在Twitter应用设置页指定的URL。 首先，你
必须在Twitter注册一个新应用。如果你还没有应用，可以从Twitter开发者网站(https://dev.twitter.com/) 的"Cr
eate a new application"链接开始。一旦你创建了你的Twitter应用，你将被指定一个access token和一个secr
et来标识你在Twitter上的应用。你需要在本节下面代码的合适位置填充那些值。

import tornado.auth
class TwHandler(tornado.web.RequestHandler,tornado.auth.TwitterMixin):
    @tornado.web.asynchronous
    def get(self):
        oAuthToken = self.get_secure_cookie('oauth_token')
        oAuthSecret = self.get_secure_cookie('oauth_secret')
        userID = self.get_secure_cookie('user_id')

        if self.get_argument('oauth_token',None):
            self.get_authenticated_user(self.async_callback(self.__twitter_on_auth))
            return
        elif oAuth Token and oAuthSecret:
            accessToken = {
                'key': oAuthToken,
                'secret': oAuthSecret
            }
            self.twitter_request('/users/show',
                                 access_token=accessToken,
                                 user_id=userID,
                                 callback=self.async_callback(self._twitter_on_user)
                                 )
            return

第八章  部署Tornado

到目前为止，为了简单起见，在我们的例子中都是使用单一的Tornado进程运行的。这使得测试应用和快速变更
非常简单，但是这不是一个合适的部署策略。部署一个应用到生产环境面临着新的挑战，既包括最优化性能，也
包括管理独立进程。本章将介绍强化你的Tornado应用、增加请求吞吐量的策略，以及使得部署Tornado服务器
更容易的工具。

8.1
运行多个Tornado实例的原因
在大多数情况下，组合一个网页不是一个特别的计算密集型处理。服务器需要解析请求，取得适当的数据，以及
将多个组件组装起来进行响应。如果你的应用使用阻塞的调用查询数据库或访问文件系统，那么服务器将不会在
等待调用完成时响应传入的请求。在这些情况下，服务器硬件有剩余的CPU时间来等待I / O操作完成。
鉴于响应一个HTTP请求的时间大部分都花费在CPU空闲状态下，我们希望利用这个停工时间，最大化给定时间
内我们可以处理的请求数量。也就是说，我们希望服务器能够在处理已打开的请求等待数据的过程中接收尽可能
多的新请求。
正如我们在异步Web服务()
讨论的异步HTTP请求中所看到的，Tornado的非阻塞架构在解决这类问题上大有帮
助。回想一下，异步请求允许Tornado进程在等待出站请求返回时执行传入的请求。然而，我们碰到的问题是当
同步函数调用块时。设想在一个Tornado执行的数据库查询或磁盘访问块中，进程不允许回应新的请求。这个问
题最简单的解决方法是运行多个解释器的实例。通常情况下，你会使用一个反向代理，比如Nginx，来非配多个T
ornado实例的加载。

8.2
使用Nginx作为反向代理

一个代理服务器是一台中转客户端资源请求到适当的服务器的机器。一些网络安装使用代理服务器过滤或缓存本
地网络机器到Internet的HTTP请求。因为我们将运行一些在不同TCP端口上的Tornado实例，因此我们将使用
反向代理服务器：客户端通过Internet连接一个反向代理服务器，然后反向代理服务器发送请求到代理后端的Tor
nado服务器池中的任何一个主机。代理服务器被设置为对客户端透明的，但它会向上游的Tornado节点传递一些
有用信息，比如原始客户端IP地址和TCP格式。

反向代理接收所有传入的HTTP请求，然后把它们分配给独立的Tornado实
例。