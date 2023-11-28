#!/usr/bin/env python3
#
# Recommended usage:
#
# 1) Copy this file to ~/.python_profile
# 2) Add the following line to ~/.bash_profile
#
#    export PYTHONSTARTUP=${HOME}/.python_profile
#
# 3) Restart the terminal for 2) to take effect
#
import platform

hostname = platform.node()
if hostname == "dawn":
    c = [202, 50, 27]
elif hostname == "tiffany":
    c = [33, 121, 226]
else:
    c = [33, 121, 226]

import sys

sys.ps1 = "\033[38;5;{}m>\033[38;5;{}m>\033[38;5;{}m>\033[0m ".format(c[0], c[1], c[2])
sys.ps2 = "\033[38;5;214m...\033[0m "
