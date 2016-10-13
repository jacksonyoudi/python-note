# coding:utf8

flask有两个主要的依赖：路由、调试和web服务器的网关接口(WSGI)子系统有Werkzeugtigong ,模板系统由
jinja2提供。Werkzeug和jinjia2都是由Flask的核心开发者开发而成的。


from flask import Flask
app = Flask(__name__)
这里使用__name__ 决定程序的根目录


路由： 处理URL和函数之间关系的程序
在Flask程序中定义路由的最简单的反思，是使用程序实例提供的app.route修饰器，把修饰器的函数注册为路由

@app.route('/')
def index():
    return '<h1>hello world!</h1>'

这个函数的返回值称为响应，是客户端接收的内容。
像index()这样的函数称为视图函数（view function）。视图函数返回的响应可以是包含HTML的模板，或字符。


定义动态的URL
@app.route('/user/<name>')
def user(name):
    return '<h1>hello world,%s!</h1>' % name

尖括号中内容就是动态部分，任何能匹配的静态部分的URL都会映射到这个路由上，调用视图函数时，Flask会将动态
部分作为参数传入函数。

同样路由可以定义数据类型
@app.route('/user/<int:id>')
可以使用int,float,path,另外path类型也是字符串，但是把斜线当做分隔符。

2.3启动服务器

if __name__ == '__main__':
    app.run(debug=True)

服务器启动后，会进入轮询，等待并出路请求。轮询会一直运行，知道程序停止。
app.run()
def run(self, host=None, port=None, debug=None, **options):
    pass

2.5 请求-响应循环
2.5.1 请求和请求上下文

flask从客户端收到请求时，要让视图函数能够访问一些对象，这样才能处理请求。请求对象是一个很好的例子。它封装了
客户端发送的HTTP请求。

为了避免大量的可有可无的参数把视图函数弄得一团糟，flask使用上下文临时把某些对象变为全局可访问。有了上下文，就可以写出下面的视图函数。

from flask import request
@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent

注意在这个视图函数中我们如何把request 当作全局变量使用。事实上，request 不可能是
全局变量。试想，在多线程服务器中，多个线程同时处理不同客户端发送的不同请求时，
每个线程看到的request 对象必然不同。Falsk 使用上下文让特定的变量在一个线程中全局
可访问，与此同时却不会干扰其他线程。

flask使用上下文让特定的变量在一个线程中全局可访问，与此同时却不会干扰到其他线程。

线程是可单独管理的最小指令集。进程经常使用多个活动线程，有时还会共
享内存或文件句柄等资源。多线程Web 服务器会创建一个线程池，再从线
程池中选择一个线程用于处理接收到的请求。

flask有两种上下文：程序上下文和请求上下文

current_app   程序上下文  当前激活程序的程序实例
g             程序上下文  处理请求是用作临时存储对象。每次请求都会重设这个变量。
request       请求上下文  请求对象，封装了客户端发出的HTTP请求中的内容。
session       请求上下文  用户会话，用于存储请求之间需要"记住"的值的字典

Flask 在分发请求之前激活（或推送）程序和请求上下文，请求处理完成后再将其删除。程
序上下文被推送后，就可以在线程中使用current_app 和g 变量。类似地，请求上下文被
推送后，就可以使用request 和session 变量。如果使用这些变量时我们没有激活程序上
下文或请求上下文，就会导致错误

没激活程序上下文之前就调用current_app.name 会导致错误，但推送完上
下文之后就可以调用了

2.5.2请求调度

程序收到客户端发来的请求时，要找到处理该请求的视图函数。为了完成这个任务，Flask
会在程序的URL 映射中查找请求的URL。URL 映射是URL 和视图函数之间的对应关系。
Flask 使用app.route 修饰器或者非修饰器形式的app.add_url_rule() 生成映射。

@app.route()或者 app.add_url_rule()

app.url_map可以查看映射

In [8]: app.url_map
Out[8]:
Map([<Rule '/' (HEAD, OPTIONS, GET) -> index>,
 <Rule '/static/<filename>' (HEAD, OPTIONS, GET) -> static>,
 <Rule '/user/<name>' (HEAD, OPTIONS, GET) -> user>])


URL 映射中的HEAD、Options、GET 是请求方法，由路由进行处理。Flask 为每个路由都指
定了请求方法，这样不同的请求方法发送到相同的URL 上时，会使用不同的视图函数进
行处理。HEAD 和OPTIONS 方法由Flask 自动处理，因此可以这么说，在这个程序中，URL
映射中的3 个路由都使用GET 方法
REST ful

2.5.3 请求钩子
对应 Django的中间件
process_request
process_view
process_exception
process_response


有时在处理请求之前或之后执行代码会很有用。例如，在请求开始时，我们可能需要创
建数据库连接或者认证发起请求的用户。为了避免在每个视图函数中都使用重复的代码，
Flask 提供了注册通用函数的功能，注册的函数可在请求被分发到视图函数之前或之后
调用。

请求钩子使用修饰器实现。Flask 支持以下4 种钩子

before_first_request: 注册一个函数，在处理第一个请求之前运行的
before_request: 注册一个函数，在每次请求之前运行的

after_reqeust: 注册一个函数，如果没有未处理的异常抛出，在每次请求之后运行。
teardown_request:注册一个函数，即使有未处理的异常抛出，也在每次请求之后运行。

在请求钩子函数和视图函数之间共享数据一般使用上下文全局变量g。例如，before_
request 处理程序可以从数据库中加载已登录用户，并将其保存到g.user 中。随后调用视
图函数时，视图函数再使用g.user 获取用户。

2.5.4 响应

Flask 调用视图函数后，会将其返回值作为响应的内容。大多数情况下，响应就是一个简
单的字符串，作为HTML 页面回送客户端。

但HTTP 协议需要的不仅是作为请求响应的字符串。HTTP 响应中一个很重要的部分是状
态码，Flask 默认设为200，这个代码表明请求已经被成功处理。

如果视图函数返回的响应需要使用不同的状态码，那么可以把数字代码作为第二个返回
值，添加到响应文本之后。例如，下述视图函数返回一个400 状态码，表示请求无效：

@app.route('/')
def index():
    return '<h1>Bad Request</h1>', 400

视图函数返回的响应还可接受第三个参数，这是一个由首部（header）组成的字典，可以
添加到HTTP 响应中。

如果不想返回由1 个、2 个或3 个值组成的元组，Flask 视图函数还可以返回Response 对
象。make_response() 函数可接受1 个、2 个或3 个参数（和视图函数的返回值一样），并
返回一个Response 对象。有时我们需要在视图函数中进行这种转换，然后在响应对象上调
用各种方法，进一步设置响应。下例创建了一个响应对象，然后设置了cookie：
@app.route('/')
def index():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response

有一种名为重定向的特殊响应类型。这种响应没有页面文档，只告诉浏览器一个新地址用
以加载新页面。
重定向经常使用302 状态码表示，指向的地址由Location 首部提供。重定向响应可以使用
3 个值形式的返回值生成，也可在Response 对象中设定。不过，由于使用频繁，Flask 提
供了redirect() 辅助函数，用于生成这种响应：

from flask import redirect

@app.route('/'):
def index():
    return redirect('http://www.baidu.com')

还有一种特殊的响应由abort 函数生成，用于处理错误。在下面这个例子中，如果URL 中
动态参数id 对应的用户不存在，就返回状态码404：

from flask import abort

