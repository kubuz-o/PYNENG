# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком виде:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
ospf_route_template = '''
Prefix\t\t\t\t {0}
AD/Metric\t\t\t {1}
Next-Hop\t\t\t {2}
Last update\t\t\t{3}
Outbound Interface\t{4}
'''

with open('ospf.txt', 'r') as f:
    for line in f:
        print(ospf_route_template.format(line.split(',')[0].split()[1],
                                         line.split(',')[0].split()[2].strip('[]'),
                                         line.split(',')[0].split()[4],
                                         line.split(',')[1],
                                         line.split(',')[2]).rstrip('\n'))

