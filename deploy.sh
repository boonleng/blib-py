#!/bin/bash

python -m build --no-isolation

version=$(grep "__version__" src/blib/__init__.py | awk -F'"' '{print $2}')
archive=$(ls -t dist/blib-py-${version}.tar.gz)

echo "version = ${version}   archive = ${archive}"

twine upload --verbose --repository blib-py ${archive}
