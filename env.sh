#!/bin/bash

# Setup the virtual environment
export virtualenv_dir="venv"
source $virtualenv_dir/bin/activate

# Setup the python path
export PYTHONPATH=src/:src/lib/:$PYTHONPATH


