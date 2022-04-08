import math
from src.figure import Figure
from src.square import Square


# from src.circle import Circle
# from src.rectangle import Rectangle


class Triangle(Figure):
    name = "triangle"

    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.name = "triangle"
        if side1 >= side2 + side3 or side2 >= side1 + side3 or side3 >= side1 + side2:
            raise ValueError("None")

    @property
    def perimetr(self):
        return self.side1 + self.side2 + self.side3

    @property
    def area(self):
        return math.sqrt(self.perimetr / 2 * (self.perimetr / 2 - self.side1) * (self.perimetr / 2 - self.side2) * (
                self.perimetr / 2 - self.side3))

    def add_perimetr(self, figure2):
        if isinstance(figure2, Figure):
            return figure2.perimetr + self.perimetr
        else:
            raise ValueError("Неправильное значение")

    def add_area(self, figure2):
        if isinstance(figure2, Figure):
            return figure2.area + self.area
        else:
            raise ValueError("Неправильное значение")


square = Square(10)
triangl = Triangle(10,12,13)
print(triangl.perimetr)
