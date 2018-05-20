# @author Evan Green
# @date May 17, 2018


class cTower(object):
    '''
    This class defines a cTower object, which has a position and dimensions that define its area of coverage.
    The starting position is bottom_left, which is where I will designate the (0,0) origin.
    '''
    def __init__(self,position,width,height):
        assert isinstance(position,tuple)
        assert isinstance(width,int)
        assert isinstance(height,int)
        assert width > 0
        assert height > 0
        self.bottom_left = position
        self.width = width
        self.height = height

    '''
    defines the bottom right corner of the tower
    '''
    @property
    def bottom_right(self):
        return (self.bottom_left[0] + self.width, self.bottom_left[1])

    '''
    defines the top left corner of the tower
    '''
    @property
    def top_left(self):
        return (self.bottom_left[0], self.bottom_left[1] + self.height)
    
    '''
    defines the top right corner of the tower
    '''
    @property
    def top_right(self):
        return (self.bottom_left[0] + self.width, self.bottom_left[1] + self.height)

    '''
    defines the area of the tower, width * height which shows how much coverage this tower has
    '''
    @property
    def area(self):
        return self.width * self.height

    '''
    defines the y value of the top edge of the tower
    '''
    @property
    def top(self):
        return self.top_left[1]

    '''
    defines the y value of the bottom edge of the tower
    '''
    @property
    def bot(self):
        return self.bottom_left[1]

    '''
    defines the x value of the left edge of the tower
    '''
    @property
    def left(self):
        return self.top_left[0]

    '''
    defines the x value of the right edge of the tower
    '''
    @property
    def right(self):
        return self.top_right[0]

    '''
    defines how a tower is displayed upon printing
    '''
    def __repr__(self):
        return 'tower(%s,%d,%d)' % (self.bottom_left,self.width,self.height)

    '''
    defines how to compare one tower to another and check for equality
    '''
    def __eq__(self,other):
        return ((self.left,self.bot) == (other.left,other.bot) and (self.width == other.width) and (self.height == other.height))

    '''
    defines how to compare one tower to another and check for inequality
    '''
    def __ne__(self,other):
        return ((self.left,self.bot) != (other.left,other.bot) or (self.width != other.width) or (self.height != other.height))