# coding: utf8

php超文本预处理器是一种允许网站开发者创建与数据库相互作用的动态内容编程语言
php基本上是用于开发软件应用网站的语言。

php是 hypertext Preprocessor
php是嵌入在HTML中的服务器端脚本语言。它用来管理动态内容、数据库、会话跟踪、甚至简历整个商务网站
它集成了许多流行的数据库，包括mysql、postgreSQL，Oracle、Sybase、Informix和Microsoft SQLServer

尤其在Unix系统里PHP作为Apache编译模块是，php有令人欣喜的执行力。一旦开始，mysql
服务器将在设定的时间内执行非常复杂的命令查询巨大的结果集。

php支持一大批主要协议，如pop3，IMAP和LDAP。PHP4添加了对java的支持，并且首次分布式对象体系结构
（COM和CORBA），并制作多层开发
php语言简洁：PHP语言系统要求不需要太严谨。
PHP语法类似C语言

PHP的常见用途：
PHP执行系统功能,创建、打开、读、写和关闭系统上的文件。
PHP可以处理forms表单，如手机数据文件，将数据保存到一个文件中，可以通过电子邮件发送数据，返回给用户数据。
通过PHP在数据库中添加、删除、修改元素。
访问cookie变量和设置cookie
使用PHP，可以限制用户访问网站的某些页面
可以对数据加密。

php的特点：
简单
效率
安全
灵活
多变


嵌入到html中

<html>
<head>
<title>hello World</title>
<body>
<?php echo "Hello,World"?>
</body>
</html>

若要检查上面的例子中输出，你会注意到php代码不是本文件从服务器发送到web浏览器中
所有的php在web也中呈现处理和脱离状态；从web服务器向客户端返回的唯一的方式就是纯粹的HTMl输出。
所有PHP代码必须包含三个特别的标记之一才可以被PHP解释器认可。
<?php PHP code gose here?>
<? PHP code goes here ?>
<script language="php"> PHP code goes here</script>



php环境设置
为了正常开发和运行PHP web页面，有三个重要的组件需要安装在你的计算机系统中。
    web服务器
    数据库
    php解释器--为了处理php脚本，指令解释器必须安装生成html输出，可以发送到web浏览器。

php解析：
用户区分php代码  php解析
<?php ?>


段标签格式
SGML形式
<? ...?>
当你构建php时，选择--enable-short-tags配置选项
在php.ini文件中设置short_open_tag为on.PHP配置文件中必须禁用此项放置解析XML，因为相同的语法适用于XML标记。

ASP风格的标签
<%.....%>
<script language="PHP">...</script>


php代码的注释

#
#
//

多行注释
/*  */


php对空格不敏感
php大小敏感
语句表达式由分号终止
表达式的组合令牌
花括号组成代码块

在命令提示符中运行 PHP 脚本
php test.php

变量类型
信息存储的主要方式是通过一个PHP程序使用一个变量。这里了解PHP变量是很重要的事情。
所有的变量在php中标有一个$
一个变量的值取决于最近赋给的值
变量赋值使用 '=' 操作符、变量左边和右边的表达式计算
变量可以不需要被提前定义，使用时定义即可。
php变量中没有内在类型---一个变量实现不知道是否会用于存储数字还是字符串
变量使用之前，需要分配有默认值
php可以自动地从一个类型转换成另一个类型


数据类型：
整数
浮点数
布尔值
空：
字符串类型
数组
对象
资源


整数：
$int_var = 12345;
$another_int = -12345 + 12345;

浮点型：
$many = 2.288888;

布尔值：
if (TRUE)
    print("this will always print")
else
    print("this will never print")

空
$my_var = NULL

一个变量被赋值为空，有以下属性：
它在布尔上下文的求值结果为FALSE
测试使用IsSet()函数时返回FALSE

字符串
''
""  可以引用





