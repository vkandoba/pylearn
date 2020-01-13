from unittest import TestCase

from calc import div


class TestCalc(TestCase):
    def test_div(self):
        self.assertTrue(div(10, 5) == 2.0)

    def test_div_by_zero(self):
        self.assertRaises(ZeroDivisionError)