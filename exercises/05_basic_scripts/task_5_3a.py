# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]
data_mode = input("Введите режим работы интерфейса (access/trunk): ")
data_interface = input("Введите тип и номер интерфейса: ")

port_variable = {'access': 'Введите номер VLAN: ',         # создаем дополнительный словарь
                 'trunk': 'Введите разрешенные VLANы: '}
data_vlan = input(port_variable[data_mode])

d_keys = ['access', 'trunk']  # ключи основного словаря - режим работы интерфейса
template = dict.fromkeys(d_keys)  # создаем основной словарь
# заполняем основной словарь шаблонами и значениями из дополнительного словаря
template['access'] = [port_variable['access'], access_template]
template['trunk'] = [port_variable['trunk'], trunk_template]

template_chosen = template[data_mode]  # выбранный шаблон по введенному режиму работы интерфейса
config = '\n'.join(template_chosen[1])  # шаблон на вывод

print('interface', data_interface, '\n', config.format(data_vlan))  # вывод конфига
