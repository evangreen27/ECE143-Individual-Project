import random
from cTower import *

towerPossibilities = []
def coverage(n, coverageW, coverageH):
    '''
    This method creates new towers and trims towers that are covering a piece of area already covered by another tower. 
    It will save both the original coverage area of each tower ( oldTowers ) as well as the trimmed coverage area of each tower (newTowers). 
    If a tower is completely covered by a tower already placed, I do not count it toward the number of towers placed total.

    While there are less than n towers placed or the total area is less than desired, I will create a new tower, trim it, and
    determine the possible trimmed tower with the highest area and add that to the list of placed towers.

    Parameters:
        n - the amount of towers we will place onto the grid (at maximum, may be less if it is completely filled earlier)
        coverageW - the width of our coverage area
        coverageH - the height of our coverage area

    Returns:
        towerList - list of all towers after they have been trimmed down to smaller areas
        startList - list of all towers before they were trimmed, exactly as they were upon creation.
        area - the area of all towers after they have been trimmed.
    '''
    
    assert isinstance(n,int)
    assert isinstance(coverageW,int)
    assert isinstance(coverageH,int)
    assert n > 0
    assert coverageW > 0
    assert coverageH > 0

    towerList = []
    startList = []
    area = coverageH * coverageW
    global towerPossibilities #list of possible towers to add after trimming, but will choose one with highest area


    while len(towerList) < n:
        if(isFilled(towerList,area)):
            return (towerList,startList, findArea(towerList))

        #reset possible towers each iteration
        towerPossibilities = []
        newTower = createTower(coverageW,coverageH)
        #print("--------------new %s") % newTower

        if(len(towerList) == 0):
            towerList.append(newTower)
            startList.append(newTower)
        else:
            trimTower(newTower,towerList)
            if(len(towerPossibilities) > 0):
                towerPossibilities = sorted(towerPossibilities, key=lambda x: x[0])
                towerList.append(towerPossibilities[-1][1])
                startList.append(newTower)


    return (towerList,startList,findArea(towerList))

def fullCoverage(coverageW, coverageH):
    '''
    This method creates new towers and trims towers that are covering a piece of area already covered by another tower. 
    It will save both the original coverage area of each tower ( oldTowers ) as well as the trimmed coverage area of each tower (newTowers). 
    If a tower is completely covered by a tower already placed, I do not count it toward the number of towers placed total.

    This method is very similar to the coverage function but with one major difference - it will run until the area is completely filled.
    This means that there is no n parameter, since we will not stop after a certain amount of towers placed.

    Parameters:
        coverageW - the width of our coverage area
        coverageH - the height of our coverage area

    Returns:
        len(towerList) - amount of towers it took to fill the graph.
        we can print out towerList to see the actual towers, but it is not needed in this problem.
    '''
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
    '''
    This method creates a tower which has covers a rectangular area and is randomly given a size and starting position.
    The height and width are determined first so that they will be large, 
    since if I determined the position first then it would decrease the average tower size.

    I use a random integer from 1 to maximum because a tower with 0 width will not have any area.

    I use a position from 0 to coverage - size so that the position + width or height will not be outside the grid bounds.

    Parameters:
        coverageW - maximum height of the tower
        coverageH - maximum width of the tower

    Returns:
        cTower - reference to the tower
    '''
    assert isinstance(coverageW,int)
    assert isinstance(coverageH,int)
    assert coverageW > 0
    assert coverageH > 0

    width = random.randint(1,coverageW)
    height = random.randint(1,coverageH)
    x = random.randint(0,coverageW-width)
    y = random.randint(0,coverageH-height)
    return cTower((x,y),width,height)

