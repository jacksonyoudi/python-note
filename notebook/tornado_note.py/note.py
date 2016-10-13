# coding: utf8

Tornado是一个python web框架和异步网络库,通过使用非阻塞网络I/O,tornado可以支持上万及级的连接
处理长连接，WebScokets,和其他需要与每个用户保持长久连接的应用。

import tornado.websocket
import tornado.ioloop
import tornado.iostream

ioloop.py 主要的是将底层的epoll或者说是其他的IO多路复用封装作异步事件来处理
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


tornado是一个python web框架和异步网络库，通过使用非网络IO
Tornado可以支持上万级连接，处理长连接，websocket和其他需要与每个用户保持长久连接的应用。

Tornado大体可以分为4个部分。
web框架（包括创建web应用的requestHandler类，还有很多其他的支持类）
HTTP的客户端和服务端实现（HTTPServer and AsyncHTTPClient）
异步网络库(IOLoop and IOStream),为HTTP组件提供构建模块，也可以用来实现其他协议。
协程库(tornado.gen)允许异步代码写的更直接而不用链式回调的方式

Tornado web框架和HTTP server一起为WSGI提供了一个全栈式的选择，在WSGI容器(WSGIAdapter)中使用tornado web


异步和非阻塞I/O
实时web功能需要为每个用户提供一个多数时间被闲置的长连接, 在传统的同步web服务器中，这意味着要为每个用户提供一个线程, 当然每个线程的开销都是很昂贵的.
为了尽量减少并发连接造成的开销，Tornado使用了
一种单线程事件循环的方式. 这就意味着所有的应用代码都应该是异步非阻塞的, 因为在同一时间只有一个操作是有效的.

阻塞
一个函数在等待某些事情的返回值的时候会被 阻塞.
函数被阻塞的原因有很多: 网络I/O,磁盘I/O,互斥锁等.
事实上 每个 函数在运行和使用CPU的时候都或多或少 会被阻塞
(举个极端的例子来说明为什么对待CPU阻塞要和对待一般阻塞一样的严肃:
比如密码哈希函数 bcrypt, 需要消耗几百毫秒的CPU时间,这已 经远远超过了一般的网络或者磁盘请求时间了).
一个函数可以在某些方面阻塞在另外一些方面不阻塞.例如, tornado.httpclient 在默认的配置下,会在
DNS解析上面阻塞,但是在其他网络请 求的时候不阻塞 (为了减轻这种影响，可以用 ThreadedResolver
或者是 通过正确配置 libcurl 用 tornado.curl_httpclient 来做). 在Tornado的上下文中,我们一般讨论网络I/O上下文的阻塞,尽管各种阻塞已经被最小化.

import tornado.httpclient
import tornado.curl_httpclient

异步
异步 函数在会在完成之前返回，在应用中触发下一个动作之前通常会在后 台执行一些工作
(和正常的 同步 函数在返回前就执行完所有的事情不同).这里列 举了几种风格的异步接口:

回调参数
返回一个占位符 (Future, Promise, Deferred)
传送给一个队列
回调注册表 (POSIX信号)

不论使用哪种类型的接口, 按照定义 异步函数与它们的调用者都有着不同的交互方 式;
也没有什么对调用者透明的方式使得同步函数异步(类似 gevent 使用轻量级线程的系统性能虽然堪比异步系统,但它们并 没有真正的让事情异步).


“阻塞”与"非阻塞"与"同步"与“异步"不能简单的从字面理解，提供一个从分布式系统角度的回答。
1.同步与异步
同步和异步关注的是消息通信机制 (synchronous communication/ asynchronous communication)
所谓同步，就是在发出一个*调用*时，在没有得到结果之前，该*调用*就不返回。但是一旦调用返回，就得到返回值了。
换句话说，就是由*调用者*主动等待这个*调用*的结果。

而异步则是相反，*调用*在发出之后，这个调用就直接返回了，所以没有返回结果。换句话说，当一个异步过程调用发出后，调用者不会立刻得到结果。而是在*调用*发出后，*被调用者*通过状态、通知来通知调用者，或通过回调函数处理这个调用。

典型的异步编程模型比如Node.js

举个通俗的例子：
你打电话问书店老板有没有《分布式系统》这本书，如果是同步通信机制，书店老板会说，你稍等，”我查一下"，然后开始查啊查，等查好了（可能是5秒，也可能是一天）告诉你结果（返回结果）。
而异步通信机制，书店老板直接告诉你我查一下啊，查好了打电话给你，然后直接挂电话了（不返回结果）。然后查好了，他会主动打电话给你。在这里老板通过“回电”这种方式来回调。

2. 阻塞与非阻塞
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

def asynchrous_fetch(url,callback):
    http_client = AsyncHTTPClient()
    def handle_response(response):
        callback(response.body)
    http_client.fetch(url,callback=handle_response)


使用 Future 代替回调:
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
不同于那些最多只能达到10,000个并发连接的传统网络服务器，Tornado在设
计之初就考虑到了性能因素，旨在解决C10K问题，这样的设计使得其成为一个拥有非常高性能的框架。
还拥有处理安全性、用户验证、社交网络以及与外部服务（如数据库和网站API）进行异步交互的工具。

异步服务器在这一场景中的应用相对较新，但他们正是被设计用来减轻基于线程的服务器的限制的。当负载增加
时，诸如Node.js，lighttpd和Tornodo这样的服务器使用协作的多任务的方式进行优雅的扩展。也就是说，如果
当前请求正在等待来自其他资源的数据（比如数据库查询或HTTP请求）时，一个异步服务器可以明确地控制以
挂起请求。异步服务器用来恢复暂停的操作的一个常见模式是当合适的数据准备好时调用回调函数。我们将会在
异步Web服务() 讲解回调函数模式以及一系列Tornado异步功能的应用。


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


#python hello.py --port=8000

必须导入的四个模块
import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver


tornado.options从命令行中读取设置。
Tornado包括了一个有用的模块（tornado.options）来从命令行中读取设置。我们在这里使用这个模块指定我
们的应用监听HTTP请求的端口。它的工作流程如下：如果一个与define语句中同名的设置在命令行中被给
出，那么它将成为全局options的一个属性。如果用户运行程序时使用了--help 选项，程序将打印出所有你定义
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
    app = tornado.web.Application(handlers=[(r'/',IndexHandler)])

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


从上面的代码可以看出，你可以使用RequestHandler类的set_status()方法显式地设置HTTP状态码。然
而，你需要记住在某些情况下，Tornado会自动地设置HTTP状态码。下面是一个常用情况的纲要：

404 Not Found
Tornado会在HTTP请求的路径无法匹配任何RequestHandler类相对应的模式时返回404（Not Found）响应
码。
400 Bad Request
如果你调用了一个没有默认值的get_argument函数，并且没有发现给定名称的参数，Tornado将自动返回一个
400（Bad Request）响应码。
405 Method Not Allowed
如果传入的请求使用了RequestHandler中没有定义的HTTP方法（比如，一个POST请求，但是处理函数中只
有定义了get方法），Tornado将返回一个405（Methos Not Allowed）响应码。
500 Internal Server Error
当程序遇到任何不能让其退出的错误时，Tornado将返回500（Internal Server Error）响应码。你代码中任何
没有捕获的异常也会导致500响应码。