@app.route('/user/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>Hello, %s</h1>' % user.name
注意，abort 不会把控制权交还给调用它的函数，而是抛出异常把控制权交给Web 服
务器。

2.6 Flask扩展

Flask 被设计为可扩展形式，故而没有提供一些重要的功能，例如数据库和用户认证，所
以开发者可以自由选择最适合程序的包，或者按需求自行开发。
社区成员开发了大量不同用途的扩展，如果这还不能满足需求，你还可使用所有Python 标
准包或代码库。为了让你知道如何把扩展整合到程序中，接下来我们将在hello.py 中添加
一个扩展，使用命令行参数增强程序的功能。

使用Flask-Script支持命令行选项

Flask 的开发Web 服务器支持很多启动设置选项，但只能在脚本中作为参数传给app.run()
函数。这种方式并不十分方便，传递设置选项的理想方式是使用命令行参数。

Flask-Script 是一个Flask 扩展，为Flask 程序添加了一个命令行解析器。Flask-Script 自带
了一组常用选项，而且还支持自定义命令。

pip install flask-script


from flask.ext.script import Manager
manager = Manager(app)

if __name__ == '__main__':
    manager.run()
专为Flask 开发的扩展都暴漏在flask.ext 命名空间下。Flask-Script 输出了一个名为
Manager 的类，可从flask.ext.script 中引入。

这个扩展的初始化方法也适用于其他很多扩展：把程序实例作为参数传给构造函数，初始
化主类的实例。创建的对象可以在各个扩展中使用。在这里，服务器由manager.run() 启
动，启动后就能解析命令行了。
(venv) $ python hello.py runserver --help
usage: hello.py runserver [-h] [-t HOST] [-p PORT] [--threaded]
[--processes PROCESSES] [--passthrough-errors] [-d]
[-r]

运行Flask 开发服务器：app.run()
optional arguments:
-h, --help 显示帮助信息并退出
-t HOST, --host HOST
-p PORT, --port PORT
--threaded
--processes PROCESSES
--passthrough-errors
-d, --no-debug
-r, --no-reload

--host 参数是个很有用的选项，它告诉Web 服务器在哪个网络接口上监听来自客户端的
连接。默认情况下，Flask 开发Web 服务器监听localhost 上的连接，所以只接受来自服
务器所在计算机发起的连接。下述命令让Web 服务器监听公共网络接口上的连接，允许同
网中的其他计算机连接服务器：
(venv) $ python hello.py runserver --host 0.0.0.0
* Running on http://0.0.0.0:5000/
* Restarting with reloader


第三章 模板

业务逻辑和表现逻辑
业务逻辑在后台
表现逻辑要展示到前端

把业务逻辑和表现逻辑混在一起会导致代码难以理解和维护。假设要为一个大型表格构建
HTML 代码，表格中的数据由数据库中读取的数据以及必要的HTML 字符串连接在一起。
把表现逻辑移到模板中能够提升程序的可维护性。

模板是一个包含响应文本的文件，其中包含用占位变量表示的动态部分，其具体值只在请
求的上下文中才能知道。使用真实值替换变量，再返回最终得到的响应字符串，这一过程
称为渲染。为了渲染模板，Flask 使用了一个名为Jinja2 的强大模板引擎。

使用真实值替换变量，再返回最终得到的响应字符串，这一过程称为渲染。

3.1 Jinja2模板引擎
形式最简单的Jinja2 模板就是一个包含响应文本的文件。示例3-1 是一个Jinja2 模板，它
和示例2-1 中index() 视图函数的响应一样。

示例3-1　templates/index.html：Jinja2 模板
<h1>Hello World!</h1>

示例3-2　 templates/user.html：Jinja2 模板
<h1>Hello, {{ name }}!</h1>


3.1.1 渲染模板
默认情况下，Flask 在程序文件夹中的templates 子文件夹中寻找模板。在下一个hello.py
版本中，要把前面定义的模板保存在templates 文件夹中，并分别命名为index.html 和user.
html。

# coding: utf8
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)


if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')

Flask 提供的render_template 函数把Jinja2 模板引擎集成到了程序中。render_template 函
数的第一个参数是模板的文件名。随后的参数都是键值对，表示模板中变量对应的真实
值。在这段代码中，第二个模板收到一个名为name 的变量。

前例中的name=name 是关键字参数，这类关键字参数很常见，但如果你不熟悉它们的话，
可能会觉得迷惑且难以理解。左边的“name”表示参数名，就是模板中使用的占位符；右
边的“name”是当前作用域中的变量，表示同名参数的值。

3.1.2 变量
在模板中使用的{{ name }} 结构表示一个变量，它是一种特殊的占位符，告诉模
板引擎这个位置的值从渲染模板时使用的数据中获取。

Jinja2 能识别所有类型的变量，甚至是一些复杂的类型，例如列表、字典和对象。在模板
中使用变量的一些示例如下：

<p>A value from a dictionary: {{ mydict['key'] }}.</p>
<p>A value from a list: {{ mylist[3] }}.</p>
<p>A value from a list, with a variable index: {{ mylist[myintvar] }}.</p>
<p>A value from an object method: {{ myobj.somemethod() }}.</p>

{{ dict['key'] }}
{{ list['index_count'] }}
{{ mylist[myintvar] }}
{{ myobj.somethod() }}

可以使用过滤器修改变量，过滤器名添加在变量名之后，中间使用竖线分隔。例如，下述
模板以首字母大写形式显示变量name 的值：
Hello, {{ name|capitalize }}

Jinja2变量过滤器
safe       渲染值时不转义
capitlize  把值的首字母转换成大写，其他字母转换成小写
lower      把值的转换成小写
upper      把值转换成大写
title      把值中的单词的首字母大写
trim       把值的首尾空格去掉
stringtags 渲染之前把值中所有的HTML标签都去掉

safe 过滤器值得特别说明一下。默认情况下，出于安全考虑，Jinja2 会转义所有变量。例
如，如果一个变量的值为'<h1>Hello</h1>'，Jinja2 会将其渲染成'&lt;h1&gt;Hello&lt;/
h1&gt;'，浏览器能显示这个h1 元素，但不会进行解释。很多情况下需要显示变量中存储
的HTML 代码，这时就可使用safe 过滤器。

3.1.3 控制结构
Jinja2 提供了多种控制结构，可用来改变模板的渲染流程。本节使用简单的例子介绍其中
最有用的控制结构。

{% if user %}
    hello,{{ user }}
{% else %}
    hello,Stranger!
{% endif %}

另一种常见需求是在模板中渲染一组元素。下例展示了如何使用for 循环实现这一需求：

<ul>
{% for comnet in comments %}
    <li>{{  comment }}</li>
{% endif %}
</ul>

Jinja2 还支持宏。宏类似于Python 代码中的函数。例如：

{% macro render_comment(comment) %}
<li>{{ comment }}</li>
{% endmacro %}

<ul>
{% for comment in comments %}
    {{ render_comment(comment) }}
{% endfor %}
</ul>

为了重复使用宏，我们可以将其保存在单独的文件中，然后在需要使用的模板中导入：
{% import 'macros.html' as macros %}
<ul>
{% for comment in comments %}
{{ macros.render_comment(comment) }}
{% endfor %}
</ul>

需要在多处重复使用的模板代码片段可以写入单独的文件，再包含在所有模板中，以避免
重复：
{% include 'common.html' %}

另一种重复使用代码的强大方式是模板继承，它类似于Python 代码中的类继承。首先，创
建一个名为base.html 的基模板：
模板 ｜ 23
<html>
<head>
{% block head %}
<title>{% block title %}{% endblock %} - My Application</title>
{% endblock %}
</head>
<body>
{% block body %}
{% endblock %}
</body>
</html>

