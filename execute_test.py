#!/usr/bin/env python
import imp
from automated_test import automatedTest 
from celery import Celery

app = Celery('tasks', broker = 'pyamqp://guest@localhost//')

def load_test(testPath):
    if testPath.endswith('.py'):
        testPath = testPath[:-3]
    module = __import__(testPath)
    objs = dir(module)
    for objname in objs:
        obj = getattr(module,objname)
        try:
            if obj not in (automatedTest,):
                if issubclass(obj,automatedTest):
                    return obj
#            else:
#                raise Exception("Base class automated_test cannot be run")
        except TypeError:
            pass
    raise Exception("No test present in %s" % (testPath))

@app.task
def execute_test(testPath, **kargs):
    testClass = load_test(testPath)
    test = testClass(**kargs)
    test.pre()
    test.run()
    test.post()