def isFilled(towerList,area):
    '''
    This method determines if the grid area is completely covered or not.

    Parameters:
        towerList - list of all towers after they have been trimmed down to smaller areas
        area - the desired area of the entire grid, which we will compare our area against.

    Returns:
        True or False - True if the entire area is covered by the towers in the list.
    '''
    assert isinstance(towerList,list)
    assert isinstance(area,int)
    assert area > 0

    totalArea = 0
    for tower in towerList:
        totalArea = totalArea + tower.area
    if(totalArea == (area)):
        return True
    return False

def findArea(towerList):
    '''
    This method gives the sum of the areas in the towerList, so we can see how much coverage we have.

    Parameters:
        towerList - list of all towers after they have been trimmed down to smaller areas

    Returns:
        totalArea - the sum of the areas in the towerList, representing the total coverage of our towers.
    '''
    assert isinstance(towerList,list)

    totalArea = 0
    for tower in towerList:
        totalArea = totalArea + tower.area
    return totalArea

def trimTower(newTower,towerList):
    '''
    This method will take in a new tower that we want to trim, and trim it down so that it fits on our grid without intersecting with any other tower.
    First, I determine if it is intersecting with any other tower. If it is not, then we can compare it against the other towers.
    If it is intersecting, then we need to know exactly how it is intersecting with the other tower. The easiest way to do this is by checking
    which edges are less than or greater than the other tower's edges. For instance, if we know that two towers intersect and that 
    the new tower's top edge is higher, then we know that we can trim off the bottom to get rid of an intersection with that tower.
    We need to check all four edges, and trim the tower four different ways depending on which cases are true.

    Once a trimmed tower is created, we need to run the function again with that new trimmed tower, since it may not be compatible with
    all the other towers on the grid. This means we will end up forming a large tree of possible towers, and that we will have to sort
    this tree and determine the trimmed tree that gives the highest area later (see the coverage method for this step).

    If we know that the tower does not intersect with any other tower, then we can add it to the possible towers. This means that
    for a large amount of towers, there will be many computations taking place.

    Parameters:
        newTower - The newly created tower that may be freshly created or freshly trimmed, but not completely trimmed
        towerList - The currently placed towers on the grid

    Returns:
        None, since we are updating the towerPossibilities global variable. This needs to be global because each iteration could
        affect the other trimmed towers, so the information needs to be updated as it recurses.
    '''
    assert isinstance(towerList,list)
    assert isinstance(newTower,cTower)

    global towerPossibilities
    tower1 = None
    tower2 = None
    tower3 = None
    tower4 = None
    trimmed = False
    if(len(towerList) == 0):
        towerPossibilities.append((newTower.area,newTower))
        return 0
    tower = towerList[0]
    #print("Checking if %s overlaps %s") % (newTower,tower)
    if (newTower.left < tower.right and newTower.right > tower.left and newTower.top > tower.bot and newTower.bot < tower.top):
        #print("%s Does overlap %s") % (newTower,tower)

        if(tower.top < newTower.top): # trim bottom
            tower1 = cTower((newTower.left,newTower.bot + (tower.top - newTower.bot)),newTower.width,newTower.height - (tower.top - newTower.bot))
            trimTower(tower1,towerList[1:])
            trimmed = True

        if(tower.bot > newTower.bot): # trim top
            tower2 = cTower((newTower.left,newTower.bot),newTower.width,newTower.height - (newTower.top - tower.bot))
            trimTower(tower2,towerList[1:])
            trimmed = True

        if(tower.right < newTower.right): #trim left
            tower3 = cTower((newTower.left + (tower.right - newTower.left),newTower.bot),newTower.width - (tower.right - newTower.left),newTower.height)
            trimTower(tower3,towerList[1:])
            trimmed = True

        if(tower.left > newTower.left): #trim right
            tower4 = cTower((newTower.left,newTower.bot),newTower.width - (newTower.right - tower.left),newTower.height)
            trimTower(tower4,towerList[1:])
            trimmed = True

        if(trimmed == False):
            #Completely inside another placed tower, don't add it
            return 0
    else:
        trimTower(newTower,towerList[1:])
    return 0