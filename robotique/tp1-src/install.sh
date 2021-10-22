#!/bin/bash
python3 -m pip install --upgrade pip
python3 -m pip install virtualenv
python3 -m virtualenv tp1-env
source tp1-env/bin/activate
pip install numpy pygame
