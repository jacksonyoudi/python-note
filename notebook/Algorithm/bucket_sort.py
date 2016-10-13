# coding: utf8
a = [3, 4, 6, 1, 4, 5]

init_list = (max(a)+1) * [0]

for i in a:
    init_list[i] += 1

count = 0
for i in init_list:
    for j in xrange(i):
        print count
    count += 1
