import unittest
from Passport import Passport

class PassportTest(unittest.TestCase):
    def test_valid_constructor(self):
        data = "byr:2024 iyr:2016\neyr:2034 ecl:zzz pid:985592671 hcl:033b48\nhgt:181 cid:166"
        passport = Passport(data)
        self.assertEqual(2024, passport.birth_year)
        self.assertEqual(2016, passport.issue_year)
        self.assertEqual(2034, passport.exp_year)
        self.assertEqual("181", passport.height)
        self.assertEqual("033b48", passport.hair_color)
        self.assertEqual("zzz", passport.eye_color)
        self.assertEqual("985592671", passport.id)
        self.assertEqual("166", passport.country_id)

    def test_invalid_constructor(self):
        data = "eyr:2034 ecl:zzz pid:985592671 hcl:033b48\nhgt:181 cid:166"
        passport = Passport(data)
        self.assertIsNone(passport.birth_year)
        self.assertIsNone(passport.issue_year)
        self.assertEqual(2034, passport.exp_year)
        self.assertEqual("181", passport.height)
        self.assertEqual("033b48", passport.hair_color)
        self.assertEqual("zzz", passport.eye_color)
        self.assertEqual("985592671", passport.id)
        self.assertEqual("166", passport.country_id)

    def test_is_not_valid(self):
        data = "eyr:2034 ecl:zzz pid:985592671 hcl:033b48\nhgt:181 cid:166"
        passport = Passport(data)
        self.assertFalse(passport.is_valid())

    def test_valid_birth_year(self):
        data = ["byr:1900", "byr:2020", "byr:1920", "byr:2002", "byr:2000"]
        expected = [False, False, True, True, True]
        for i in range(len(data)):
            passport = Passport(data[i])
            self.assertEqual(expected[i], passport.valid_birth_year(), data[i])

    def test_valid_issue_year(self):
        data = ["iyr:1900", "iyr:2030", "iyr:2010", "iyr:2020", "iyr:2015"]
        expected = [False, False, True, True, True]
        for i in range(len(data)):
            passport = Passport(data[i])
            self.assertEqual(expected[i], passport.valid_issue_year(), data[i])

    def test_valid_exp_year(self):
        data = ["eyr:1900", "eyr:2040", "eyr:2020", "eyr:2030", "eyr:2025"]
        expected = [False, False, True, True, True]
        for i in range(len(data)):
            passport = Passport(data[i])
            self.assertEqual(expected[i], passport.valid_exp_year(), data[i])

    def test_valid_height(self):
        data = ["hgt:111", "hgt:50in", "hgt:80in", "hgt:59in", "hgt:76in", "hgt:65in", "hgt:65cm", "hgt:200cm", "hgt:150cm", "hgt:193cm", "hgt:175cm"]
        expected = [False, False, False, True, True, True, False, False, True, True, True]
        for i in range(len(data)):
            passport = Passport(data[i])
            self.assertEqual(expected[i], passport.valid_height(), data[i])

    def test_valid_hair_color(self):
        data = ["hcl:blah", "hcl:#000000", "hcl:#ffffff", "hcl:#02468a", "hcl:000000"]
        expected = [False, True, True, True, False]
        for i in range(len(data)):
            passport = Passport(data[i])
            self.assertEqual(expected[i], passport.valid_hair_color(), data[i])

    def test_valid_eye_color(self):
        data = ["ecl:amb", "ecl:blu", "ecl:brn", "ecl:gry", "ecl:grn", "ecl:hzl", "ecl:oth", "ecl:zzz"]
        expected = [True, True, True, True, True, True, True, False]
        for i in range(len(data)):
            passport = Passport(data[i])
            self.assertEqual(expected[i], passport.valid_eye_color(), data[i])

    def test_valid_id(self):
        data = ["pid:000000000", "pid:00000000", "pid:0000000000"]
        expected = [True, False, False]
        for i in range(len(data)):
            passport = Passport(data[i])
            self.assertEqual(expected[i], passport.valid_id(), data[i])