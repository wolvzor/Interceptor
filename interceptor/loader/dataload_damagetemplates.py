import csv

from interceptor.fighter.damagetemplate import DamageTemplate


def load_templates(filename='data/damage_template_data.csv'):
    raw_data = open(filename, 'rt')
    reader = csv.reader(raw_data, delimiter=',', quoting=csv.QUOTE_NONE)
    x = list(reader)
    template_dict = dict()
    for line in x:
        if line[0] != 'Name':
            damage_list = []
            for x in range(0, 10):
                damage_list.append(int(line[x + 5]))
            template_dict.update({line[0]: DamageTemplate(line[0], line[1], line[2], line[3], line[4], damage_list)})
    raw_data.close()
    return template_dict
