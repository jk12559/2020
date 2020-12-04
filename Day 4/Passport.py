import re

class Passport:
    def __init__(self, data):
        temp1 = self.split_lines(data)
        temp2 = [self.split_spaces(x) for x in temp1]
        flat_list = [item for sublist in temp2 for item in sublist]
        data_map = self.make_map(flat_list)
        self.birth_year = int(data_map["byr"]) if "byr" in data_map else None
        self.issue_year = int(data_map["iyr"]) if "iyr" in data_map else None
        self.exp_year = int(data_map["eyr"]) if "eyr" in data_map else None
        self.height = data_map["hgt"] if "hgt" in data_map else None
        self.hair_color = data_map["hcl"] if "hcl" in data_map else None
        self.eye_color = data_map["ecl"] if "ecl" in data_map else None
        self.id = data_map["pid"] if "pid" in data_map else None
        self.country_id = data_map["cid"] if "cid" in data_map else None

    def split_lines(self, data):
        return data.splitlines()

    def split_spaces(self, data):
        return data.split(" ")

    def make_map(self, data):
        return dict([x.split(":") for x in data])

    def is_valid(self):
        if not self.valid_birth_year():
            return False
        if not self.valid_issue_year(): 
            return False
        if not self.valid_exp_year(): 
            return False
        if not self.valid_height(): 
            return False
        if not self.valid_hair_color(): 
            return False
        if not self.valid_eye_color():
            return False
        if not self.valid_id():
            return False
        return True

    def valid_birth_year(self):
        if self.birth_year == None:
            return False
        return self.birth_year >= 1920 and self.birth_year <= 2002
    def valid_issue_year(self):
        if self.issue_year == None:
            return False
        return self.issue_year >= 2010 and self.issue_year <= 2020
    def valid_exp_year(self):
        if self.exp_year == None:
            return False
        return self.exp_year >=2020 and self.exp_year <= 2030
    def valid_height(self):
        if self.height == None:
            return False
        height_pattern = re.compile("(\d*)(in|cm)")
        height_match = height_pattern.match(self.height)
        if not height_match:
            return False
        if height_match.group(2) == "in":
            return int(height_match.group(1)) >= 59 and int(height_match.group(1)) <= 76
        if height_match.group(2) == "cm":
            return int(height_match.group(1)) >= 150 and int(height_match.group(1)) <= 193
    def valid_hair_color(self):
        if self.hair_color == None:
            return False
        hair_color_pattern = re.compile("#[0-9a-f]{6}")
        if hair_color_pattern.match(self.hair_color):
            return True
        return False
    def valid_eye_color(self):
        if self.eye_color == None:
            return False
        return self.eye_color in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    def valid_id(self):
        if self.id == None:
            return False
        id_pattern = re.compile("^\d{9}$")
        if id_pattern.match(self.id):
            return True
        return False
