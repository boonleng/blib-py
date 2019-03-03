import colorsys
import matplotlib
import matplotlib.pyplot
import matplotlib.font_manager
import numpy as np

from .base import *

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

def rgb2lab(rgb):
    rgbv = np.array(rgb) / 255.0
    if len(rgbv.shape) == 1:
        rgbv = rgbv[[np.newaxis]]
    matrix = [[0.412453, 0.357580, 0.180423],
              [0.212671, 0.715160, 0.072169],
              [0.019334, 0.119193, 0.950227]]
    mat = np.array(matrix).transpose()
    xyz = np.matmul(rgbv, mat)
    # Normalize to D65 white point
    x = xyz[:, 0] / 0.950456;
    y = xyz[:, 1]
    z = xyz[:, 2] / 1.088754;
    # Threshold
    T = 0.008856
    xt = (x > T).astype(bool)
    yt = (y > T).astype(bool)
    zt = (z > T).astype(bool)
    y3 = y ** (1.0 / 3.0)
    fX = np.multiply(xt, x ** (1.0 / 3.0)) + np.multiply(~xt, 7.787 * x + 16.0 / 116.0)
    fY = np.multiply(yt, y3)               + np.multiply(~yt, 7.787 * y + 16.0 / 116.0)
    fZ = np.multiply(zt, z ** (1.0 / 3.0)) + np.multiply(~zt, 7.787 * y + 16.0 / 116.0)
    L = np.multiply(yt, 116.0 * y3 - 16.0) + np.multiply(~yt, 903.3 * y)
    a = 500.0 * (fX - fY)
    b = 200.0 * (fY - fZ)
    return np.array([L, a, b]).transpose()

def listFonts(verbose=0, showname=False):
    def make_html(fontname, showname=showname):
        line = '<p><span style="font-family:{font}; font-size:16pt;">{font}</span>'.format(font=fontname)
        if showname:
            line += ' (<span style="color:blue;">{}</span>)'.format(fontname)
        line += '</p>'
        return line
    code = '\n'.join([make_html(font) for font in sorted(set([f.name for f in matplotlib.font_manager.fontManager.ttflist]))])
    if verbose:
        print('Type these in Notebook:\nfrom IPython.core.display import HTML\nHTML(result)')
    html = '<div style="column-count:2;">{}</div>'.format(code)
    return html

def fleximap(count=15, xp=None, cp=None):
    if xp is None and cp is None:
        # Color provided
        cp = [
            [0.5, 0.0, 0.0],
            [1.0, 0.0, 0.0],
            [1.0, 1.0, 1.0],
            [0.0, 0.0, 1.0],
            [0.0, 0.0, 0.5],
        ]
        # X-axis provided
        xp = [0.0, 0.2, 0.5, 0.8, 1.0]
    # If anchors are supplied but not x
    if xp is None:
        xp = np.linspace(0.0, 1.0, len(cp))
    if cp is None:
        print('Supply xp and cp.')
        return None
    cp = np.array(cp)
    xi = np.linspace(0.0, 1.0, count)
    rgb = np.array([np.interp(xi, xp, cp[:, i]) for i in range(3)]).transpose((1, 0))
    return rgb

# from .colorspace import *

