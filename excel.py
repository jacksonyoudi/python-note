#!/usr/bin/env python
# coding: utf8

import xlrd
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def excel_read():
    workbook = xlrd.open_workbook('1.xlsx')
    print workbook.sheet_names()

if __name__ == '__main__':
    excel_read()
