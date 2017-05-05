#!/usr/bin/env python

from automated_test import automatedTest
import time

class blocked_test(automatedTest):

    def __init__(self, **kargs):
        pass

    def pre(self):
        super(blocked_test, self).pre()

    def run(self):
        print "RUN BLOCKED"
        return 'BLOCKED'

    def post(self):
        super(blocked_test, self).post()
