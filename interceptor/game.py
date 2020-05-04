from interceptor.loader.dataload_damagetemplates import load_templates
from interceptor.loader.dataload_fighters import load_fighters
from interceptor.loader.dataload_weapons import load_weapons

# Dataloads
weapon_list = load_weapons()
print(weapon_list)
for weapon in weapon_list:
    print(weapon)

damage_templates = load_templates()
print(damage_templates)
for key in damage_templates:
    print(damage_templates[key])

renegade_fighters = load_fighters('data/fighter_renegade_data.json', weapon_list)
print(renegade_fighters)
for key in renegade_fighters:
    print(renegade_fighters[key])

tog_fighters = load_fighters('data/fighter_tog_data.json', weapon_list)
print(tog_fighters)
for key in tog_fighters:
    print(tog_fighters[key])