block 标签定义的元素可在衍生模板中修改。在本例中，我们定义了名为head、title 和
body 的块。注意，title 包含在head 中。下面这个示例是基模板的衍生模板：

{% extends "base.html" %}
{% block title %}Index{% endblock %}
{% block head %}
{{ super() }}
<style>
</style>
{% endblock %}
{% block body %}
<h1>Hello, World!</h1>
{% endblock %}
extends 指令声明这个模板衍生自base.html。在extends 指令之后，基模板中的3 个块被
重新定义，模板引擎会将其插入适当的位置。注意新定义的head 块，在基模板中其内容不
是空的，所以使用super() 获取原来的内容。

3.2　使用Flask-Bootstrap集成Twitter Bootstrap
Bootstrap（http://getbootstrap.com/）是Twitter 开发的一个开源框架，它提供的用户界面组
件可用于创建整洁且具有吸引力的网页，而且这些网页还能兼容所有现代Web 浏览器。

Bootstrap 是客户端框架，因此不会直接涉及服务器。服务器需要做的只是提供引用了
Bootstrap 层叠样式表（CSS） 和JavaScript 文件的HTML 响应， 并在HTML、CSS 和
JavaScript 代码中实例化所需组件。这些操作最理想的执行场所就是模板。

要想在程序中集成Bootstrap，显然要对模板做所有必要的改动。不过，更简单的方法是
使用一个名为Flask-Bootstrap 的Flask 扩展，简化集成的过程。Flask-Bootstrap 使用pip
安装：
pip install flask-bootstrap

　hello.py：初始化Flask-Bootstrap
from flask.ext.bootstrap import Bootstrap
# ...
bootstrap = Bootstrap(app)
和第2 章中的Flask-Script 一样，Flask-Bootstrap 也从flask.ext 命名空间中导入，然后把
程序实例传入构造方法进行初始化。
初始化Flask-Bootstrap 之后，就可以在程序中使用一个包含所有Bootstrap 文件的基模板。
这个模板利用Jinja2 的模板继承机制，让程序扩展一个具有基本页面结构的基模板，其中
就有用来引入Bootstrap 的元素。示例3-5 是把user.html 改写为衍生模板后的新版本。

{% extends "bootstrap/base.html" %}
{% block title %}Flasky{% endblock %}
{% block navbar %}
<div class="navbar navbar-inverse" role="navigation">
<div class="container">
<div class="navbar-header">
<button type="button" class="navbar-toggle"
data-toggle="collapse" data-target=".navbar-collapse">
<span class="sr-only">Toggle navigation</span>
<span class="icon-bar"></span>
<span class="icon-bar"></span>
<span class="icon-bar"></span>
</button>
<a class="navbar-brand" href="/">Flasky</a>
</div>
<div class="navbar-collapse collapse">
<ul class="nav navbar-nav">
<li><a href="/">Home</a></li>
    </ul>
</div>
</div>
</div>
{% endblock %}
{% block content %}
<div class="container">
<div class="page-header">
<h1>Hello, {{ name }}!</h1>
</div>
</div>
{% endblock %}

Jinja2 中的extends 指令从Flask-Bootstrap 中导入bootstrap/base.html， 从而实现模板继
承。Flask-Bootstrap 中的基模板提供了一个网页框架，引入了Bootstrap 中的所有CSS 和
模板 ｜ 25
JavaScript 文件。
基模板中定义了可在衍生模板中重定义的块。block 和endblock 指令定义的块中的内容可
添加到基模板中。

上面这个user.html 模板定义了3 个块，分别名为title、navbar 和content。这些块都是
基模板提供的，可在衍生模板中重新定义。title 块的作用很明显，其中的内容会出现在
渲染后的HTML 文档头部，放在<title> 标签中。navbar 和content 这两个块分别表示页
面中的导航条和主体内容。

在这个模板中，navbar 块使用Bootstrap 组件定义了一个简单的导航条。content 块中有个
<div> 容器，其中包含一个页面头部。之前版本的模板中的欢迎信息，现在就放在这个页
面头部。

Flask-Bootstrap 的base.html 模板还定义了很多其他块，都可在衍生模板中使用。
Flask-Bootstrap基模板中定义的块
块名              说明
doc              整个HTML文档
html_attribs     <html>标签属性
html             <html>标签的内容
head             <head>标签中的内容
title            <title>标签中内容
metas           一组<meta> 标签
styles          层叠样式表定义
body_attribs    <body> 标签的属性
body            <body> 标签中的内容
navbar          用户定义的导航条
content         用户定义的页面内容
scripts         文档底部的JavaScript 声明


表3-2 中的很多块都是Flask-Bootstrap 自用的，如果直接重定义可能会导致一些问题。例
如，Bootstrap 所需的文件在styles 和scripts 块中声明。如果程序需要向已经有内容的块
中添加新内容，必须使用Jinja2 提供的super() 函数。例如，如果要在衍生模板中添加新
的JavaScript 文件，需要这么定义scripts 块：

{% block scripts %}
{{ super() }}
<script type="text/javascript" src="my-script.js"></script>
{% endblock %}


3.3 自定义错误页面

像常规路由一样，Flask 允许程序使用基于模板的自定义错误页面。最常见的错误代码有
两个：404，客户端请求未知页面或路由时显示；500，有未处理的异常时显示。
@app.errorhandler(404)
def page_not_found(e):
return render_template('404.html'), 404
@app.errorhandler(500)
def internal_server_error(e):
return render_template('500.html'), 500

和视图函数一样，错误处理程序也会返回响应。它们还返回与该错误对应的数字状态码。
错误处理程序中引用的模板也需要编写。这些模板应该和常规页面使用相同的布局，因此
要有一个导航条和显示错误消息的页面头部。
编写这些模板最直观的方法是复制templates/user.html，分别创建templates/404.html 和
templates/500.html，然后把这两个文件中的页面头部元素改为相应的错误消息。但这种方
法会带来很多重复劳动。

Jinja2 的模板继承机制可以帮助我们解决这一问题。Flask-Bootstrap 提供了一个具有页面基
本布局的基模板，同样，程序可以定义一个具有更完整页面布局的基模板，其中包含导航
条，而页面内容则可留到衍生模板中定义。示例3-7 展示了templates/base.html 的内容，这
是一个继承自bootstrap/base.html 的新模板，其中定义了导航条。这个模板本身也可作为其
他模板的基模板，例如templates/user.html、templates/404.html 和templates/500.html。

{% extends "bootstrap/base.html" %}
{% block title %}Flasky{% endblock %}
{% block navbar %}
<div class="navbar navbar-inverse" role="navigation">
<div class="container">
<div class="navbar-header">
<button type="button" class="navbar-toggle"
data-toggle="collapse" data-target=".navbar-collapse">
<span class="sr-only">Toggle navigation</span>
<span class="icon-bar"></span>
<span class="icon-bar"></span>
<span class="icon-bar"></span>
</button>
<a class="navbar-brand" href="/">Flasky</a>
</div>
<div class="navbar-collapse collapse">
<ul class="nav navbar-nav">
<li><a href="/">Home</a></li>
</ul>
</div>
</div>
</div>
{% endblock %}
{% block content %}
<div class="container">
{% block page_content %}{% endblock %}
</div>
{% endblock %}
这个模板的content 块中只有一个<div> 容器，其中包含了一个名为page_content 的新的
空块，块中的内容由衍生模板定义。
现在，程序使用的模板继承自这个模板，而不直接继承自Flask-Bootstrap 的基模板。通过
继承templates/base.html 模板编写自定义的404 错误页面很简单，

