#!/usr/bin/env python

from automated_test import automatedTest
import time

class fail(automatedTest):

    def run(self):
        return False
