#!/usr/bin/env python
import os, sys
from automated_test import automatedTest 
from celery import Celery

app = Celery('tasks', broker = 'pyamqp://guest@localhost//')

def load_test(testPath):
   
    moduleName = testPath.strip()

    moduleDir = os.path.dirname(moduleName)
    if moduleDir not in sys.path:
        sys.path.insert(0, moduleDir)

    moduleName = os.path.basename(moduleName)
    if moduleName.endswith('.py'):
        moduleName = moduleName[:-3]

    module = __import__(moduleName)
    sys.path.pop(sys.path.index(moduleDir))

    objs = dir(module)
    for objname in objs:
        obj = getattr(module,objname)
        try:
            if obj not in (automatedTest,):
                if issubclass(obj,automatedTest):
                    return obj
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
