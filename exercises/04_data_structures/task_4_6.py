# -*- coding: utf-7 -*-
"""
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"

"""
print('Prefix\t\t\t\t' + ospf_route.split(',')[0].split()[0] +
      '\nAD/Metric\t\t\t' + ospf_route.split(',')[0].split()[1] +
      '\nNext-Hop\t\t\t' + ospf_route.split(',')[0].split()[3] +
      '\nLast update\t\t\t' + ospf_route.split(',')[1].split()[0] +
      '\nOutbound Interface\t' + ospf_route.split(',')[2].split()[0])
"""
#или второй вариант

ospf_route_template = '''
Prefix\t\t\t\t {0}
AD/Metric\t\t\t {1}
Next-Hop\t\t\t {2}
Last update\t\t\t{3}
Outbound Interface\t{4}
'''

print(ospf_route_template.format(ospf_route.split(',')[0].split()[0],
                                 ospf_route.split(',')[0].split()[1],
                                 ospf_route.split(',')[0].split()[3],
                                 ospf_route.split(',')[1],
                                 ospf_route.split(',')[2]))
