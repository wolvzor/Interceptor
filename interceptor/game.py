from interceptor.loader.dataload_weapons import load_weapons

weapon_list = load_weapons()
print(weapon_list)
for weapon in weapon_list:
    print(weapon)
