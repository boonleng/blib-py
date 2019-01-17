#!/usr/bin/env python3
import sys
sys.ps1='\033[38;5;33m>\033[38;5;121m>\033[38;5;226m>\033[0m '
sys.ps2='\033[38;5;214m...\033[0m '

import matplotlib
matplotlib.rcParams['font.family'] = 'serif'
matplotlib.rcParams['font.serif'] = ['Arial', 'Helvetica']
matplotlib.rcParams['font.sans-serif'] = ['System Font', 'Verdana', 'Arial']
matplotlib.rcParams['figure.figsize'] = (8.89, 5)   # Change the size of plots
matplotlib.rcParams['figure.dpi'] = 144

