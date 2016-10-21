# coding: utf8

class Stack():
    def __init__(self, size):
        self.stack = []
        self.size = size

    def push(self, var):
        if self.Full():
            return 'Full,can not push'
        else:
            self.stack.append(var)

    def pop(self):
        if self.Empty():
            return 'Empty ,can not pop'
        else:
            a = self.stack.pop(0)
            print a
    def Full(self):
        if len(self.stack) == self.size:
            return True
        else:
            return False

    def Empty(self):
        if self.stack == []:
            return True
        else:
            return False
