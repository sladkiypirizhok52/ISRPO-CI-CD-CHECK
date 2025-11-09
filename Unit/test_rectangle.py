
import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    def test_area_normal(self):
        self.assertEqual(area(5, 10), 50)

    def test_area_zero(self):
        self.assertEqual(area(0, 10), 0)

    def test_perimeter(self):
        self.assertEqual(perimeter(4, 6), 20)

    def test_negative_values(self):
        with self.assertRaises(ValueError):
            area(-2, 5)
