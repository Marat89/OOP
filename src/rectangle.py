from src.figure import Figure
#from src.square import Square
#from src.circle import Circle
#from src.triangle import Triangle

class Rectangle(Figure):

    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    @property
    def area(self):
        return self.side1 * self.side2

    @property
    def perimetr(self):
        return self.side1 * 2 + self.side2 * 2

    def add_perimetr(self, figure2):
        #if isinstance(figure2, Figure):
            return figure2.perimetr + self.perimetr
        #else:
        #    raise ValueError("Неправильное значение")

    def add_area(self, figure2):
        if isinstance(figure2, Figure):
            return figure2.area + self.area
        else:
            raise ValueError("Неправильное значение")
