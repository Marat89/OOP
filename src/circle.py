from src.figure import Figure
#from src.square import Square
#from src.triangle import Triangle
#from src.rectangle import Rectangle


class Circle(Figure):

    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14159 * self.radius ** 2

    @property
    def perimetr(self):
        return 2 * (3.14159 * self.radius)

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
