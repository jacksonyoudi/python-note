# coding: utf8
chart = {'A': ['B', 'D'], 'C': ['E'], 'D': ['C', 'E']}


def path(chart, x, y, pathd=[]):
    '''
    :param chart:  图
    :param x: 起点
    :param y: 最终节点
    :param pathd: 路径
    :return:
    '''
    pathd = pathd + [x]
    if x == y:
        return pathd
    if not chart.has_key(x):
        return None

    for jd in chart[x]:
        if jd not in pathd:
            newjd = path(chart, jd, y, pathd)
            if newjd:
                return newjd
