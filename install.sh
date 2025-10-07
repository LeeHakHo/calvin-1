#!/bin/bash

# Ensure build helpers are available first so older packages that rely on
# setuptools' legacy options or scikit-build can be built correctly.
# Pin setuptools to 57.5.0 (older projects in this repo expect legacy behavior)
# and install scikit-build and setuptools_scm which some packages require.
pip install --upgrade pip
pip install wheel setuptools==57.5.0 scikit-build setuptools_scm

# Wheel is never depended on, but always needed. MulticoreTSNE requires lower CMake version
pip install cmake==3.18.4

cd calvin_env/tacto
pip install -e .
cd ..
pip install -e .
cd ../calvin_models
pip install -e .
