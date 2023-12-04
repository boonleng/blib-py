#!/bin/bash

python setup.py sdist
twine upload --verbose --repository blib-py $(ls -t dist/* | head -n 1)
