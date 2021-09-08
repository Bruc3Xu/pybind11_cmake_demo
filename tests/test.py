# -*- coding: utf-8 -*-
import unittest

import cmake_example as m


class MyTest(unittest.TestCase):
    def test_add(self):
        self.assertAlmostEqual(m.add_pi(1, 2), 3 + 3.1415926, 0.00001)
        self.assertEqual(m.add(1, 2), 3)

    def test_subtract(self):
        self.assertEqual(m.subtract(1, 2), -1)

    def test_divide(self):
        self.assertEqual(m.divide(1, 4), 0.25)
        self.assertEqual(m.divide(20, 4), 5.0)
        self.assertEqual(m.divide(2, 0), -1.0)


if __name__ == '__main__':
    unittest.main()
