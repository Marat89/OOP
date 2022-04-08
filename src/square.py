from src.figure import Figure
#from src.circle import Circle
#from src.rectangle import Rectangle
#from src.triangle import Triangle


class Square(Figure):
    name = "square"

    def __init__(self, side):
        self.side = side
        self.name = "square"
        if side <= 0:
            raise ValueError("None")

    @property
    def area(self):
        return self.side * self.side

    @property
    def perimetr(self):
        return self.side * 4

    def add_perimetr(self, figure2):
        if isinstance(figure2, Figure):
            return self.perimetr + figure2.perimetr
        else:
            raise ValueError("Неправильное значение")

    def add_area(self, figure2):
        if isinstance(figure2, Figure):
            return figure2.area + self.area
        else:
            raise ValueError("Неправильное значение")
