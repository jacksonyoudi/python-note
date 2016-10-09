#!/usr/bin/env python
# coding: utf8

from collections import Counter
s = '''A Counter is a dict subclass for counting hashable objects. It is an unordered collection where elements are stored as dictionary keys and their counts are stored as dictionary values. Counts are allowed to be any integer value including zero or negative counts. The Counter class is similar to bags or multisets in other languages.'''.lower()
c = Counter(s)
# 获取出现频率最高的5个字符
print c.most_common(5)

