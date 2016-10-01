#!/usr/bin/env python
# coding: utf8

import paramiko

t = paramiko.Transport(("139.129.47.28", 22))
t.connect(username="root", password="***")
sftp = paramiko.SFTPClient.from_transport(t)
# localpath = "/root/python/paramiko/pk1.py"
# remotepath = "/tmp/pk1.py"
# sftp.put(localpath=localpath, remotepath=remotepath)
localpath = "/root/python/paramiko/log.txt"
remotepath = "/tmp/cmdb/2.txt"
sftp.get(remotepath=remotepath, localpath=localpath)
sftp.close()
t.close()
