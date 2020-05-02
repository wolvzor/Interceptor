from interceptor.loader.dataload_damagetemplates import load_templates
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
