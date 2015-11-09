#!/bin/bash

virtualenv testing
. testing/bin/activate

find . -name "*.pyc" -delete

pip install -e ~/Projects/apysigner
pip install -r requirements/test.txt

nosetests --with-xunit --with-xcover --cover-package=generic_request_signer
TEST_EXIT=$?
rm -rf jenkins_reports
mkdir jenkins_reports
pep8 request_signer > jenkins_reports/pep8.report
PEP8_EXIT=$?
pyflakes request_signer > jenkins_reports/pyflakes.report
PYFLAKES_EXIT=$?

# cleanup virtualenv
deactivate
rm -rf testing/

let JENKINS_EXIT="$TEST_EXIT + $PEP8_EXIT + $PYFLAKES_EXIT"
if [ $JENKINS_EXIT -gt 2 ]; then
    echo "Test exit status:" $TEST_EXIT
    echo "PEP8 exit status:" $PEP8_EXIT
    echo "Pyflakes exit status:" $PYFLAKES_EXIT
    echo "Exiting Build with status:" $EXIT
    exit $JENKINS_EXIT
fi

