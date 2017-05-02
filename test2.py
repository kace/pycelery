#!/usr/bin/env python

from automated_test import automatedTest
import time

class test2(automatedTest):

    def __init__(self, **kargs):
        pass

    def pre(self):
        super(test2, self).pre()

    def run(self):
        super(test2, self).run()

    def post(self):
        super(test2, self).post()

    def print_test(self):
        print "BASIC2 TEST"
