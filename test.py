#!/usr/bin/env python

from automated_test import automatedTest
import time

class test(automatedTest):

    def __init__(self, **kargs):
        self.timeWait=kargs['timeWait']

    def pre(self):
        time.sleep(self.timeWait)
        super(test, self).pre()

    def run(self):
        time.sleep(self.timeWait)
        super(test, self).run()

    def post(self):
        time.sleep(self.timeWait) 
        super(test, self).post()

    def print_test(self):
        print "BASIC TEST"
