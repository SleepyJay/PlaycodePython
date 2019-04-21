#!/usr/bin/python

import unittest
import sys, os
import glob
import inspect

"""Run tests with modules in higher up folders (see README)"""


def run_tests(rel_tests_dir='tests', rel_modules_path='..', tests_pattern='test_*.py'):
    filename = caller_file(2)

    # Add this to use package modules
    base_dir  = os.path.dirname(filename)
    proj_root = os.path.abspath(os.path.join(base_dir, rel_modules_path))
    sys.path.insert(0, proj_root)

    # now find tests
    tests_glob = os.path.join(base_dir, rel_tests_dir, tests_pattern)
    test_file_strings = glob.glob(tests_glob)

    # create unittest objects
    loader = unittest.TestLoader()
    suite  = unittest.TestSuite()

    # iterate over tests files
    for f_str in test_file_strings:
        fname = os.path.basename(f_str)
        mod = __import__('tests.' + os.path.splitext(fname)[0], fromlist=[''])
        suite.addTests(loader.loadTestsFromModule(mod))

    # initialize a runner, pass it your suite and run it
    runner = unittest.TextTestRunner(verbosity=3)
    return runner.run(suite)


# Note, this goes back three stacks, i.e. for [foo -> run_tests -> _caller_file], we want 'foo'.
def caller_file(backwards=2):
    frame = inspect.stack()[backwards]
    module = inspect.getmodule(frame[0])
    return module.__file__


