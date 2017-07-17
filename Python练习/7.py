#!/usr/bin/python
class Student(object):
    @property
    def brith(self):
        return self.__brith
    @brith.setter
    def brith(self,value):
        self.__brith = value

    @property
    def age(self):
        return 2015 - self.__brith

s=Student()
s.brith=11
print(s.brith)
print("****************************************************")
print(s.age)

