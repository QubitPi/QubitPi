#!/bin/bash
set -x
set -e

python3 sync.py -f git@github.com:QubitPi/mlflow.git -u git@github.com:mlflow/mlflow.git -ub master
python3 sync.py -f git@github.com:QubitPi/ubuntu-server-documentation.git -u git@github.com:canonical/ubuntu-server-documentation.git -ub main
