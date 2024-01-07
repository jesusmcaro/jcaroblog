#!/bin/bash
echo "##################"
echo "running postcreate.sh"
echo "##################"

# Set up a virtual environment from the poetry.lock file
pip install poetry==1.7.0
python -m venv jcaroblog-dev-venv
source jcaroblog-dev-venv/bin/activate
poetry install

