# coding: utf8

class Tree():
    def __init__(self,leftjd=0,rightjd=0,data=0):
        self.leftjd = leftjd
        self.rightjd = rightjd
        self.data = data

class Btree():
    def __init__(self,base):
        self.base=base
    def empty(self):
        if self.base is 0:
            return True
        else:
            return False
    def quot(self,jd):
        '''
        前序遍历，NLR，根左右
        '''
        if jd==0:
            return
        print jd.data
        self.quot(jd.leftjd)
        self.quot(jd.rightjd)

    def mount(self,jd):
       '''中序遍历，LNR，左根右'''
       if jd==0:
           return
       self.mount(jd.leftjd)
       print jd.data
       self.mount(jd.rightjd)
    def hout(self,jd):
        '''后序遍历，LRN，左右根'''
        if jd==0:
            return
        self.hout(jd.leftjd)
        self.hout(jd.rightjd)
        print jd.data
