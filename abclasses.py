from abc import ABCMeta, abstractmethod

class Shape(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def area(self): pass

    @abstractmethod  
    def perimeter(self): pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width=width
        self.height=height

        super(Rectangle, self).__init__()
    def area(self):
        print("Using Rectangle area method:")
        return self.width * self.height
    
    def perimeter(self):
        print("Using Rectangle perimeter method")
        return self.width*2+self.height*2
    
class Square(Rectangle):
    def __init__(self, side_length):
        self.side_length=side_length
        super(Square, self).__init__(side_length, side_length)
        
    def area(self):
        print("Using Square area method:")
        return self.width*self.height
    
    def perimeter(self):
        print("Using Square perimeter method:")
        return self.width*2+self.height*2
        
        
rect=Rectangle(5,6)
print(rect.area())
s=Square(4)
print(s.area())
