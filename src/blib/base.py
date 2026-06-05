#
# Some default parameters I'd like to use
#


def useTheme(theme="light"):
    import matplotlib
    import matplotlib.colors
    from cycler import cycler

    props = {
        "font.family": "sans-serif",
        "font.sans-serif": ["Helvetica", "Arial", "Lucida Grande", "DejaVu Sans"],
        "figure.figsize": (8, 4.5),
        "figure.dpi": 108,
        "legend.frameon": False,
        "axes.linewidth": 0.5,
        "axes.labelsize": 10,
        "axes.labelpad": 4.0,
        "axes.labelweight": "normal",
        "axes.titleweight": "normal",
        "axes.titlesize": 12,
        "axes.titlepad": 6.0,
        "grid.linewidth": 0.5,
        "lines.linewidth": 0.9,
    }
    if "-hd" in theme:
        props.update(
            {
                "figure.dpi": 144,
                "grid.linewidth": 0.4,
                "lines.linewidth": 0.7,
            }
        )
    if "dark" in theme:
        props.update(
            {
                "figure.facecolor": "black",
                "axes.facecolor": (0, 0, 0, 0.9),
                "axes.edgecolor": "white",
                "axes.labelcolor": "white",
                "grid.color": (0.3, 0.3, 0.3),
                "grid.linestyle": "-",
                "xtick.color": "white",
                "ytick.color": "white",
                "hatch.color": "white",
                "text.color": "white",
                "legend.frameon": True,
                "legend.facecolor": (0.1, 0.1, 0.1, 0.1),
                "legend.edgecolor": "white",
            }
        )
        mc = [
            "mediumturquoise",
            "gold",
            "hotpink",
            "chartreuse",
            "dodgerblue",
            "darkorange",
            "mediumpurple",
            "crimson",
            "grey",
            "rosybrown",
        ]
    elif "light" in theme:
        props.update(
            {
                "figure.facecolor": "white",
                "axes.facecolor": (1, 1, 1, 0.9),
                "axes.edgecolor": "black",
                "axes.labelcolor": "black",
                "grid.color": (0.7, 0.7, 0.7),
                "grid.linestyle": ":",
                "xtick.color": "black",
                "ytick.color": "black",
                "hatch.color": "black",
                "text.color": "black",
                "legend.frameon": True,
                "legend.facecolor": (1, 1, 1, 0.1),
                "legend.edgecolor": "black",
            }
        )
        mc = [
            "steelblue",
            "darkorange",
            "forestgreen",
            "crimson",
            "blueviolet",
            "saddlebrown",
            "hotpink",
            "grey",
            "darkkhaki",
            "mediumturquoise",
        ]
    else:
        raise ValueError("Unknown theme: {}".format(theme))
    for keys in props:
        matplotlib.rcParams[keys] = props[keys]

    dd = {k[0]: k[1] for k in matplotlib.colors.CSS4_COLORS.items()}
    cc = [dd[m] for m in mc]
    matplotlib.rcParams["axes.prop_cycle"] = cycler(color=cc)


def cplot(t, x=None):
    import numpy as np
    import matplotlib.pyplot as plt

    if x is None:
        x = t
        t = np.arange(len(t))
    a = np.abs(x)
    m = np.max(a) * 1.3
    h1 = plt.plot(t, x.real, label="I", zorder=4)
    h2 = plt.plot(t, x.imag, label="Q", zorder=3)
    h3 = plt.plot(t, a, label="A", linewidth=0.8, zorder=2)
    plt.legend(loc="lower left", ncol=3)
    plt.gca().set(ylim=[-m, m])
    plt.grid()
    return [*h1, *h2, *h3]
