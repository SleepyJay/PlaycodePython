#!/usr/bin/python

import sys, os

base_dir = os.path.dirname(__file__)
sys.path.insert(0, os.path.abspath(os.path.join(base_dir, '..')))

from JAGpy import Pyrove

Pyrove.run_tests()
