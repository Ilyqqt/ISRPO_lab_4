import unittest
import math

from circle import circle_area, circle_perimeter
from square import square_area, square_perimeter

class TestCircle(unittest.TestCase):

    def test_area(self):
        self.assertAlmostEqual(circle_area(1), math.pi, places=7)
        self.assertEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(2), 4 * math.pi, places=7)

    def test_perimeter(self):
        self.assertAlmostEqual(circle_perimeter(1), 2 * math.pi, places=7)
        self.assertEqual(circle_perimeter(0), 0)
        self.assertAlmostEqual(circle_perimeter(2), 4 * math.pi, places=7)

class TestSquare(unittest.TestCase):

    def test_area_square(self):
        self.assertEqual(square_area(2), 4)
        self.assertEqual(square_area(0), 0)
        self.assertEqual(square_area(5), 25)

    def test_perimeter_square(self):
        self.assertEqual(square_perimeter(2), 8)
        self.assertEqual(square_perimeter(0), 0)
        self.assertEqual(square_perimeter(5), 20)


if __name__ == '__main__':
    unittest.main()
