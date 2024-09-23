import math 
class ImageArea:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def sosanh(self, other, ax) :
        if ax == "==":
            return self.get_area() == other.get_area()
        elif ax == ">":
            return self.get_area() > other.get_area()
        elif ax == "<":
            return self.get_area() < other.get_area()
        elif ax == '>=':
            return self.get_area() >= other.get_area()
        elif ax == '<=':
            return self.get_area() <= other.get_area()
        elif ax == "!=":
            return self.get_area() != other.get_area()
        else:
            return False


a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)
print(a1.sosanh(a2, "=="))
print(a1.sosanh(a3, "!="))
a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)
print(a1.sosanh(a2, "!="))
print(a1.sosanh(a3, ">="))
a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)
print(a1.sosanh(a2, "<="))
print(a1.sosanh(a3, "<"))