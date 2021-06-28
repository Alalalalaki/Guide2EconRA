"""
This code is used to add paths to system path so that ipynb can import python files in other folders
"""

import sys
import os


def addpath(path="Code"):
    "default path at parent directory"
    module_path = os.path.abspath(os.path.join(os.pardir, path))
    if module_path not in sys.path:
        sys.path.append(module_path)
