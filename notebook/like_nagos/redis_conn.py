#!/usr/bin/env python
# coding: utf8

import redis

conn = redis.Redis(host='localhost')
conn.set('test', 'redis testing')
