#!/usr/bin/env python
import h5py
import numpy as np
import sys
import os

assert len(sys.argv) == 2, "Please supply one argument, the h5 master file."
assert os.path.exists(sys.argv[1]), "Specified file does not exist"
print(f"Processing master HDF5 file {sys.argv[1]}...")
with h5py.File(sys.argv[1],"r+") as f:
    
print(f"Finished processing HDF5 file {sys.argv[1]}.")
