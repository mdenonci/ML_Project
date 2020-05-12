from win32api import GetSystemMetrics

def getScreenRes():
    resTxt = str(GetSystemMetrics(0)-200) + "x" + str(GetSystemMetrics(1)-200)
    return resTxt