#!/usr/bin/python
class Animal(object):
    def run(self):
        print("Animal is running...")
class Dog(Animal):
    def run(self):
        print("Dog is running")
    def eat(self):
        print("Eating is running...")
test = Dog()
test.run()
test.eat()
