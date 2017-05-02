#!/usr/bin/env python

from automated_test import automatedTest
import time

class test(automatedTest):

    def __init__(self, **kargs):
        self.timeWait=kargs['timeWait']

    def pre(self):
        super(test, self).pre()
        time.sleep(self.timeWait)

    def run(self):
        super(test, self).run()
        time.sleep(self.timeWait)

    def post(self):
        super(test, self).post()
        time.sleep(self.timeWait) 

    def print_test(self):
        print "BASIC TEST"
