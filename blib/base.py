import matplotlib
import cycler

from .colors import colors

def setColorCycleX():
    n = [5, 11, 29, 21, 15, 39, 6, 34, 9, 27, 20, 38]
    c = []
    for i in n:
        c.append(swatch[i][1].hex_format())
    matplotlib.rcParams['axes.prop_cycle'] = cycler.cycler(color=c)

def setColorCycle(column=3):
    c = []
    for i in range(column, len(swatch), 6):
        c.append(swatch[i][1].hex_format())
    matplotlib.rcParams['axes.prop_cycle'] = cycler.cycler(color=c)

#
# Some default parameters I'd like to use
#

def useTheme(theme='light'):
    props = {
        'font.family': 'sans-serif',
        'font.sans-serif': ['Helvetica', 'Arial', 'Lucida Grande', 'DejaVu Sans'],
        'figure.figsize': (8, 4),
        'figure.dpi': 108,
        'legend.frameon': False,
        'lagend.labelspacing': 0.5,
        'axes.linewidth': 0.5,
        'axes.labelsize': 10,
        'axes.labelpad': 4.0,
        'axes.labelweight': 'normal',
        'axes.titleweight': 'normal',
        'axes.titlesize': 12,
        'axes.titlepad': 6.0,
    }
    if theme == 'light':
        props.update({
            'figure.facecolor': 'white',
            'axes.facecolor': (1, 1, 1, 0.9),
            'axes.edgecolor': 'black',
            'axes.labelcolor': 'black',
            'grid.color': 'black',
            'xtick.color': 'black',
            'ytick.color': 'black',
            'hatch.color': 'black',
            'text.color': 'black',
            'legend.facecolor': 'white',
            'legend.edgecolor': 'black',
            'lines.markeredgecolor': 'black',
            'lines.markerfacecolor': 'black'
        })
    elif theme == 'dark':
        props.update({
            'figure.facecolor': 'black',
            'axes.facecolor': (0, 0, 0, 0.9),
            'axes.edgecolor': 'white',
            'axes.labelcolor': 'white',
            'grid.color': 'white',
            'xtick.color': 'white',
            'ytick.color': 'white',
            'hatch.color': 'white',
            'text.color': 'white',
            'legend.facecolor': 'black',
            'legend.edgecolor': 'white',
            'lines.markeredgecolor': 'white',
            'lines.markerfacecolor': 'white'
        })
    for keys in props:
        matplotlib.rcParams[keys] = props[keys]

highlight = [0.85, 0.96, 0]

# Make a list out of it
colorList = list(colors.items())

# The first color palette
idx = [433, 303, 290, 401, 537, 336, 129, 127, 270, 15, 142, 513, 90, 56, 325, 373, 460, 87, 59, 517, 521, 476, 348, 343, 356, 286, 107, 108, 531, 118, 124, 124, 229, 217, 202, 179, 404, 213, 544, 516, 482, 21]

swatch = [colorList[x] for x in idx]
swatchn = [[c[1].red, c[1].green, c[1].blue] for c in swatch]
swatchInHex = [x[1].hex_format() for x in swatch]

idx = [5, 11, 29, 21, 15, 39, 6, 34, 9, 27, 20, 38]
linecolors = [swatchInHex[i] for i in idx]

setColorCycleX()
