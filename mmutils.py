#!/usr/bin/env python
import numpy as np
import pickle
from pint import UnitRegistry


'''
-----------
mmutils
-----------
'''
__version__ = 1.0

# Definition of the unit registry and Quantity function.
ureg = UnitRegistry()
ureg.enable_contexts('spectroscopy')
Quantity = ureg.Quantity


# Pickling functions
def pickle_save(variable, fname='file.pkl'):
    with open(fname, 'wb') as f:
        pickle.dump(variable, f)
    print(f'Variable saved to {fname} file.')


def pickle_read(fname='file.pkl'):
    with open(fname, 'rb') as f:
        variable = pickle.load(f)
    return variable
