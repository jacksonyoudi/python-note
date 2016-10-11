Docker包括三个基本概念
镜像(Image)
容器(Container)
仓库(Repository)

Docker镜像只是一个只读模板。
镜像可以用来创建Docker容器。
Docker 提供了一个很简单的机制来创建镜像或者更新现有的镜像，用户甚至可以直接从其他人那里下载一个已
经做好的镜像来直接使用。


Docker容器
容器是从镜像创建的运行实例。它可以被启动，开始，停止，删除。每个容器都是相互隔离的，保证安全的平台。
可以把容器看做是一个简易版的linux环境（ 包括root用户权限，进程空间、用户空间和网络空间）和运行在其中的应用程序。


注意：镜像是只读的，容器在启动的时候穿件一层可写层作为最上层。


Docker仓库
仓库是集中存放镜像文件的场所。有时候会把仓库和仓库注册服务器(Registry)混为一谈，并不严格区分。实际上，仓库注册服务器上
往往存放多个仓库，每个仓库又包含多个镜像，每个镜像有不同的标签（tag）。

仓库分为公开仓库(publick)和私有仓库(Private)两种形式。

最大的公开仓库是 Docker Hub(https://hub.docker.com),存放了数量庞大的镜像提供给用户下载
国内是Docker Pool(http://www.dockerpool.com)

用户可以在本地创建本地网络的私有仓库。

当用户创建了自己的镜像之后可以使用push命令将他上传到公有或私有的仓库，这样下次在另一台机器上使用这个镜像了，只是从仓库pull下来。


获取镜像

docker pull ubuntu:14.04
docker pull registry.hub.docker.com/ubuntu:14.04
docker pull dl.dockerpool.com:5000/ubuntu:14.04

14.04: Pulling from library/ubuntu
04c996abc244: Downloading [================>                                  ] 21.09 MB/65.7 MB
d394d3da86fe: Download complete
bac77aae22d4: Download complete
b48b86b78e97: Download complete
09b3dd842bf5: Download complete
09b3dd842bf5: Pulling fs layer


获得容器以后：
使用容器
docker run -t -i ubuntu:14.04 /bin/bash

Usage:	docker run [OPTIONS] IMAGE [COMMAND] [ARG...]
-t, --tty                       Allocate a pseudo-TTY
-i, --interactive               Keep STDIN open even if not attached


显示出本地已有的镜像
docker images

docker的文件保存在/var/lib/docker下面
cat /var/lib/docker/image/aufs/repositories.json | python -mjson.tool
显示详细信息

root@VM-166-182-ubuntu:/var/lib/docker/image/aufs# docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
ubuntu              14.04               f2d8ce9fa988        13 days ago         187.9 MB
ubuntu              15.10               9b9cb95443b5        11 weeks ago        137.2 MB
hello-world         latest              c54a2cc56cbb        3 months ago        1.848 kB

显示： repository 仓库、镜像标记,ID,创建时间，镜像大小
TAG 信息用来标记来自统一仓库的不同镜像
ID:用于标识唯一镜像，如果ID一样，说明是同一个镜像。

运行容器
docker run -t -i ubuntu:14.04 /bin/bash
如果不指定TAG,默认使用latest


创建镜像：
创建镜像的有很多种方法，用户可以从Docker Hub获取已有的镜像并更新。也可以利用本地文件系统创建一个。


修改已有的镜像：
先使用下载的镜像启动容器
docker -t -i training/sinatra /bin/bash
exit

docker commit -m '说明信息' -a '作者信息' ID号 repository:tag

docker commit -m "Added json gem" -a "Docker Newbee" 0b2616b0e5a8 ouruser/sinatra:v2
4f177bd27a9ff0f6dc2a830403925b5360bfe0b93d476f7fc3231110e7f71b1c


利用Dockerfile来创建镜像
使用docker commit来扩展一个镜像比较简单，但是不方便在一个团队中共享。我们可以使用dcoker build来创建
一个新的镜像。
所以，首先需要创建一个Dockerfile，包含一些如何创建一个镜像的指令。

新建一个目录和一个Dockerfile

Dockerfile 中每一条指令都创建镜像的一层，例如：
# This is a comment
FROM ubuntu:14.04
MAINTAINER Docker Newbee <newbee@docker.com>
RUN apt-get -qq update
RUN apt-get -qqy install ruby ruby-dev
RUN gem install sinatra
Dockerfile 基本的语法是 * 使用# 来注释 * FROM 指令告诉 Docker 使用哪个镜像作为基础 * 接着是维护者
的信息 * RUN 开头的指令会在创建中运行，比如安装一个软件包，在这里使用 apt-get 来安装了一些软件
编写完成 Dockerfile 后可以使用docker build 来生成镜像。

sudo docker build -t="ouruser/sinatra:v2" .  （注意路径）
其中-t 标记来添加 tag，指定新的镜像的用户信息。 “.” 是 Dockerfile 所在的路径（当前目录），也可以替
换为一个具体的 Dockerfile 的路径。
可以看到 build 进程在执行操作。它要做的第一件事情就是上传这个 Dockerfile 内容，因为所有的操作都要依据
Dockerfile 来进行。 然后，Dockfile 中的指令被一条一条的执行。每一步都创建了一个新的容器，在容器中执行
指令并提交修改（就跟之前介绍过的docker commit 一样）。当所有的指令都执行完毕之后，返回了最终的镜
像 id。所有的中间步骤所产生的容器都被删除和清理了。

此外，还可以利用ADD 命令复制本地文件到镜像；用EXPOSE 命令来向外部开放端口；用CMD 命令来
描述容器启动后运行的程序等。例如
# put my local web site in myApp folder to /var/www
ADD myApp /var/www
# expose httpd port
EXPOSE 80
# the command to run
CMD ["/usr/sbin/apachectl", "-D", "FOREGROUND"]

修改镜像的标签
sudo docker tag 5db5f8471261 ouruser/sinatra:devel

docker tag ID repository:tag


从本地文件系统导入
cat ubuntu-14.04-x86_64-minimal.tar.gz |docker import - ubuntu:14.04


上传镜像
用户可以通过docker push命令，把自己创建的镜像上传到仓库中来共享。
用户在Docker Hub上完成注册后，可以推送自己的镜像到仓库中。
docker push ouruser/sinatra


存出和载入镜像

存出镜像可以使用docker save
docker save -o ubuntu:14.04

装入镜像
docker load
docker load --input ubuntu_14.04.tar
或 docker  load < ubuntu_14.04.tar


移除镜像
docker rmi
docker rmi training/sinatra
docker rmi c54a2cc56cbb
注意：在删除镜像之前要先用docker rm 删掉依赖于这个镜像的所有容器。


镜像实现的原理
镜像是如何实现增量的修改和维护的？
每个镜像都是由很多层次构成，docker使用Union FS将这些不同的层结合到一个镜像中去的。

通常Union FS有两个用途，一方面可以实现不借助LVM，RAID将多个disk挂载到同一个目录下，另外更常用的就是将一个只读的分支和一个可写的分支联合在一起
live CD正是基于此方法可以允许在镜像上不变的基础上允许用户在其上进行一些写的操作。Docker在AUFS上构建容器也是利用了类似的原理。



启动：
容器是独立运行的一个或一组应用，以及他们的运行环境。对应的，虚拟机可以理解为模拟运行的一整套操作系统（提供了运行态环境和其他系统环境）
和跑在上面的应用。


启动容器有两种方式：
一种是基于镜像新建一个容器并启动
另一种是一个将在终止状态(stopped)的容器重新启动。

新建并启动
docker run
docker run ubuntu:14.04 /bin/echo 'hello word'
执行完命令，容器就会终止

docker run -t -i ubuntu:14.04 /bin/bash
启动一个bash终端
-t 选项让Docker分配一个伪终端（pseudo-tty）并绑定到容器的标准输入上， -i 则让容器的标准输入保持打开。


当利用docker run 来创建容器时，Docker在后台运行的标准操作包括：
检查本地是否在指定的镜像中，不存在就从公有仓库中下载
利用镜像创建并启动一个容器
分配一个文件系统，并在只读的镜像层外面挂载一层可读层
从宿主主机配置的网桥接口中桥接一个虚拟接口到容器中去
从地址池配置一个ip地址给容器
执行用户指定的应用程序
执行完毕后容器被终止

启动已终止容器
可以利用docker start命令，直接将一个已经终止的容器启动运行。


守护态运行
docker run -d
sudo docker run -d ubuntu:14.04 /bin/sh -c "while true; do echo hello world; sleep 1; done"

docker ps查看容器的信息

获取docker容器的输出信息，可以通过docker logs命令。

终止容器
docker stop来终止运行中的容器
docker restart


进入容器
docker attach
nsenter



导出和导入容器
docker ps -a
如果要导出本地某个容器，可以使用docker export命令
docker export 7691a814370e >ubuntu.tar
这样将容器快照到本地文件

导入容器快照
docker import

删除一个处于终止状态的容器
socker rm  trusting_newton



仓库(repository)是集中存放镜像的地方
注册服务器(registry),实际上注册服务器是管理仓库的的具体服务器，每个服务器上可以有更多个仓库，每个仓库有多个镜像。
仓库可以被认为一个具体的项目或目录。

登录
docker login
可以通过执行docker login 命令来输入用户名、密码和邮箱来完成注册和登录。 注册成功后，本地用户目录的
.dockercfg 中将保存用户的认证信息。
.dockercfg

查找；
docker search
命令来查找官方仓库中的镜像

可以看到返回了很多包含关键字的镜像，其中包括镜像名字、描述、星级（表示该镜像的受欢迎程度）、是否官
方创建、是否自动创建。 官方的镜像说明是官方项目组创建和维护的，automated 资源允许用户验证镜像的来
源和内容。

docker search -s N


docker pull
docker push

自动创建(Automated Builed)
自动创建（Automated Builds）功能对于需要经常升级镜像内程序来说，十分方便。 有时候，用户创建了镜
像，安装了某个软件，如果软件发布新版本则需要手动更新镜像。。
而自动创建允许用户通过 Docker Hub 指定跟踪一个目标网站（目前支持 GitHub 或 BitBucket）上的项目，一
旦项目发生新的提交，则自动执行创建。

自动创建的具体步骤:
创建并登陆Docker Hub，以及目标网站
在目标网站中连接账户到Docker Hub
在 Docker Hub 中配置一个自动创建(https://registry.hub.docker.com/builds/add/) ；
选取一个目标网站中的项目（需要含 Dockerfile）和分支；
指定 Dockerfile 的位置，并提交创建。


私有仓库

docker-registry
docker run -d -p 5000:5000 -v /home/user/registry-conf:/registry-conf -e DOCKER_REGIS
TRY_CONFIG=/registry-conf/config.yml registry
默认情况下，仓库会被创建在容器的 `/tmp/registry` 下。可以通过 `-v` 参数来将镜像文件存放在本地的指定路径。
例如下面的例子将上传的镜像放到 `/opt/data/registry` 目录。
docker run -d -p 5000:5000 -v /opt/data/registry:/tmp/registry registry













