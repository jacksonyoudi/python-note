#!/usr/bin/env python
# coding: utf8

import salt.client

client = salt.client.LocalClient()
ret = client.cmd('*', 'test.ping')
print ret
