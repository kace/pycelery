#!/usr/bin/env python

from automated_test import automatedTest
import time

class fail(automatedTest):

    def pre(self):
        time.sleep(self.timeWait)
        super(fail, self).pre()

    def run(self):
        time.sleep(self.timeWait)
        super(fail, self).run()

    def post(self):
        time.sleep(self.timeWait) 
        super(fail, self).post()

    def print_fail(self):
        print "BASIC TEST"