　templates/user.html：使用模板继承机制简化页面模板
{% extends "base.html" %}
{% block title %}Flasky{% endblock %}
{% block page_content %}
<div class="page-header">
<h1>Hello, {{ name }}!</h1>
</div>
{% endblock %}

3.4　链接
任何具有多个路由的程序都需要可以连接不同页面的链接，例如导航条。
在模板中直接编写简单路由的URL 链接不难，但对于包含可变部分的动态路由，在模板
中构建正确的URL 就很困难。而且，直接编写URL 会对代码中定义的路由产生不必要的
依赖关系。如果重新定义路由，模板中的链接可能会失效。
为了避免这些问题，Flask 提供了url_for() 辅助函数，它可以使用程序URL 映射中保存
的信息生成URL。
url_for() 函数最简单的用法是以视图函数名（或者app.add_url_route() 定义路由时使用
的端点名）作为参数，返回对应的URL。例如，在当前版本的hello.py 程序中调用url_
for('index') 得到的结果是/。调用url_for('index', _external=True) 返回的则是绝对地
址，在这个示例中是http://localhost:5000/。

生成连接程序内不同路由的链接时，使用相对地址就足够了。如果要生成在
浏览器之外使用的链接，则必须使用绝对地址，例如在电子邮件中发送的
链接。

使用url_for() 生成动态地址时， 将动态部分作为关键字参数传入。例如，url_for
('user', name='john', _external=True) 的返回结果是http://localhost:5000/user/john。

url_for('view_func_name',_external=True)
传入url_for() 的关键字参数不仅限于动态路由中的参数。函数能将任何额外参数添加到
查询字符串中。例如，url_for('index', page=2) 的返回结果是/?page=2。

3.5　静态文件

Web 程序不是仅由Python 代码和模板组成。大多数程序还会使用静态文件，例如HTML
代码中引用的图片、JavaScript 源码文件和CSS。

你可能还记得在第2 章中检查hello.py 程序的URL 映射时，其中有一个static 路由。
这是因为对静态文件的引用被当成一个特殊的路由，即/static/<filename>。例如，调用
url_for('static', filename='css/styles.css', _external=True) 得到的结果是http://
localhost:5000/static/css/styles.css。

默认设置下，Flask 在程序根目录中名为static 的子目录中寻找静态文件。如果需要，可在
static 文件夹中使用子文件夹存放文件。服务器收到前面那个URL 后，会生成一个响应，
包含文件系统中static/css/styles.css 文件的内容。

　templates/base.html：定义收藏夹图标
{% block head %}
{{ super() }}
<link rel="shortcut icon" href="{{ url_for('static', filename = 'favicon.ico') }}"
type="image/x-icon">
<link rel="icon" href="{{ url_for('static', filename = 'favicon.ico') }}"
type="image/x-icon">
{% endblock %}
图标的声明会插入head 块的末尾。注意如何使用super() 保留基模板中定义的块的原始
内容。

3.6　使用Flask-Moment本地化日期和时间
如果Web 程序的用户来自世界各地，那么处理日期和时间可不是一个简单的任务。
服务器需要统一时间单位，这和用户所在的地理位置无关，所以一般使用协调世界时
（Coordinated Universal Time，UTC）。不过用户看到UTC 格式的时间会感到困惑，他们更
希望看到当地时间，而且采用当地惯用的格式。
要想在服务器上只使用UTC 时间，一个优雅的解决方案是，把时间单位发送给Web 浏览
器，转换成当地时间，然后渲染。Web 浏览器可以更好地完成这一任务，因为它能获取用
户电脑中的时区和区域设置。

有一个使用JavaScript 开发的优秀客户端开源代码库，名为moment.js（http://momentjs.
com/），它可以在浏览器中渲染日期和时间。Flask-Moment 是一个Flask 程序扩展，能把
moment.js 集成到Jinja2 模板中。Flask-Moment 可以使用pip 安装：
(venv) $ pip install flask-moment
这个扩展的初始化方法如示例3-11 所示。
　hello.py：初始化Flask-Moment
from flask.ext.moment import Moment
moment = Moment(app)
模板 ｜ 31
除了moment.js，Flask-Moment 还依赖jquery.js。要在HTML 文档的某个地方引入这两个
库，可以直接引入，这样可以选择使用哪个版本，也可使用扩展提供的辅助函数，从内容
分发网络（Content Delivery Network，CDN）中引入通过测试的版本。Bootstrap 已经引入
了jquery.js，因此只需引入moment.js 即可。示例3-12 展示了如何在基模板的scripts 块
中引入这个库。
templates/base.html：引入moment.js 库
{% block scripts %}
{{ super() }}
{{ moment.include_moment() }}
{% endblock %}
为了处理时间戳，Flask-Moment 向模板开放了moment 类。示例3-13 中的代码把变量
current_time 传入模板进行渲染。

from datetime import datetime
@app.route('/')
def index():
return render_template('index.html',
current_time=datetime.utcnow())

　templates/index.html：使用Flask-Moment 渲染时间戳
<p>The local date and time is {{ moment(current_time).format('LLL') }}.</p>
<p>That was {{ moment(current_time).fromNow(refresh=True) }}</p>
format('LLL') 根据客户端电脑中的时区和区域设置渲染日期和时间。参数决定了渲染的方
式，'L' 到'LLLL' 分别对应不同的复杂度。format() 函数还可接受自定义的格式说明符。
第二行中的fromNow() 渲染相对时间戳，而且会随着时间的推移自动刷新显示的时间。这
个时间戳最开始显示为“a few seconds ago”，但指定refresh 参数后，其内容会随着时
间的推移而更新。如果一直待在这个页面，几分钟后，会看到显示的文本变成“a minute
ago”“2 minutes ago”等。

Flask-Monet 假定服务器端程序处理的时间戳是“纯正的”datetime 对象，
且使用UTC 表示。关于纯正和细致的日期和时间对象1 的说明，

Flask-Moment 渲染的时间戳可实现多种语言的本地化。语言可在模板中选择，把语言代码
传给lang() 函数即可：
{{ moment.lang('es') }}

第四章 web表单
请求对象包含客户端发出的所有请求信息。其中，request.form 能获取
POST 请求中提交的表单数据。
尽管Flask 的请求对象提供的信息足够用于处理Web 表单，但有些任务很单调，而且要重
复操作。比如，生成表单的HTML 代码和验证提交的表单数据。

Flask-WTF（http://pythonhosted.org/Flask-WTF/）扩展可以把处理Web 表单的过程变成一
种愉悦的体验。这个扩展对独立的WTForms（http://wtforms.simplecodes.com）包进行了包
装，方便集成到Flask 程序中。
Flask-WTF 及其依赖可使用pip 安装：
(venv) $ pip install flask-wtf

4.1　跨站请求伪造保护
第一次或者不信任的用户post数据到网站。


默认情况下，Flask-WTF 能保护所有表单免受跨站请求伪造（Cross-Site Request Forgery，
CSRF）的攻击。恶意网站把请求发送到被攻击者已登录的其他网站时就会引发CSRF 攻击。

为了实现CSRF 保护，Flask-WTF 需要程序设置一个密钥。Flask-WTF 使用这个密钥生成
加密令牌，再用令牌验证请求中表单数据的真伪。设置密钥的方法如示例4-1 所示。

示例4-1　hello.py：设置Flask-WTF
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

app.config 字典可用来存储框架、扩展和程序本身的配置变量。使用标准的字典句法就能
把配置值添加到app.config 对象中。这个对象还提供了一些方法，可以从文件或环境中导
入配置值。

