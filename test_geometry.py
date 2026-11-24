import unittest
from geometry import triangle_area, triangle_perimetr
from geometry import square_area, square_perimetr


class GeometryTestCase(unittest.TestCase):

    def test_triangle_area(self):
        res = triangle_area(10, 5)
        self.assertEqual(res, 25)

    def test_triangle_area_zero(self):
        res = triangle_area(10, 0)
        self.assertEqual(res, 0)

    def test_triangle_area_fraction(self):
        res = triangle_area(3, 5)
        self.assertEqual(res, 7.5)

    def test_triangle_perimetr(self):
        res = triangle_perimetr(3, 4, 5)
        self.assertEqual(res, 12)

    def test_triangle_perimetr_equilateral(self):
        res = triangle_perimetr(5, 5, 5)
        self.assertEqual(res, 15)

    def test_triangle_perimetr_fraction(self):
        res = triangle_perimetr(2.5, 3.5, 4)
        self.assertEqual(res, 10)

    def test_square_area(self):
        res = square_area(10)
        self.assertEqual(res, 100)

    def test_square_area_zero(self):
        res = square_area(0)
        self.assertEqual(res, 0)

    def test_square_area_fraction(self):
        res = square_area(2.5)
        self.assertEqual(res, 6.25)

    def test_square_perimetr(self):
        res = square_perimetr(10)
        self.assertEqual(res, 40)

    def test_square_perimetr_zero(self):
        res = square_perimetr(0)
        self.assertEqual(res, 0)

    def test_square_perimetr_fraction(self):
        res = square_perimetr(2.5)
        self.assertEqual(res, 10)