#!/usr/bin/env python
import imp
from automated_test import automatedTest 
from celery import Celery

app = Celery('tasks', broker = 'pyamqp://guest@localhost//')

def load_test(testPath):
    try:
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
            except TypeError:
                pass
        assert "No test present"
    except ImportError:
        assert "No module"

@app.task
def execute_test(testPath):
    testClass = load_test(testPath)
    test = testClass()
    test.pre()
    test.run()
    test.post()
