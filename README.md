# Boonleng's Python Library

[![][version-shield]][release-link]
[![][python-shield]][python-link]
[![][license-shield]][license-link]

This is a collection of some convenient functions, color schemes, etc. for convenient coding in the future.

## Install Using the Python Package-Management System

```shell
pip install blib-py
```

## Install from Source for System-Wide Usage

Download the project from either GitHub or ARRC GitLab:

```shell
git clone https://github.com/boonleng/blib-py.git
```

or

```shell
git clone https://git.arrc.ou.edu/cheo4524/blib-py.git
```

Change directory to the project folder and install using `pip`.

```shell
cd blib-py
pip install .
```

## Use It Without Instlallation

It is possible to use this library without installation. Assuming that you downloaded the project into the folder `~/Developer/blib-py/src`, you can add the path to Python's search path as follows.

```python
import os
import sys

sys.path.insert(0, os.path.expanduser('~/Developer/blib-py/src'))

import blib
```

## Theme / Colors

A theme can be activated by:

```python
blib.useTheme("light")

blib.utils.showLineColors()
```

![light](https://raw.githubusercontent.com/boonleng/blib-py/master/blob/line-colors-light.png)

```python
blib.useTheme("dark")

blib.utils.showLineColors()
```

![dark](https://raw.githubusercontent.com/boonleng/blib-py/master/blob/line-colors-dark.png)

<!-- Link Definitions -->
[version-shield]: https://img.shields.io/github/v/release/boonleng/blib-py
[release-link]: https://github.com/boonleng/blib-py/releases
[python-shield]: https://img.shields.io/badge/python-3.8+-ffd43b?logo=python&logoColor=fff
[python-link]: https://www.python.org
[license-shield]: https://img.shields.io/badge/license-MIT-red
[license-link]: https://github.com/boonleng/blib-py/blob/master/LICENSE
