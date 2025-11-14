# test/conftest.py
import sys
import os

# Insert the project root (parent of this test directory) at front of sys.path
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)