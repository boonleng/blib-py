#!/bin/bash

python setup.py sdist
twine upload --verbose --repository blib-py $(ls -t dist/* | tail -n 1)
