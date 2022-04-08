import pytest
from src.circle import Circle
from src.square import Square
from src.triangle import Triangle
from src.rectangle import Rectangle


# Фикстура квадрата
@pytest.fixture
def square():
    square = Square(10)
    yield square
    del square

# Фикстура прямоугольника
@pytest.fixture
def rectangle():
    rectangle = Rectangle(10, 10)
    yield rectangle
    del rectangle


# Фикстура круга
@pytest.fixture
def circle():
    circle = Circle(10)
    yield circle
    del circle


# Фикстура треугольника
@pytest.fixture
def triangle():
    triangle = Triangle(10, 11, 12)
    yield triangle
    del triangle


