import matplotlib.patches as patches
import calcCoverage

def prepRectangles(towerList):
    rects = []
    color = [(0.1,0.1,0.8,0.9), (0.1,1,0.2,0.9), (1,0,0.1,0.9), (0.5,0.05,0.5,0.9), (0.9,0.9,0,0.9), (0.2,0.2,0.2,0.3), (0.7,0.1,0.9,0.9), (0.6,0.6,0.6,0.9), (0.3,0.5,0.6,0.9), (0.2,0.1,0.6,0.9), (0.7,0.7,0.2,0.9)]
    edge = (0,0,0,1)
    colorsize = len(color)
    for idx,tower in enumerate(towerList):
            rect = patches.Rectangle((tower.left,tower.bot),tower.width,tower.height, fc=color[idx%colorsize] ,ec=edge)
            rects.append(rect)

    return rects