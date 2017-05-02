#!/usr/bin/env python

from automated_test import automatedTest
import time

class basicTest(automatedTest):

    def pre(self):
        super(basicTest, self).pre()
        time.sleep(1)

    def run(self):
        print "RUNTEST"
        time.sleep(5)

    def post(self):
        print "POSTTEST"
        time.sleep(1) 

    def print_test(self):
        print "BASIC TEST"
