#!/usr/bin/python
class Timer(object):
    def run(self):
        print("Timer is running...")

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Timer())