SECRET_KEY 配置变量是通用密钥，可在Flask 和多个第三方扩展中使用。如其名所示，加
密的强度取决于变量值的机密程度。不同的程序要使用不同的密钥，而且要保证其他人不
知道你所用的字符串。


4.2　表单类

使用Flask-WTF 时，每个Web 表单都由一个继承自Form 的类表示。这个类定义表单中的
一组字段，每个字段都用对象表示。字段对象可附属一个或多个验证函数。验证函数用来
验证用户提交的输入值是否符合要求。

示例4-2 是一个简单的Web 表单，包含一个文本字段和一个提交按钮。

示例4-2　hello.py：定义表单类
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')

这个表单中的字段都定义为类变量，类变量的值是相应字段类型的对象。在这个示例中，
NameForm 表单中有一个名为name 的文本字段和一个名为submit 的提交按钮。StringField
类表示属性为type="text" 的<input> 元素。SubmitField 类表示属性为type="submit" 的
<input> 元素。字段构造函数的第一个参数是把表单渲染成HTML 时使用的标号。


StringField 构造函数中的可选参数validators 指定一个由验证函数组成的列表，在接受
用户提交的数据之前验证数据。验证函数Required() 确保提交的字段不为空。

Form 基类由Flask-WTF 扩展定义，所以从flask.ext.wtf 中导入。字段和验
证函数却可以直接从WTForms 包中导入。

WTForms支持的HTML标准字段
字段类型                 说　　明
StringField             文本字段
TextAreaField           多行文本字段
PasswordField           密码文本字段
HiddenField             隐藏文本字段
DateField               文本字段，值为datetime.date 格式
DateTimeField           文本字段，值为datetime.datetime 格式
IntegerField            文本字段，值为整数
DecimalField            文本字段，值为decimal.Decimal
FloatField              文本字段，值为浮点数
BooleanField            复选框，值为True 和False
RadioField              一组单选框
SelectField             下拉列表
SelectMultipleField     下拉列表，可选择多个值
FileField               文件上传字段
SubmitField             表单提交按钮
FormField               把表单作为字段嵌入另一个表单
FieldList               一组指定类型的字段

表4-2　WTForms验证函数
验证函数                 说　　明
Email                   验证电子邮件地址
EqualTo                 比较两个字段的值；常用于要求输入两次密码进行确认的情况
IPAddress               验证IPv4 网络地址
Length                  验证输入字符串的长度
NumberRange             验证输入的值在数字范围内
Optional                无输入值时跳过其他验证函数
Required                确保字段中有数据
Regexp                  使用正则表达式验证输入值
URL                     验证URL
AnyOf                   确保输入值在可选值列表中
NoneOf                  确保输入值不在可选值列表中

4.3 把表单渲染成HTMl
表单字段是可调用的，在模板中调用后会渲染成HTML。假设视图函数把一个NameForm 实
例通过参数form 传入模板，在模板中可以生成一个简单的表单，如下所示：
<form method="POST">
{{ form.hidden_tag() }}
{{ form.name.label }} {{ form.name() }}
{{ form.submit() }}
</form>
当然，这个表单还很简陋。要想改进表单的外观，可以把参数传入渲染字段的函数，传入
的参数会被转换成字段的HTML 属性。
例如，可以为字段指定id 或class 属性，然后定
义CSS 样式：

<form method="POST">
{{ form.hidden_tag() }}
{{ form.name.label }} {{ form.name(id='my-text-field') }}
{{ form.submit() }}
</form>

即便能指定HTML 属性，但按照这种方式渲染表单的工作量还是很大，所以在条件允许的
情况下最好能使用Bootstrap 中的表单样式。Flask-Bootstrap 提供了一个非常高端的辅助函
数，可以使用Bootstrap 中预先定义好的表单样式渲染整个Flask-WTF 表单，而这些操作
只需一次调用即可完成。使用Flask-Bootstrap，上述表单可使用下面的方式渲染：

{% import "bootstrap/wtf.html" as wtf %}
{{ wtf.quick_form(form) }}
import 指令的使用方法和普通Python 代码一样，允许导入模板中的元素并用在多个模板
中。导入的bootstrap/wtf.html 文件中定义了一个使用Bootstrap 渲染Falsk-WTF 表单对象
的辅助函数。wtf.quick_form() 函数的参数为Flask-WTF 表单对象，使用Bootstrap 的默认
样式渲染传入的表单

{% extends "base.html" %}
{% import "bootstrap/wtf.html" as wtf %}
{% block title %}Flasky{% endblock %}
{% block page_content %}
<div class="page-header">
<h1>Hello, {% if name %}{{ name }}{% else %}Stranger{% endif %}!</h1>
</div>
{{ wtf.quick_form(form) }}
{% endblock %}

内容区的第二部分使用wtf.quick_form() 函数渲染NameForm 对象。

4.4　在视图函数中处理表单
视图函数index() 不仅要渲染表单，还要接收表单中的数据
@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html', form=form, name=name)
app.route 修饰器中添加的methods 参数告诉Flask 在URL 映射中把这个视图函数注册为
GET 和POST 请求的处理程序。如果没指定methods 参数，就只把视图函数注册为GET 请求
的处理程序。

把POST 加入方法列表很有必要，因为将提交表单作为POST 请求进行处理更加便利。表单
也可作为GET 请求提交，不过GET 请求没有主体，提交的数据以查询字符串的形式附加到
URL 中，可在浏览器的地址栏中看到。基于这个以及其他多个原因，提交表单大都作为
POST 请求进行处理。

局部变量name 用来存放表单中输入的有效名字，如果没有输入，其值为None。如上述代
码所示，在视图函数中创建一个NameForm 类实例用于表示表单。提交表单后，如果数据能
被所有验证函数接受，那么validate_on_submit() 方法的返回值为True，否则返回False。
这个函数的返回值决定是重新渲染表单还是处理表单提交的数据。

validate_on_submit() 验证表单是否合法
用户第一次访问程序时，服务器会收到一个没有表单数据的GET 请求，所以validate_on_
submit() 将返回False。if 语句的内容将被跳过，通过渲染模板处理请求，并传入表单对
象和值为None 的name 变量作为参数。用户会看到浏览器中显示了一个表单。

用户提交表单后，服务器收到一个包含数据的POST 请求。validate_on_submit() 会调用
name 字段上附属的Required() 验证函数。

4.5　重定向和用户会话

最新版的hello.py 存在一个可用性问题。用户输入名字后提交表单，然后点击浏览器的刷
新按钮，会看到一个莫名其妙的警告，要求在再次提交表单之前进行确认。之所以出现这
种情况，是因为刷新页面时浏览器会重新发送之前已经发送过的最后一个请求。如果这个
请求是一个包含表单数据的POST 请求，刷新页面后会再次提交表单。大多数情况下，这并
不是理想的处理方式。

很多用户都不理解浏览器发出的这个警告。基于这个原因，最好别让Web 程序把POST 请
求作为浏览器发送的最后一个请求。

这种需求的实现方式是，使用重定向作为POST 请求的响应，而不是使用常规响应。重定
向是一种特殊的响应，响应内容是URL，而不是包含HTML 代码的字符串。浏览器收到
这种响应时，会向重定向的URL 发起GET 请求，显示页面的内容。这个页面的加载可能
要多花几微秒，因为要先把第二个请求发给服务器。除此之外，用户不会察觉到有什么不
同。现在，最后一个请求是GET 请求，所以刷新命令能像预期的那样正常使用了。这个技
巧称为Post/ 重定向/Get 模式

