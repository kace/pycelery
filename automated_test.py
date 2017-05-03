#!/usr/bin/env python
# automatedTest - nonexecutable base class

class automatedTest(object):

    def __init__(self, **kargs):
        print kargs

    def pre(self):
        print "PRETEST"
        pass

    def run(self):
        print "TEST"
        return True

    def post(self):
        print "POSTTEST"
        pass
