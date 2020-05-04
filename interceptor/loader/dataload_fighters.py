import json

from interceptor.fighter.fighter import generate_shields, generate_armor, Fighter
from interceptor.fighter.fighter_weapons import FighterWeapons


def load_fighters(filename, loaded_weapons):
    fighters_dict = dict()
    with open(filename) as json_file:
        json_array = json.load(json_file)
        for item in json_array:
            shields = item['shields']
            shield_dict = generate_shields(shields['bow'], shields['left'], shields['right'], shields['stern'])

            armor = item['armor']
            armor_dict = generate_armor(armor['bow'], armor['left'], armor['right'], armor['stern'])

            weapons = item['weapons']
            fighter_weapons = FighterWeapons()
            for weapon in weapons:
                if weapon['type'] not in loaded_weapons:
                    print(f"ERROR: Weapon Type not found in loaded weapons: {weapon['type']}")
                fighter_weapons.add_weapon(weapon['location'], loaded_weapons.get(weapon['type']))

            engines = item['engines']
            center_engine = engines['center'] if 'center' in engines else 0
            left_engine = engines['left'] if 'left' in engines else 0
            right_engine = engines['right'] if 'right' in engines else 0

            fighters_dict.update({item['name']:
                                      Fighter(item['name'], item['class'], item['mass'], item['cost'], center_engine,
                                              right_engine,
                                              left_engine, item['thrust'], item['streamlining'], item['antigrav'],
                                              shield_dict,
                                              armor_dict, fighter_weapons)})
    return fighters_dict