POST/重定向/GET模式

但这种方法会带来另一个问题。程序处理POST 请求时，使用form.name.data 获取用户输
入的名字，可是一旦这个请求结束，数据也就丢失了。因为这个POST 请求使用重定向处
理，所以程序需要保存输入的名字，这样重定向后的请求才能获得并使用这个名字，从而
构建真正的响应。

程序可以把数据存储在用户会话中，在请求之间“记住”数据。用户会话是一种私有存
储，存在于每个连接到服务器的客户端中。我们在第2 章介绍过用户会话，它是请求上下
文中的变量，名为session，像标准的Python 字典一样操作。


默认情况下，用户会话保存在客户端cookie 中，使用设置的SECRET_KEY 进
行加密签名。如果篡改了cookie 中的内容，签名就会失效，会话也会随之
失效。

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))


如果get，form.validate_on_submit()为Flase，执行return render_template('index.html', form=form, name=session['name'])
如果是post，redirect---->get--->seesion['name']有值


4.6 Flask消息
请求完成后，有时需要让用户知道状态发生了变化。这里可以使用确认消息、警告或者错
误提醒。一个典型例子是，用户提交了有一项错误的登录表单后，服务器发回的响应重新
渲染了登录表单，并在表单上面显示一个消息，提示用户用户名或密码错误。

@app.route('/', methods=['get', 'post'])
def index():
    form = NameForm()
    old_name = session.get('name')
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have change you name!')
            seesion['name'] = form.name.data
            return redirect(url_for('index'))
        return render_template('index.html', form=form, name=session.get('name'))

在这个示例中，每次提交的名字都会和存储在用户会话中的名字进行比较，而会话中存储
的名字是前一次在这个表单中提交的数据。如果两个名字不一样，就会调用flash() 函数，
在发给客户端的下一个响应中显示一个消息。
仅调用flash() 函数并不能把消息显示出来，程序使用的模板要渲染这些消息。最好在
基模板中渲染Flash 消息，因为这样所有页面都能使用这些消息。Flask 把get_flashed_
messages() 函数开放给模板，用来获取并渲染消息，

get_flashed_messages()

{% for message in get_flashed_messages() %}
<div class="alert alert-warning">
<button type="button" class="close" data-dismiss="alert">&times;</button>
{{ message }}
</div>
{% endfor %}

在模板中使用循环是因为在之前的请求循环中每次调用flash() 函数时都会生成一个消息，
所以可能有多个消息在排队等待显示。get_flashed_messages() 函数获取的消息在下次调
用时不会再次返回，因此Flash 消息只显示一次，然后就消失了。


第5章  数据库

数据库按照一定规则保存程序数据，程序再发起查询取回所需的数据。Web 程序最常用基
于关系模型的数据库，这种数据库也称为SQL 数据库，因为它们使用结构化查询语言。不
过最近几年文档数据库和键值对数据库成了流行的替代选择，这两种数据库合称NoSQL

5.1　SQL数据库

表中有个特殊的列，称为主键，其值为表中各行的唯一标识符。表中还可以有称为外键的
列，引用同一个表或不同表中某行的主键。行之间的这种联系称为关系，这是关系型数据
库模型的基础。

从这个例子可以看出，关系型数据库存储数据很高效，而且避免了重复。将这个数据库中
的用户角色重命名也很简单，因为角色名只出现在一个地方。一旦在roles 表中修改完角
色名，所有通过role_id 引用这个角色的用户都能立即看到更新。

所有不遵循上节所述的关系模型的数据库统称为NoSQL 数据库。NoSQL 数据库一般使用
集合代替表，使用文档代替记录。NoSQL 数据库采用的设计方式使联结变得困难，所以大
多数数据库根本不支持这种操作。对于结构如图5-1 所示的NoSQL 数据库，若要列出各
用户及其角色，就需要在程序中执行联结操作，即先读取每个用户的role_id，再在roles
表中搜索对应的记录

易用性
如果直接比较数据库引擎和数据库抽象层，显然后者取胜。抽象层，也称为对象关系
映射（Object-Relational Mapper，ORM） 或对象文档映射（Object-Document Mapper，
ODM），在用户不知觉的情况下把高层的面向对象操作转换成低层的数据库指令。

性能
ORM 和ODM 把对象业务转换成数据库业务会有一定的损耗。大多数情况下，这种性
能的降低微不足道，但也不一定都是如此。一般情况下，ORM 和ODM 对生产率的提
升远远超过了这一丁点儿的性能降低，所以性能降低这个理由不足以说服用户完全放弃
ORM 和ODM。真正的关键点在于如何选择一个能直接操作低层数据库的抽象层，以
防特定的操作需要直接使用数据库原生指令优化。

。SQLAlchemy ORM 就是一个很好的例子，它支持很多关系型数据库引擎，包
括流行的MySQL、Postgres 和SQLite。

FLask集成度
选择框架时，你不一定非得选择已经集成了Flask 的框架，但选择这些框架可以节省
你编写集成代码的时间。使用集成了Flask 的框架可以简化配置和操作，所以专门为
Flask 开发的扩展是你的首选。

5.5　使用Flask-SQLAlchemy管理数据库

Flask-SQLAlchemy 是一个Flask 扩展，简化了在Flask 程序中使用SQLAlchemy 的操作。
SQLAlchemy 是一个很强大的关系型数据库框架，支持多种数据库后台。SQLAlchemy 提
供了高层ORM，也提供了使用数据库原生SQL 的低层功能。

FLask-SQLAlchemy数据库URL
数据库引擎URL
MySQL mysql://username:password@hostname/database
Postgres postgresql://username:password@hostname/database
SQLite（Unix） sqlite:////absolute/path/to/database
SQLite（Windows） sqlite:///c:/absolute/path/to/database

SQLite 数据库不需要使用服务器，因此不用指定hostname、username 和
password。URL 中的database 是硬盘上文件的文件名。

程序使用的数据库URL 必须保存到Flask 配置对象的SQLALCHEMY_DATABASE_URI 键中。配
置对象中还有一个很有用的选项，即SQLALCHEMY_COMMIT_ON_TEARDOWN 键，将其设为True
时，每次请求结束后都会自动提交数据库中的变动。其他配置选项的作用请参阅Flask-
SQLAlchemy 的文档。示例5-1 展示了如何初始化及配置一个简单的SQLite 数据库。


# coding:utf8
from flask.ext.sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

db 对象是SQLAlchemy 类的实例，表示程序使用的数据库，同时还获得了Flask-SQLAlchemy
提供的所有功能。

5.6 定义模型

模型这个术语表示程序使用的持久化实体。在ORM 中，模型一般是一个Python 类，类中
的属性对应数据库表中的列。

Flask-SQLAlchemy 创建的数据库实例为模型提供了一个基类以及一系列辅助类和辅助函
数，可用于定义模型的结构。图5-1 中的roles 表和users 表可定义为模型Role 和User，

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)

    def __repr__(self):
        return '<User %r>' % self.username

类变量__tablename__ 定义在数据库中使用的表名。如果没有定义__tablename__，Flask-SQLAlchemy
会使用一个默认名字，但默认的表名没有遵守使用复数形式进行命名的约定所以最好由我们自己来指定表名。其余的类变量都是该模型的属性，被定义为db.Column
类的实例。

db.Column 类构造函数的第一个参数是数据库列和模型属性的类型

