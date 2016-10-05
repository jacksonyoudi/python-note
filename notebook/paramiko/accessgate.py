#!/usr/bin/env python
# coding: utf8

import paramiko


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(username='root', port=22, hostname='139.129.47.28', key_filename='/root/.ssh/id_rsa')

channel = ssh.invoke_shell()
channel.close()
ssh.close()
