#!/bin/bash
set -x
set -e

# Special case for https://github.com/QubitPi/glassfish-hk2
# Because they put doc source code in gh-pages, a branch which is supposed to be automatically managed
# This is not the dominant practice and I won't sacrifice the generality of my script for this single repo
# Some preliminary setup:
#
# cd daily-sync/
# git clone git@github.com:QubitPi/glassfish-hk2.git
# cd glassfish-hk2
# git checkout gh-pages
# git remote add upstream git@github.com:eclipse-ee4j/glassfish-hk2.git
cd daily-sync/glassfish-hk2/
git fetch upstream
git rebase upstream/gh-pages
git push origin gh-pages -f
cd ../../
