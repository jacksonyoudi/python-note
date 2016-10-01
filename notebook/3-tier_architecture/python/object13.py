#!/usr/bin/env python
# coding: utf8

class Employee(object):
    def __init__(self, name, job=None, pay=0):
        self._name = name
        self._job = job
        self._pay = pay

    def giveRaise(self, percent):
        self._pay = int(self._pay * (1 + percent))

    def __str__(self):
        return '[Employee:%s,%s,%s]' % (self._name, self._job, self._pay)


class Manager(Employee):
    def __init__(self, name, pay):
        Employee.__init__(self, name, 'mgr', pay)

    def giveRaise(self, percent, bonus=.10):
        Employee.giveRaise(self, percent + bonus)


class Department(object):
    def __init__(self, *args):
        self.members = list(args)

    def addMember(self, person):
        self.members.append(person)

    def showAll(self):
        for person in self.members:
            print person

    def giveRaise(self, percent):
        for person in self.members:
            person.giveRaise(percent)


if __name__ == '__main__':
    a = Employee("xiaoli", "sw_engince", 10000)
    b = Employee("xiaowang", "hw_engince", 12000)
    c = Manager("xiaozhang", 8000)

    d = Department(a, b, c)

    d.showAll()
    d.giveRaise(0.1)
    d.showAll()
