# By J.P. Moreno
import random
from data import *

area_codes = ["416", "647", "905"]

def phone_gen():
    first = str(random.randint(100, 999))
    second = str(random.randint(1000, 9999))
    area_code = random.choice(area_codes)
    return f"{area_code}-{first}-{second}"

class Person:
    def __init__(self, name):
        self.first_name = name[0]
        self.last_name = name[1]
        self.username = (self.first_name[0]+self.last_name).lower()
        self.email = self.username + "@email.com"
        self.password = "password"
        self.phone_number = phone_gen()

    def __str__(self):
        return f"(username, first_name, last_name, email, phone_number) - ({self.username}, {self.first_name}, {self.last_name}, {self.email}, {self.phone_number})"

address_prefix = ["Main", "Cornerbrook", "Highland", "Rosemary", "Dundas", "Mavis", "Redmond"]
address_postfix = ["Boulevard", "Street", "Avenue", "Drive", "Crescent"]

def address_gen():
    number = str(random.randint(0,199))
    prefix = random.choice(address_prefix)
    postfix = random.choice(address_postfix)
    return f"{number} {prefix} {postfix}"

pc_areas = ["L5M", "L5J", "L4X", "L4H", "L4H"]
def postal_gen():
    prefix = random.choice(pc_areas)
    postfix = chr(random.randint(ord('A'), ord('Z'))) + str(random.randint(0,9))+ chr(random.randint(ord('A'), ord('Z')))
    return f"{prefix}{postfix}"
    
class Restaurant:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.phone_number = phone_gen()
        self.address = address_gen()
        self.postal_code = postal_gen()
    
    def __str__(self):
        return f"{self.name} - {self.desc} - {self.phone_number} - {self.address} - {self.postal_code}"

types_of_rests = ["arab", "chinese", "indian", "italian", "spanish", "turkish"]


def gen_data():
    owner_rest_pairs = []
    for type_of_rest in types_of_rests:
        names = globals()[type_of_rest+"_names"]
        for name in names:
            person = Person(name)
            rest_name, rest_desc = globals()[type_of_rest+"_rest_namedesc_gen"](person)
            rest = Restaurant(rest_name, rest_desc)
            owner_rest_pairs.append((person, rest, type_of_rest))
    return owner_rest_pairs
