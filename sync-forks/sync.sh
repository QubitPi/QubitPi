#!/bin/bash
set -x
set -e

python3 sync.py -f git@github.com:QubitPi/leadership-blogs.git -u git@github.com:saicaca/fuwari.git -ub main

# ML
python3 sync.py -f git@github.com:QubitPi/mlflow.git -u git@github.com:mlflow/mlflow.git -ub master

# UI
python3 sync.py -f git@github.com:QubitPi/react.dev.git -u git@github.com:reactjs/react.dev.git -ub main
python3 sync.py -f git@github.com:QubitPi/docusaurus.git -u git@github.com:facebook/docusaurus.git -ub main
python3 sync.py -f git@github.com:QubitPi/jest.git -u git@github.com:jestjs/jest.git -ub main
python3 sync.py -f git@github.com:QubitPi/cypress-documentation.git -u git@github.com:cypress-io/cypress-documentation.git -ub main
python3 sync.py -f git@github.com:QubitPi/redux.git -u git@github.com:reduxjs/redux.git -ub master
python3 sync.py -f git@github.com:QubitPi/react-redux.git -u git@github.com:reduxjs/react-redux.git -ub master
python3 sync.py -f git@github.com:QubitPi/redux-toolkit.git -u git@github.com:reduxjs/redux-toolkit.git -ub master
python3 sync.py -f git@github.com:QubitPi/babel-website.git -u git@github.com:babel/website.git -ub main
python3 sync.py -f git@github.com:QubitPi/TypeScript-Website.git -u git@github.com:microsoft/TypeScript-Website.git -ub v2

# Arango
python3 sync.py -f git@github.com:QubitPi/arangodb-docs.git -u git@github.com:arangodb/docs-hugo.git -ub main
python3 sync.py -f git@github.com:QubitPi/arangodb-java-driver.git -u git@github.com:arangodb/arangodb-java-driver.git -ub main
python3 sync.py -f git@github.com:QubitPi/python-arango.git -u git@github.com:arangodb/python-arango.git -ub main

# Hadoop Ecosystem
python3 sync.py -f git@github.com:QubitPi/hadoop.git -u git@github.com:apache/hadoop.git -ub trunk

# Dev-Ops
python3 sync.py -f git@github.com:QubitPi/MailHog.git -u git@github.com:mailhog/MailHog.git -ub master
python3 sync.py -f git@github.com:QubitPi/linuxserver-documentation.git -u git@github.com:linuxserver/docker-documentation.git -ub master
python3 sync.py -f git@github.com:QubitPi/ubuntu-server-documentation.git -u git@github.com:canonical/ubuntu-server-documentation.git -ub main
python3 sync.py -f git@github.com:QubitPi/docker-mailserver.git -u git@github.com:docker-mailserver/docker-mailserver.git -ub master
