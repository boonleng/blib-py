#!/usr/bin/env python3
import platform
hostname = platform.node()
if hostname == 'dawn':
	c = [202, 50, 27]
elif hostname == 'tiffany':
	c = [33, 121, 226]
else:
	c = [33, 121, 226]

import sys
sys.ps1='\033[38;5;{}m>\033[38;5;{}m>\033[38;5;{}m>\033[0m '.format(c[0], c[1], c[2])
sys.ps2='\033[38;5;214m...\033[0m '

import matplotlib
matplotlib.rcParams['font.family'] = 'serif'
matplotlib.rcParams['font.serif'] = ['Arial', 'Helvetica']
matplotlib.rcParams['font.sans-serif'] = ['System Font', 'Verdana', 'Arial']
matplotlib.rcParams['figure.figsize'] = (8.89, 5)   # Change the size of plots
matplotlib.rcParams['figure.dpi'] = 144

