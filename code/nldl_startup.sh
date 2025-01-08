#! /bin/env bash

# Create a symlink to the shared storage in the home directory:
ln -sf /mnt/shared

# Load the required modules:
module load Python/3.11.5-GCCcore-13.2.0
module load git/2.42.0-GCCcore-13.2.0

# Activate the tutorial virtual environment:
source /mnt/shared/nldl_llm_tutorial/bin/activate

# Start Jupyter Lab?
# jupyter-lab --no-browser --ip=0.0.0.0 --port=8888