def colorspace(rgba):

    # Some constants for convenient coding later
    count = rgba.shape[0]
    x = np.arange(count)
    rgb = rgba[:, :3]

    # Color in HSV representation
    hsv = np.array([colorsys.rgb_to_hsv(r, g, b) for r, g, b in rgb])

    # If image width = 1280, 0.8 x 1280 = 1024
    BACK_RECT = [0.1, 0.11, 0.8, 0.85]
    LINE_RECT = [0.1, 0.41, 0.8, 0.55]
    MAIN_RECT = [0.1, 0.11, 0.8, 0.30]

    linewidth = 1.5

    # New figure
    fig = matplotlib.pyplot.figure(figsize=(8.8889, 5), dpi=144)
    fig.patch.set_alpha(0.0)

    # Background
    axb = fig.add_axes(BACK_RECT, frameon=False)
    axb.yaxis.set_visible(False)
    axb.xaxis.set_visible(False)

    # Main axis for images
    axm = fig.add_axes(MAIN_RECT, label='Images')
    axm.patch.set_visible(False)

    # Line axis for lines
    axl = fig.add_axes(LINE_RECT, label='Lines')
    axl.patch.set_visible(False)
    axl.xaxis.set_visible(False)

    # Draw
    if count <= 64:
        marker = '.'
    else:
        marker = None
    line_r = matplotlib.lines.Line2D(x, rgb[:, 0], linewidth=linewidth, color='r', label='R', marker=marker)
    line_g = matplotlib.lines.Line2D(x, rgb[:, 1], linewidth=linewidth, color='g', label='G', marker=marker)
    line_b = matplotlib.lines.Line2D(x, rgb[:, 2], linewidth=linewidth, color='b', label='B', marker=marker)
    line_h = matplotlib.lines.Line2D(x, hsv[:, 0], linewidth=linewidth, color=linecolors[0], label='H', marker=marker)
    line_s = matplotlib.lines.Line2D(x, hsv[:, 1], linewidth=linewidth, color=linecolors[1], label='S', marker=marker)
    line_v = matplotlib.lines.Line2D(x, hsv[:, 2], linewidth=linewidth, color=linecolors[2], label='V', marker=marker)
    axl.add_line(line_r)
    axl.add_line(line_g)
    axl.add_line(line_b)
    axl.add_line(line_h)
    axl.add_line(line_s)
    axl.add_line(line_v)
    if rgba.shape[1] > 3:
        line_a = matplotlib.lines.Line2D(x, rgba[:, 3], linewidth=linewidth, color='#777777', label='A', marker=marker, linestyle=':')
        axl.add_line(line_a)

    # Backdrop gradient
    cmap = matplotlib.colors.LinearSegmentedColormap.from_list('backdrop', rgb)
    axb.imshow(np.arange(count).reshape(1, -1), cmap=cmap, extent=(0, 1, 0, 1), aspect='auto', alpha=0.2)

    # Various representations of the colors
    clr = np.expand_dims(rgb, axis=0)
    red = np.zeros((1, count, 3)); red[0, :, 0] = rgb[:, 0]
    grn = np.zeros((1, count, 3)); grn[0, :, 1] = rgb[:, 1]
    blu = np.zeros((1, count, 3)); blu[0, :, 2] = rgb[:, 2]
    c = matplotlib.pyplot.get_cmap('hsv');     hue = np.expand_dims(np.array([c(i)[:3] for i in hsv[:, 0]]), axis=0)
    c = matplotlib.pyplot.get_cmap('Purples'); sat = np.expand_dims(np.array([c(i)[:3] for i in hsv[:, 1]]), axis=0)
    c = matplotlib.pyplot.get_cmap('gray');    val = np.expand_dims(np.array([c(i)[:3] for i in hsv[:, 2]]), axis=0)
    # Lower image to show various color components / intrinsic parameters
    if rgba.shape[1] > 3:
        alp = np.expand_dims(np.array([c(i)[:3] for i in rgba[:, 3]]), axis=0)
        img = np.concatenate((clr, red, grn, blu, hue, sat, val, alp), axis=0)
        axm.imshow(img, extent=(-0.5, count-0.5, -0.5, 7.5), aspect='auto')
        axl.set_title('Color Space - RGB, HSV, A', weight='bold')
        axm.set_yticks(range(8))
        _ = axm.set_yticklabels(['Opacity', 'Value', 'Saturation', 'Hue', 'Blue', 'Green', 'Red', 'Swatch'])
    else:
        img = np.concatenate((clr, red, grn, blu, hue, sat, val), axis=0)
        axm.imshow(img, extent=(-0.5, count-0.5, -0.5, 6.5), aspect='auto')
        axl.set_title('Color Space - RGB, HSV', weight='bold')
        axm.set_yticks(range(7))
        _ = axm.set_yticklabels(['Value', 'Saturation', 'Hue', 'Blue', 'Green', 'Red', 'Swatch'])

    # Axis limits, grid, etc.
    axl.set_xlim([-0.5, count - 0.5])
    axl.set_ylim([-0.05, 1.18])
    axl.set_ylabel('Values')
    axl.grid(alpha=0.5, color='k', linestyle=':')
    lines = [line_r, line_g, line_b, line_h, line_s, line_v]
    leg = axl.legend(handles=lines, loc='upper left', ncol=7, frameon=False, fontsize=9)
    axm.set_xlabel('Color Index')

# Extended colormap for reflectivity
# s - shades / element (number of shades for blue, green, etc.)
def zmapx(s=3):
    if (s % 3):
        print('Poor choice of {} shades / element. Recommend either 30, 15, 6 or 3.'.format(s))
    count = round(6.6667 * s) + 2
    n = count - 1
    xp = np.zeros(16)
    for i in range(6):
        xp[2 * i + 1] = round(i * s + 1) / n
        xp[2 * i + 2] = round((i + 1) * s) / n
    xp[13] = round(6 * s + 1) / n
    xp[14] = round(6 * s + 0.6667 * s) / n
    xp[15] = 1.0
    cp = [
        [0.00, 0.00, 0.00],
        [0.80, 0.60, 0.80],    # light purple
        [0.40, 0.20, 0.40],    # dark purple
        [0.80, 0.80, 0.60],    # light dirty
        [0.40, 0.40, 0.40],    # dark gray
        [0.00, 1.00, 1.00],    # cyan
        [0.00, 0.00, 1.00],    # dark blue
        [0.00, 1.00, 0.00],    # light green
        [0.00, 0.50, 0.00],    # dark green
        [1.00, 1.00, 0.00],    # yellow
        [1.00, 0.50, 0.00],    # orange
        [1.00, 0.00, 0.00],    # torch red
        [0.50, 0.00, 0.00],    # dark red
        [1.00, 0.00, 1.00],    # magenta
        [0.56, 0.35, 1.00],    # purple
        [1.00, 1.00, 1.00]     # white
         ]
    return fleximap(count, xp, cp)

