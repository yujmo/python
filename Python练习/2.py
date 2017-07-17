#!/usr/bin/python
class Student(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score
    def print_score(self):
        print('%s:%s' % (self.__name,self.__score))
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    def set_score(self,score):
        self.__score = score


bart = Student('Bart Simpson',69)
bart.print_score()
bart.set_score(59)
bart.print_score()
print(bart._Student__score)
