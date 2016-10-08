# coding: utf8
class Bitmap():
    def __init__(self, max):
        self.size = int((max + 31 - 1) / 31)
        self.array = [0 for i in range(self.size)]

    def bitIndex(self, num):
        return num % 31

    def set(self, num):
        elemIndex = num / 31
        byteIndex = self.bitIndex(num)
        elem = self.array[elemIndex]
        self.array[elemIndex] = elem | (1 << byteIndex)

    def test(self, i):
        elemIndex = x / 31
        byteIndex = self.bitIndex(i)
        if self.array[elemIndex] & (1 << byteIndex)
            return True
        return False
