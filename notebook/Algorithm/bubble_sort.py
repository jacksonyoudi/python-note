# coding: utf8
a = [18, 27, 69, 13, 45, 87, 49, 67]

for j in reversed(range(len(a)-1)):
    for i in range(j+1):
        if a[i] >= a[i + 1]:
            continue
        else:
            a[i], a[i + 1] = a[i + 1], a[i]

print a