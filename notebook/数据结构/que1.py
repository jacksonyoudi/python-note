class Queue():
    def __init__(self, size):
        self.queue = []
        self.size = size
        self.head = -1
        self.tail = -1

    def Empty(self):
        if self.head == self.tail:
            return True
        else:
            return False

    def Full(self):
        if self.tail - self.head + 1 == self.size:
            return True
        else:
            return False

    def enQueue(self, content):
        if self.Full():
            print "Queue is Full!"
        else:
            self.queue.append(content)
            self.tail = self.tail + 1

    def outQueue(self):
        if self.Empty():
            print "Queue is Empty!"
        else:
            self.head = self.head + 1
            return self.queue.pop()