# Red green map for velocity
def rgmap(count=16):
    xp = [0.0, 0.3, 0.5, 0.7, 1.0]
    cp = [
        [0.00, 0.20, 0.00],
        [0.00, 0.80, 0.00],
        [0.85, 0.85, 0.85],
        [0.80, 0.00, 0.00],
        [0.20, 0.00, 0.00]
    ]
    return fleximap(count, xp, cp)

# Red green map with forced middle 3 shades
def rgmapf(count=16):
    m = count - 1
    c = np.floor(count / 2)
    xp = [0.0, (c - 2) / m, (c - 1) / m, c / m, (c + 1) / m, (c + 2) / m, 1.0]
    cp = [
        [0.00, 1.00, 0.00],
        [0.00, 0.40, 0.00],
        [0.22, 0.33, 0.22],
        [0.40, 0.40, 0.40],
        [0.33, 0.22, 0.22],
        [0.45, 0.00, 0.00],
        [1.00, 0.00, 0.00]
    ]
    return fleximap(count, xp, cp)

def wmap(s=4):
    if s % 2:
        print('Poor choice of {} shades / element. Recommend either 2, 4, 8 or 16.'.format(s))
    rgb = np.concatenate((
        fleximap(s, [0.0, 1.0], [[0.00, 1.00, 1.00], [0.00, 0.00, 0.85]]),
        fleximap(s, [0.0, 1.0], [[0.00, 0.50, 0.00], [0.00, 1.00, 0.00]]),
        fleximap(s, [0.0, 1.0], [[1.00, 1.00, 0.00], [1.00, 0.50, 0.00]]),
        fleximap(s, [0.0, 1.0], [[1.00, 0.00, 0.00], [0.50, 0.00, 0.00]]),
        fleximap(s, [0.0, 1.0], [[1.00, 0.00, 1.00], [0.50, 0.00, 0.50]]),
        fleximap(s, [0.0, 1.0], [[0.60, 0.22, 1.00], [0.35, 0.11, 0.55]]),
        np.tile([0.20, 0.45, 0.60], int(s / 2)).reshape(-1, 3),
    ))
    return rgb

def dmap():
    xp = [0.00,
          9.0 / 254.0,
         10.0 / 254.0,
         39.0 / 254.0,
         40.0 / 254.0,
         69.0 / 254.0,
         70.0 / 254.0,
         99.0 / 254.0,
        100.0 / 254.0,
        129.0 / 254.0,
        130.0 / 254.0,
        159.0 / 254.0,
        160.0 / 254.0,
        189.0 / 254.0,
        190.0 / 254.0,
        219.0 / 254.0,
        220.0 / 254.0,
        249.0 / 254.0,
        250.0 / 254.0,
        1.00];
    cp = [
        [0.30, 0.45, 0.50],    #
        [0.60, 0.90, 1.00],    #
        [0.45, 0.20, 0.80],    #
        [0.70, 0.40, 1.00],    #
        [0.50, 0.20, 0.35],    #
        [1.00, 0.50, 0.85],    #
        [0.70, 0.50, 0.15],    #
        [1.00, 1.00, 0.85],    #
        [1.00, 1.00, 1.00],    # 0dB
        [0.00, 0.35, 1.00],    #
        [0.10, 1.00, 0.50],    # 3dB
        [0.00, 0.50, 0.00],    #
        [1.00, 1.00, 0.00],    # 6dB
        [1.00, 0.50, 0.00],    # 
        [1.00, 0.00, 0.00],    #
        [0.50, 0.00, 0.00],    #
        [1.00, 0.00, 1.00],    #
        [0.50, 0.00, 0.50],    #
        [1.00, 1.00, 1.00],    #
        [0.60, 1.00, 1.00]     #
    ]
    rgb = fleximap(51, xp, cp)
    rgb = np.expand_dims(rgb, axis=2)
    rgb = np.repeat(rgb, 5, axis=2).transpose((0, 2, 1)).reshape(5 * 51, 3)
    rgb = np.concatenate((rgb, rgb[-1, :].reshape(1, 3)))
    rgba = np.concatenate((rgb, np.ones((256, 1))), axis=1)
    rgba[:11, 3] = 220.0 / 255.0
    rgba[-6:, 3] = 220.0 / 255.0
    return rgba