最常用的SQLAlchemy列类型
类型名             Python类型              说　　明
Integer             int                 普通整数，一般是32 位
SmallInteger        int                 取值范围小的整数，一般是16 位
BigInteger          int                 或long 不限制精度的整数
Float               float               浮点数
Numeric             decimal.Decimal     定点数
String              str                 变长字符串
Text                str                 变长字符串，对较长或不限长度的字符串做了优化
Unicode             unicode             变长Unicode 字符串
UnicodeText         unicode             变长Unicode 字符串，对较长或不限长度的字符串做了优化
Boolean             bool                布尔值
Date                datetime.date       日期
Time                datetime.time       时间
DateTime            datetime.datetime   日期和时间
Interval            datetime.timedelta  时间间隔
Enum                str                 一组字符串
PickleType          任何Python           对象自动使用Pickle 序列化
LargeBinary         str                 二进制文件


Interger,SmallInterger,BigInterger,Float,String,Text,Unicode,Boolean,Date,Time,Interval
Enum,PickleType,LargeBinary

最常使用的SQLAlchemy列选项
选项名                     说　　明
primary_key             如果设为True，这列就是表的主键
unique                  如果设为True，这列不允许出现重复的值
index                   如果设为True，为这列创建索引，提升查询效率
nullable                如果设为True，这列允许使用空值；如果设为False，这列不允许使用空值
default                 为这列定义默认值

primary-key,unique,index,nullable,default

5.7　关系
关系型数据库使用关系把不同表中的行联系起来。图5-1 所示的关系图表示用户和角色之
间的一种简单关系。这是角色到用户的一对多关系，因为一个角色可属于多个用户，而每
个用户都只能有一个角色。

class Role(db.Model):
    .....
    users = db.relationship('User',backref='role')

class User(db.Model):
    #...
    role_id = db.Column(db.Interger,db.ForeignKey('roles.id'))

关系使用users 表中的外键连接了两行。添加到User 模型中的role_id 列
被定义为外键，就是这个外键建立起了关系。传给db.ForeignKey() 的参数'roles.id' 表
明，这列的值是roles 表中行的id 值。

添加到Role 模型中的users 属性代表这个关系的面向对象视角。对于一个Role 类的实例，
其users 属性将返回与角色相关联的用户组成的列表。db.relationship() 的第一个参数表
明这个关系的另一端是哪个模型。如果模型类尚未定义，可使用字符串形式指定。

db.relationship() 中的backref 参数向User 模型中添加一个role 属性，从而定义反向关
系。这一属性可替代role_id 访问Role 模型，此时获取的是模型对象，而不是外键的值。

大多数情况下，db.relationship() 都能自行找到关系中的外键，但有时却无法决定把
哪一列作为外键。例如，如果User 模型中有两个或以上的列定义为Role 模型的外键，
SQLAlchemy 就不知道该使用哪列。如果无法决定外键，你就要为db.relationship() 提供
额外参数，从而确定所用外键。表5-4 列出了定义关系时常用的配置选项。

backref                 在关系的另一个模型中添加反向引用
primaryjoin             明确指定两个模型之间使用的联结条件。只在模棱两可的关系中需要指定
lazy                    指定如何加载相关记录。可选值有select（首次访问时按需加载）、immediate（源对象加载后就加载）、joined（加载记录，但使用联结）、subquery（立即加载，但使用子查询），
noload（永不加载）和dynamic（不加载记录，但提供加载记录的查询）

uselist                         如果设为Fales，不使用列表，而使用标量值
order_by                        指定关系中记录的排序方式
secondary                       指定多对多关系中关系表的名字
secondaryjoin SQLAlchemy        无法自行决定时，指定多对多关系中的二级联结条件


除了一对多之外，还有几种其他的关系类型。一对一关系可以用前面介绍的一对多关系
表示，但调用db.relationship() 时要把uselist 设为False，把“多”变成“一”。多对
一关系也可使用一对多表示，对调两个表即可，或者把外键和db.relationship() 都放在
“多”这一侧。最复杂的关系类型是多对多，需要用到第三张表，这个表称为关系表




5.8　数据库操作
首先，我们要让Flask-SQLAlchemy 根据模型类创建数据库。方法是使用db.create_all()
函数：
(venv) $ python hello.py shell
>>> from hello import db
>>> db.create_all()
如果你查看程序目录，会发现新建了一个名为data.sqlite 的文件。这个SQLite 数据库文件
的名字就是在配置中指定的。如果数据库表已经存在于数据库中，那么db.create_all()
不会重新创建或者更新这个表。如果修改模型后要把改动应用到现有的数据库中，这一特
性会带来不便。更新现有数据库表的粗暴方式是先删除旧表再重新创建：

db.create_all()  创建数据库
db.drop()  删除数据库


5.8.2 插入行
5.8.2　插入行
下面这段代码创建了一些角色和用户：
>>> from hello import Role, User
>>> admin_role = Role(name='Admin')
>>> mod_role = Role(name='Moderator')
>>> user_role = Role(name='User')
>>> user_john = User(username='john', role=admin_role)
>>> user_susan = User(username='susan', role=user_role)
>>> user_david = User(username='david', role=user_role)
模型的构造函数接受的参数是使用关键字参数指定的模型属性初始值。注意，role 属性也
可使用，虽然它不是真正的数据库列，但却是一对多关系的高级表示。这些新建对象的id
属性并没有明确设定，因为主键是由Flask-SQLAlchemy 管理的。现在这些对象只存在于
Python 中，还未写入数据库。因此id 尚未赋值：

>>> print(admin_role.id)
None
>>> print(mod_role.id)
None
>>> print(user_role.id)
None

通过数据库会话管理对数据库所做的改动，在Flask-SQLAlchemy 中，会话由db.session
表示。准备把对象写入数据库之前，先要将其添加到会话中：

>>> db.session.add(admin_role)
>>> db.session.add(mod_role)
>>> db.session.add(user_role)
>>> db.session.add(user_john)
>>> db.session.add(user_susan)
>>> db.session.add(user_david)
或者简写成：
>>> db.session.add_all([admin_role, mod_role, user_role,
... user_john, user_susan, user_david])

db.session.add()

db.session.add_all()


为了把对象写入数据库，我们要调用commit() 方法提交会话：
>>> db.session.commit()
再次查看id 属性，现在它们已经赋值了：
数据库会话db.session 和第4 章介绍的Flasksession 对象没有关系。数据库
会话也称为事务

数据库会话能保证数据库的一致性。提交操作使用原子方式把会话中的对象全部写入数据
库。如果在写入会话的过程中发生了错误，整个会话都会失效。如果你始终把相关改动放
在会话中提交，就能避免因部分更新导致的数据库不一致性。

数据库会话也可回滚。调用db.session.rollback() 后，添加到数据库会话
中的所有对象都会还原到它们在数据库时的状态。

db.session.add()
db.session.add_all()
db.session.commit()
db.session.rollback()

5.8.3　修改行
在数据库会话上调用add() 方法也能更新模型。我们继续在之前的shell 会话中进行操作，
下面这个例子把"Admin" 角色重命名为"Administrator"：
admin_role.name = 'Administrator'
db.session.add(admin_role)
db.session.commit()


5.8.4　删除行
数据库会话还有个delete() 方法。下面这个例子把"Moderator" 角色从数据库中删除：
db.session.delete(mod_role)
db.session.commit()

注意，删除与插入和更新一样，提交数据库会话后才会执行。

5.8.5 查询行
Flask-SQLAlchemy 为每个模型类都提供了query 对象。最基本的模型查询是取回对应表中
的所有记录：

