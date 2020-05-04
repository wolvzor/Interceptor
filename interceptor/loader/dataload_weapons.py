import csv

from interceptor.fighter.weapon import Weapon


def load_weapons(filename='data/weapon_data.csv'):
    raw_data = open(filename, 'rt')
    reader = csv.reader(raw_data, delimiter=',', quoting=csv.QUOTE_NONE)
    x = list(reader)
    weapon_list = dict()
    for line in x:
        if line[0] != 'Name':
            weapon_range = dict(
                [(1, line[2]), (2, line[3]), (3, line[3]), (4, line[4]), (5, line[4]), (6, line[4]), (7, line[5]),
                 (8, line[5]), (9, line[5]), (10, line[6]), (11, line[6]), (12, line[6]), (13, line[6]),
                 (14, line[6]), (15, line[6])])
            weapon_list.update({line[0]: Weapon(line[0], line[1], weapon_range, line[7], line[8], line[9])})
    raw_data.close()
    return weapon_list
