import unittest
from part1 import id_from_seat

class Part1Test(unittest.TestCase):
    def test_1(self):
        input = "BFFFBBFRRR"
        id = 567
        self.assertEquals(id, id_from_seat(input))
    
    def test_2(self):
        input = "FFFBBBFRRR"
        id = 119
        self.assertEquals(id, id_from_seat(input))
    
    def test_3(self):
        input = "BBFFBBFRLL"
        id = 820
        self.assertEquals(id, id_from_seat(input))