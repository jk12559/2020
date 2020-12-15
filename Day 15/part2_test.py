import unittest
from part2 import get_result

class TestPart1(unittest.TestCase):
    def test0(self):
        starting = [0,3,6]
        self.assertEqual(175594, get_result(starting))

    def test1(self):
        starting = [1,3,2]
        self.assertEqual(2578, get_result(starting))

    def test2(self):
        starting = [2,1,3]
        self.assertEqual(3544142, get_result(starting))