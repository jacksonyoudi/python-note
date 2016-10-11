OAuth使用第三方账号登录
OAuth2.0

Oauth 2.0原理与授权流程


应用场景：
服务商：用户资源（例如相册+日记）
提供授权认证和资源访问接口

3.第三方应用使用用户提供的账号、密码获取资源


第三方应用
用户授权
获取相册中图片
处理后图片存回

1.用户向第三方应用发起访问，要获取存储在服务商端的相册图片
2.第三方应用要求用户提供服务商的账号和密码


用户

存在的问题：
1.用户的账号，密码信息透漏给第三方，导致安全问题
2.用户要收回授权，只能通过修改密码来实现，此时如果有多个第三方应用，所有授权一起被收回
3.很难安全的实现对不同的第三方应用给予不同的权限



OAuth是一个协议标准


第三方应用
（图片在线编辑工具）
用户授权
获取相册中图片
处理后的图片存回

1.用户向第三方应用发起访问，要获取存储在服务器上的相册图片
2.第三方应用引导用户跳转到服务端授权页进行授权


用户

3.用户在服务商端完成授权后，服务端生成一个令牌（令牌中包含登录信息，权限控制等，第三方的平台等）
并携带此令牌跳回第三方应用

服务商
用户资源（相册+日记）
提供授权认证和资源访问接口

4.第三方应用以服务端生成令牌为访问凭证发起资源访问
（令牌信息包含了用户、第三方应用、资源权限等信息）


Oauth2.0授权流程

用户
1.用户请求第三方应用获取服务商端资源
2.第三方应用引导用户浏览器redirect至服务商授权页
url参数中主要包含如下信息：
第三方应用身份、授权方式、回调地址、请求资源列表

3.用户在服务商的授权页完成授权操作

4.服务商应用引导用户跳回到第三方应用提供的回调地址，
并将一个一次性的授权码code作为参数传回

5.浏览器以授权码为参数访问第三方应用
第三方应用后台获取到当前授权码code

6.第三方应用以code和第三方身份、密钥信息为参数
调用服务商提供的APi进行访问授权

7.授权成功后服务商返回给第三方应用一个访问码acess token

8.服务商一access token为凭证调用服务商提供的各类API完成资源访问操作。


3个关键过程：
1.用户在服务商授权页完成授权，获得code
2.第三方应用取得code后访问服务商应用，获得access token
3.第三方应用以access token为凭证到服务商出获取资源



开发者注册与应用创建
注册平台账号
申请成为开发者
创建网站接入类型应用  获取apikey，secretKey等信息（身份和密钥）
设置回调URL  获取回调地址 redirect uri信息
开发测试
提交审核，应用上线


http://developer.baidu.com/wiki/index.php?title=docs/oauth/application



1. 引导用户到如下地址进行授权：
http://openapi.baidu.com/oauth/2.0/authorize?
	response_type=code&
	client_id=YOUR_CLIENT_ID&
	redirect_uri=YOUR_REGISTERED_REDIRECT_URI&
	scope=email&
	display=popup

其中：client_id=APikey
redirect_uri='回调地址'

2. 如果用户同意授权,页面跳转至 YOUR_REGISTERED_REDIRECT_URI/?code=CODE 。
3. 换取Access Token。

请求：
https://openapi.baidu.com/oauth/2.0/token?
	grant_type=authorization_code&
	code=CODE&
	client_id=YOUR_CLIENT_ID&
	client_secret=YOUR_CLIENT_SECRET&
	redirect_uri=YOUR_REGISTERED_REDIRECT_URI

返回：
{
    "access_token": "1.a6b7dbd428f731035f771b8d15063f61.86400.1292922000-2346678-124328",
    "expires_in": 86400,
    "refresh_token": "2.385d55f8615fdfd9edb7c4b5ebdc3e39.604800.1293440400-2346678-124328",
    "scope": "basic email",
    "session_key": "ANXxSNjwQDugf8615OnqeikRMu2bKaXCdlLxn",
    "session_secret": "248APxvxjCZ0VEC43EYrvxqaK4oZExMB",
}

获取用户信息：
#获取当前登录用户的信息
返回当前登录用户的用户名、用户uid、用户头像。
passport/users/getLoggedInUser



Oauth2.0的原理
概述
Oauth几种授权模式
授权码模式

Oauth（开放授权）是一个正式的互联网标准协议。在不需要用户名和密码的，从第三方服务商那里获取用户资源信息。
允许第三方网站在用户授权的前提下访问用户在服务商那里存储的各种信息。而这种授权无序江永提供用户名和密码给第三方网站。
Oauth允许用户提供一个令牌给第三方网站，一个令牌对应一个特定的第三方网站，同时该令牌只能在特定的时间内访问特定的资源。
授权模式
授权码模式(authorization code): 不通过用户浏览器
简化模式(implicit)：没有C,D步骤
密码模式(resource ownwer password credenttials)
客户端模式(client credentials)

授权码模式是功能最完全的，流程最为严密的授权模式
简化模式不通过第三方应用程序的服务器，直接在浏览器中向认证服务器申请令牌，跳过了授权码这个步骤
密码模式需要用户向客户端提供自己的用户名和密码
客户端模式指客户端以自己的名义，而不是用户的名义，向“服务器提供商”进行认证
