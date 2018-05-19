# @author Evan Green
# @date May 17, 2018


class cTower(object):
    '''
    Defines a cTower Class object
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

    @property
    def bottom_right(self):
        return (self.bottom_left[0] + self.width, self.bottom_left[1])

    @property
    def top_left(self):
        return (self.bottom_left[0], self.bottom_left[1] + self.height)
    
    @property
    def top_right(self):
        return (self.bottom_left[0] + self.width, self.bottom_left[1] + self.height)

    @property
    def area(self):
        return self.width * self.height

    @property
    def points(self):
        return [bottom_right,bottom_left,top_right,top_left]

    @property
    def top(self):
        return self.top_left[1]

    @property
    def bot(self):
        return self.bottom_left[1]

    @property
    def left(self):
        return self.top_left[0]

    @property
    def right(self):
        return self.top_right[0]
    
    def __repr__(self):
        return 'tower(%s,%d,%d)' % (self.bottom_left,self.width,self.height)

    def __eq__(self,other):
        return ((self.left,self.bot) == (other.left,other.bot) and (self.width == other.width) and (self.height == other.height))

    def __ne__(self,other):
        return ((self.left,self.bot) != (other.left,other.bot) or (self.width != other.width) or (self.height != other.height))