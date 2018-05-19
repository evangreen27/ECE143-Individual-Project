import random
import cTower

towerPossibilities = []
def coverage(n, coverageW, coverageH):
    assert isinstance(n,int)
    assert isinstance(coverageW,int)
    assert isinstance(coverageH,int)
    assert n > 0
    assert coverageW > 0
    assert coverageH > 0

    towerList = []
    startList = []
    area = coverageH * coverageW
    global towerPossibilities


    while len(towerList) < n:
        if(isFilled(towerList,area)):
            #print("area filled completely")
            return (towerList,startList, findArea(towerList))
        towerPossibilities = []
        newTower = createTower(coverageW,coverageH)
        #print("-----------newtower: %s") % (newTower)
        if(len(towerList) == 0):
            towerList.append(newTower)
            startList.append(newTower)
        else:
            trimTower(newTower,towerList)
            if(len(towerPossibilities) > 0):
                towerPossibilities = sorted(towerPossibilities, key=lambda x: x[0])
                towerList.append(towerPossibilities[-1][1])
                startList.append(newTower)


    return (towerList,startList, findArea(towerList))

def fullCoverage(coverageW, coverageH):
    assert isinstance(coverageW,int)
    assert isinstance(coverageH,int)
    assert coverageW > 0
    assert coverageH > 0

    towerList = []
    area = coverageH * coverageW
    global towerPossibilities


    while isFilled(towerList,area) != True:
        towerPossibilities = []
        newTower = createTower(coverageW,coverageH)
        #print("-----------newtower: %s") % (newTower)
        if(len(towerList) == 0):
            towerList.append(newTower)
        else:
            trimTower(newTower,towerList)
            if(len(towerPossibilities) > 0):
                towerPossibilities = sorted(towerPossibilities, key=lambda x: x[0])
                towerList.append(towerPossibilities[-1][1])

    return (len(towerList))

def createTower(coverageW,coverageH):
        width = random.randint(1,coverageW)
        height = random.randint(1,coverageH)
        x = random.randint(0,coverageW-width)
        y = random.randint(0,coverageH-height)
        return cTower.cTower((x,y),width,height)

def isFilled(towerList,area):
    totalArea = 0
    for tower in towerList:
        totalArea = totalArea + tower.area
    if(totalArea == (area)):
        return True
    return False

def findArea(towerList):
    totalArea = 0
    for tower in towerList:
        totalArea = totalArea + tower.area
    return totalArea

def trimTower(newTower,towerList):
    global towerPossibilities
    tower1 = None
    tower2 = None
    tower3 = None
    tower4 = None
    trimmed = False
    for tower in towerList:
        #print("Checking if %s overlaps %s") % (newTower,tower)
        if (newTower.left < tower.right and newTower.right > tower.left and newTower.top > tower.bot and newTower.bot < tower.top):
            #print("%s Does overlap %s") % (newTower,tower)

            if(tower.top < newTower.top): # trim bottom
                tower1 = cTower.cTower((newTower.left,newTower.bot + (tower.top - newTower.bot)),newTower.width,newTower.height - (tower.top - newTower.bot))
                #print("trim bottom")
                trimTower(tower1,towerList)
                trimmed = True

            if(tower.bot > newTower.bot): # trim top
                tower2 = cTower.cTower((newTower.left,newTower.bot),newTower.width,newTower.height - (newTower.top - tower.bot))
                #print("trim top")
                trimTower(tower2,towerList)
                trimmed = True

            if(tower.right < newTower.right): #trim left
                tower3 = cTower.cTower((newTower.left + (tower.right - newTower.left),newTower.bot),newTower.width - (tower.right - newTower.left),newTower.height)
                #print("trim left")
                trimTower(tower3,towerList)
                trimmed = True

            if(tower.left > newTower.left): #trim right
                 tower4 = cTower.cTower((newTower.left,newTower.bot),newTower.width - (newTower.right - tower.left),newTower.height)
                 #print("trim right")
                 trimTower(tower4,towerList)
                 trimmed = True

            if(trimmed == False):
                #Completely inside, dont add it
                #print("Completely inside, dont add it")
                return 0
        else:
            #print("Does not overlap")
            continue
            
    if((tower1 is None) and (tower2 is None) and (tower3 is None) and (tower4 is None)):
        towerPossibilities.append((newTower.area,newTower))

    return 0
