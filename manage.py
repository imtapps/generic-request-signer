#!/usr/bin/env python

import sys
from nose.core import run

if __name__ == '__main__':
    # This is a hack to get around the fact that this project does not use Django
    sys.argv = sys.argv[:1] + sys.argv[2:]
    run(*[], **{})
