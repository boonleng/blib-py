#!/bin/bash

python setup.py sdist
twine upload --verbose $(ls dist/* | tail -n 1)
