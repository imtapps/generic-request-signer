#!/bin/bash

nosetests --with-xunit --with-xcover --cover-package=generic_request_signer
TEST_EXIT=$?

echo "Flake8 Results"
flake8 generic_request_signer
FLAKE8_EXIT=$?

let JENKINS_EXIT="$TEST_EXIT + $FLAKE8_EXIT"
if [ $JENKINS_EXIT -gt 0 ]; then
    echo "Test exit status:" $TEST_EXIT
    echo "Flake8 exit status:" $FLAKE8_EXIT
    echo "Exiting Build with status:" $JENKINS_EXIT
    exit $JENKINS_EXIT
fi

