#!/usr/bin/env python
# coding:utf8

from collections import namedtuple

websites = [
    ('sohu', 'http://www.sohu.com', u'张朝阳'),
    ('sina', 'http://www.sina.com', u'王志东'),
    ('163', 'http://www.163.com', u'丁磊'),

]

web = namedtuple('website', ['name', 'url', 'founder'])
for i in websites:
    a = web._make(i)
    print a


# result:
# website(name='sohu', url='http://www.sohu.com', founder=u'\u5f20\u671d\u9633')
# website(name='sina', url='http://www.sina.com', founder=u'\u738b\u5fd7\u4e1c')
# website(name='163', url='http://www.163.com', founder=u'\u4e01\u78ca')