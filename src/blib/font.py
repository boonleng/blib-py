def getFontOfWeight(weight, prefix="NotoSans"):
    import os
    import matplotlib.font_manager as fm

    weight_names = ["Thin", "ExtraLight", "Light", "Regular", "Medium", "SemiBold", "Bold", "ExtraBold", "Black"]
    fontpath = os.path.join(os.path.dirname(__file__), "fonts")
    if isinstance(weight, int):
        index = min(max(weight // 100 - 1, 0), 8)
        name = f"{prefix}-{weight_names[index]}.ttf"
    else:
        name = f"{prefix}-{weight}.ttf"
    path = os.path.join(fontpath, name)
    if not os.path.exists(path):
        print(f"{path} not found")
        return None
    return fm.FontProperties(fname=path)
