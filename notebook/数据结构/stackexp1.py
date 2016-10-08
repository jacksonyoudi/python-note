class Stack():
    def __init__(self, size):
        self.stack = []
        self.size = size
        self.top = 1

    def push(self, content):
        if self.Full():
            print "Stack is Full"
        else:
            self.stack.append(content)
            self.top = self.top + 1

    def pop(self):
        if self.Empty():
            print "Stack is Empty"
        else:
            self.top = self.top - 1
            return self.stack.pop()


    def Full(self):
        if self.top == self.size:
            return True
        else:
            return False

    def Empty(self):
        if self.top == -1:
            return True
        else:
            return False