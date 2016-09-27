#!/usr/bin/env python
# coding: utf8

from optparse import OptionParser

useage = 'myprog [-f <filename>] [-s <xyz>] arg1[,arg2...]'
optParser = OptionParser(useage)
optParser.add_option("-f", "--file", action="store", type="string", dest="filename")
optParser.add_option("-v", "--version", action="store", dest="verbose", default="None",
                      help="make lots of noise [default]")
fakeArgs = ['-f', 'file.txt', '-v', 'good luck to you', 'arg2', 'arge']
options, args = optParser.parse_args(fakeArgs)

print options.filename
print options.verbose
print options
print args
print optParser.print_help()
