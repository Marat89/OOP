from conftest import triangle


def test_get_perimetr_square(square):
    assert square.perimetr == 40


def test_get_area_square(square):
    assert square.area == 100

def test_get_perimetr_square(square):
    assert square.add_perimetr(triangle) == 73


