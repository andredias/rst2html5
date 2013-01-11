#!/bin/bash

# use ./jenkins.sh keep-env to keep current virtualenv

if [ -z "$WORKSPACE" ]; then
    WORKSPACE=.
fi
if [ -d metrics ]; then
    rm -rf metrics
fi
mkdir metrics
if [ ${1:-''} == 'keep-env' ]; then
    . $WORKSPACE/env/bin/activate
else
    if [ -d env ]; then
        rm -rf env
    fi
    virtualenv env
    . $WORKSPACE/env/bin/activate
    pip install -M -r requirements.txt
    pip install nose coverage
fi

nosetests --verbose --with-xunit --xunit-file=./metrics/xunit.xml --with-coverage \
     --cover-xml --cover-xml-file=../metrics/coverage.xml --cover-package=rst2html5

# sloccount
sloccount --duplicates --wide --details . | \
     egrep -v '/(env|doc|metrics|build)/' > ./metrics/sloccount.sc

# flakes:
find . -name "*.py" | egrep -v '^./(env|doc|metrics|build)'  \
    | xargs pyflakes  > ./metrics/pyflakes.log

#lint:
find . -name "*.py" | egrep -v '^./(env|doc|metrics|build)' \
    | xargs pylint --output-format=parseable --reports=y > ./metrics/pylint.log

pep8 --exclude="env,build,doc" > ./metrics/pep8.log

#clone:
clonedigger -o ./metrics/clonedigger.xml --ignore-dir=env \
    --ignore-dir=build --ignore-dir=doc --ignore-dir=tests --cpd-output .

deactivate