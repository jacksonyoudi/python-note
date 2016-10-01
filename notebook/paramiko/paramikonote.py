# coding: utf8

一、安装，下载

　　1、下载安装 pycrypto-2.6.1.tar.gz　　（apt-get install python-dev）

　　　　解压，进入，python setup.py build【编译】，python setup.py install 【安装】  ----》import Crypto

　　2、下载安装 paramiko-1.10.1.tar.gz　　

　　　　解压，进入，python setup.py build【编译】，python setup.py install 【安装】---》  import paramiko



通过密码登录

import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 第一次接受主机认证
# /root/.ssh/known_hosts


ssh.connect()
stdin,stdout,stderr = ssh.exec_command('')
print stdout
ssh.close()

def connect(
        self,
        hostname,
        port=SSH_PORT,
        username=None,
        password=None,
        pkey=None,
        key_filename=None,
        timeout=None,
        allow_agent=True,
        look_for_keys=True,
        compress=False,
        sock=None,
        gss_auth=False,
        gss_kex=False,
        gss_deleg_creds=True,
        gss_host=None,
        banner_timeout=None
):

使用密钥登录

ssh-keygen -t rsa
ssh-copy-id -i ~/ssh/id_id_rsa.pub root@ip

import paramiko
private_key_path = '/home/auto/.ssh/id_rsa'
key = paramiko.RSAKey.from_private_key_file(private_key_path)

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='host',port=port,key_filename=key,username='username')

stdin,stdout,stderr = ssh.exec_command(command='')
print stdout.read()
ssh.close()

非对称加密：



上传和下载文件
import os,sys
import paramiko

sock = ip_port = (ip,port)
t = paramiko.Transport(sock=sock) # 创建一个通道
t.connect(username=username,password=password) # 通道连接
sftp = paramiko.SFTPClient.from_transport(t)  # 在通道上创建sftp连接
sftp.get(remotepath=path,localpath=path1)
sftp.put(remotepath=path2,localpath=path3)
t.close()


SSH上传和下载

import paramiko

private_key_path = 'path'
key = paramiko.RSAKey.from_private_key_file(private_key_path)

sock = ()
t = paramiko.Transport(sock=sock)
t.connect(hostkey=key,username=user)
sftp = paramiko.SFTPClient(t)
sftp.put(localpath='',remotepath='')

sftp.get(localpath='',remotepath='')

t.close()

第三种连接
import paramiko
scp = paramiko.Transport(sock=sock)
scp.connect(username='',password=)
channel  = scp.open_session()
print channel.exec_command(command='')
channel.close()
scp.close()


交互式连接

import paramiko

scp = paramiko.Transport(sock=sock)
scp.connect(username='',password='')
channel = scp.open_session()
print channel.exec_command('')
channel.close()
scp.close()

channel = ssh.invoke_shell()
interactive.interactive_shell(channel)
channel.close()
ssh.close()




