# Test the conda environment of the python version and autogluon packages
import importlib.metadata as metadata

# output the autogluon version as a sanity check
print("autogluon version: ", metadata.version("autogluon"))

# output the python version as a sanity check as x.x.x format
import sys

print("python version: ", sys.version)