>>> Role.query.all()
[<Role u'Administrator'>, <Role u'User'>]
>>> User.query.all()
[<User u'john'>, <User u'susan'>, <User u'david'>]

Role.query.all()
User.query.all()

使用过滤器
User.query.filter_by(role=user_role).all()

若要查看SQLAlchemy 为查询生成的原生SQL 查询语句，只需把query 对象转换成字
符串：

>>> str(User.query.filter_by(role=user_role))
'SELECT users.id AS users_id, users.username AS users_username,
users.role_id AS users_role_id FROM users WHERE :param_1 = users.role_id'

如果你退出了shell 会话，前面这些例子中创建的对象就不会以Python 对象的形式存在，而
是作为各自数据库表中的行。如果你打开了一个新的shell 会话，就要从数据库中读取行，
再重新创建Python 对象。下面这个例子发起了一个查询，加载名为"User" 的用户角色：
>>> user_role = Role.query.filter_by(name='User').first()
filter_by() 等过滤器在query 对象上调用，返回一个更精确的query 对象。多个过滤器可
以一起调用，直到获得所需结果。


常用的SQLALchemy查询过滤器
过滤器                  说明
filter()                把过滤器添加到原查询上，返回一个新查询
filter_by()             把等值过滤器添加到原查询上，返回一个新查询
limit()                 使用指定的值限制原查询返回的结果数量，返回一个新查询
offset()                 偏移原查询返回的结果，返回一个新查询
order_by()              根据指定条件对原查询结果进行排序，返回一个新查询
group_by()              根据指定条件对原查询结果进行分组，返回一个新查询

在查询上应用指定的过滤器后，通过调用all() 执行查询，以列表的形式返回结果。除了
all() 之外，还有其他方法能触发查询执行。表5-6 列出了执行查询的其他方法。

最常使用的SQLAlchemy查询执行函数
all()               以列表形式返回查询的所有结果
first()             返回查询的第一个结果，如果没有结果，则返回None
first_or_404()      返回查询的第一个结果，如果没有结果，则终止请求，返回404 错误响应
get()               返回指定主键对应的行，如果没有对应的行，则返回None
get_or_404()        返回指定主键对应的行，如果没找到指定的主键，则终止请求，返回404 错误响应
count()             返回查询结果的数量
paginate()          返回一个Paginate 对象，它包含指定范围内的结果


all(),first(),first_or_404(),get_or_404(),count(),paginate()


5.9　在视图函数中操作数据库
@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index.html',
                           form=form, name=session.get('name'),
                           known=session.get('known', False))

5.10　集成Python shell
每次启动shell 会话都要导入数据库实例和模型，这真是份枯燥的工作。为了避免一直重复
导入，我们可以做些配置，让Flask-Script 的shell 命令自动导入特定的对象。
若想把对象添加到导入列表中，我们要为shell 命令注册一个make_context 回调函数，如
示例5-7 所示。
示例5-7　hello.py：为shell 命令添加一个上下文
from flask.ext.script import Shell
def make_shell_context():
return dict(app=app, db=db, User=User, Role=Role)
manager.add_command("shell", Shell(make_context=make_shell_context))
make_shell_context() 函数注册了程序、数据库实例以及模型，因此这些对象能直接导入shell：


5.11　使用Flask-Migrate实现数据库迁移
在开发程序的过程中，你会发现有时需要修改数据库模型，而且修改之后还需要更新数据库。
仅当数据库表不存在时，Flask-SQLAlchemy 才会根据模型进行创建。因此，更新表的唯一
方式就是先删除旧表，不过这样做会丢失数据库中的所有数据。

更新表的更好方法是使用数据库迁移框架。源码版本控制工具可以跟踪源码文件的变化，
类似地，数据库迁移框架能跟踪数据库模式的变化，然后增量式的把变化应用到数据库中。

SQLAlchemy 的主力开发人员编写了一个迁移框架，称为Alembic（https://alembic.readthedocs.
org/en/latest/index.html）。除了直接使用Alembic 之外，Flask 程序还可使用Flask-Migrate
（http://flask-migrate.readthedocs.org/en/latest/）扩展。这个扩展对Alembic 做了轻量级包装，并
集成到Flask-Script 中，所有操作都通过Flask-Script 命令完成。

Alcmbic

flask-migrate

首先，我们要在虚拟环境中安装Flask-Migrate：
(venv) $ pip install flask-migrate
这个扩展的初始化方法如示例5-8 所示。
示例5-8　hello.py：配置Flask-Migrate
from flask.ext.migrate import Migrate, MigrateCommand
# ...
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)
为了导出数据库迁移命令，Flask-Migrate 提供了一个MigrateCommand 类，可附加到Flask-
Script 的manager 对象上。在这个例子中，MigrateCommand 类使用db 命令附加。
在维护数据库迁移之前，要使用init 子命令创建迁移仓库：
(venv) $ python hello.py db init
Creating directory /home/flask/flasky/migrations...done
Creating directory /home/flask/flasky/migrations/versions...done
Generating /home/flask/flasky/migrations/alembic.ini...done
Generating /home/flask/flasky/migrations/env.py...done
Generating /home/flask/flasky/migrations/env.pyc...done
Generating /home/flask/flasky/migrations/README...done
Generating /home/flask/flasky/migrations/script.py.mako...done
Please edit configuration/connection/logging settings in
'/home/flask/flasky/migrations/alembic.ini' before proceeding.
这个命令会创建migrations 文件夹，所有迁移脚本都存放其中。
数据库迁移仓库中的文件要和程序的其他文件一起纳入版本控制

from flask.ext.migrate import Migrate,MigrateCommand
migirate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

5.11.2　创建迁移脚本
在Alembic 中，数据库迁移用迁移脚本表示。脚本中有两个函数，分别是upgrade() 和
downgrade()。upgrade() 函数把迁移中的改动应用到数据库中，downgrade() 函数则将改动
删除。Alembic 具有添加和删除改动的能力，因此数据库可重设到修改历史的任意一点。

我们可以使用revision 命令手动创建Alembic 迁移，也可使用migrate 命令自动创建。
手动创建的迁移只是一个骨架，upgrade() 和downgrade() 函数都是空的，开发者要使用

Alembic 提供的Operations 对象指令实现具体操作。自动创建的迁移会根据模型定义和数
据库当前状态之间的差异生成upgrade() 和downgrade() 函数的内容。

自动创建的迁移不一定总是正确的，有可能会漏掉一些细节。自动生成迁移
脚本后一定要进行检查。

migrate 子命令用来自动创建迁移脚本：
(venv) $ python hello.py db migrate -m "initial migration"
INFO [alembic.migration] Context impl SQLiteImpl.
INFO [alembic.migration] Will assume non-transactional DDL.
INFO [alembic.autogenerate] Detected added table 'roles'
INFO [alembic.autogenerate] Detected added table 'users'
INFO [alembic.autogenerate.compare] Detected added index
'ix_users_username' on '['username']'
Generating /home/flask/flasky/migrations/versions/1bc
594146bb5_initial_migration.py...done

5.11.3　更新数据库
检查并修正好迁移脚本之后，我们可以使用db upgrade 命令把迁移应用到数据库中：
(venv) $ python hello.py db upgrade
INFO [alembic.migration] Context impl SQLiteImpl.
INFO [alembic.migration] Will assume non-transactional DDL.
INFO [alembic.migration] Running upgrade None -> 1bc594146bb5, initial migration
对第一个迁移来说， 其作用和调用db.create_all() 方法一样。但在后续的迁移中，
upgrade 命令能把改动应用到数据库中，且不影响其中保存的数据。






