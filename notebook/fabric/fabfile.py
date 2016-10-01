#!/usr/bin/env python
# coding: utf8
from fabric.api import run


def host_type():

    run('uname -s')


if __name__ == '__main__':
    host_type()
