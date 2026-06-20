__version__ = "1.7.6"

import importlib

from .base import *
from .font import *

_sub_ = ["colormap", "cosmetics", "traffic", "utils"]


def __dir__():
    return sorted(list(globals().keys()) + _sub_)


def __getattr__(name):
    if name in _sub_:
        module = importlib.import_module(f".{name}", __name__)
        globals()[name] = module
        return module
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
