import matplotlib
import colors

matplotlib.rcParams['font.family'] = 'serif'
matplotlib.rcParams['font.serif'] = ['Arial']
matplotlib.rcParams['font.sans-serif'] = ['System Font', 'Verdana', 'Arial']
matplotlib.rcParams['figure.figsize'] = (8, 4)   # Change the size of plots
matplotlib.rcParams['figure.dpi'] = 108

highlight = [0.85, 0.96, 0]

# Color array N x 3
cl = list(colors.colors.items())

idx = [410, 303, 290, 401, 536, 536, 130, 127, 271, 15, 547, 513, 90, 56, 267, 373, 460, 87, 452, 105, 521, 476, 348, 166, 356, 495, 8, 44, 517, 118, 124, 355, 229, 217, 202, 181, 125, 211, 284, 309, 457, 21]

swatch = [cl[x] for x in idx]
swatchn = [[c[1].red, c[1].green, c[1].blue] for c in swatch]

def showSwatch(swatch, M=6):
    fig = matplotlib.pyplot.figure(figsize=(9, 4), dpi=216)
    ax = fig.add_axes([0, 0, 1, 0.92], frameon = False)
    for i in range(42):
        x = i % M
        y = M - i // M
        c = swatch[i]
        #print('{0:.2f},{1:.2f} -> {2}'.format(x, y, c[1].hex_format()))
        matplotlib.pyplot.plot(x, y, '.', markersize=50, color=c[1].hex_format())
        matplotlib.pyplot.text(x + 0.004, y - 0.03, str(i), color='white', va='center', ha='center')
        matplotlib.pyplot.text(x + 0.15, y - 0.03, c[0], va='center')
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    ax.set_xlim([-0.15, M])
    ax.set_ylim([-0.5, M + 0.5])
    fig.suptitle('Swatch', fontweight='bold')
    return fig
