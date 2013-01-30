#!/bin/bash
# use ./jenkins.sh keep-env to keep current virtualenv

PACKAGE='rst2html5'

if [ -z "$WORKSPACE" ]; then
    WORKSPACE=$(pwd)
fi
if [ -d metrics ]; then
    rm -rf metrics
fi
mkdir metrics
if [ ${1:-''} == 'keep-env' ] && [ -d $WORKSPACE/env ]; then
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

echo "PACKAGE = $PACKAGE"
nosetests --verbose --with-xunit --xunit-file=$WORKSPACE/metrics/xunit.xml \
    --with-coverage --cover-xml --cover-package=$PACKAGE --cover-branches \
    --cover-xml-file=$WORKSPACE/metrics/coverage.xml

echo sloccount...
sloccount --duplicates --wide --details . | \
     egrep -v '/(env|doc|metrics|build)/' > ./metrics/sloccount.sc

echo pyflakes...
find . -name "*.py" | egrep -v '^./(env|doc|metrics|build)'  \
    | xargs pyflakes  > ./metrics/pyflakes.log

echo pylint...
find . -name "*.py" | egrep -v '^./(env|doc|metrics|build)' \
    | xargs pylint --output-format=parseable --reports=y > ./metrics/pylint.log

echo pep8...
pep8 --exclude="env,build,doc" . > ./metrics/pep8.log

echo clonedigger...
clonedigger -o ./metrics/clonedigger.xml --ignore-dir=env \
    --ignore-dir=build --ignore-dir=doc --ignore-dir=tests --cpd-output .

deactivate