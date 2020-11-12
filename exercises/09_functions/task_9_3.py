# -*- coding: utf-8 -*-
"""
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN (числа):
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN (список чисел):
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

def get_int_vlan_map(config_filename):
    """
    функция обрабатывает конфигурационный файл коммутатора и возвращает кортеж из двух словарей:
    * словарь портов в режиме access, где ключи номера портов, а значения access VLAN (числа);
    * словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN (список чисел):
    :param config_filename:
    :return:
    """
    with open(config_filename, 'r') as f:  # открываем файл
        access_ports = {}  # словарь ассess-портов
        trunk_ports = {}  # словарь trunk-портов
        for line in f:
            if 'FastEthernet' in line:  # ищем FastEthernet в строке файла
                intf = line.rstrip('\n').split()[-1]  # ключ словаря
            elif 'access vlan' in line:  # ищем access vlan в строке файла
                acc_vlan = line.rstrip('\n').split()[-1]  # берем значение vlan в строке
                access_ports[intf] = int(acc_vlan)  # полученная пара ключ:значение
            elif 'trunk allowed vlan' in line:  # ищем trunk allowed vlan в строке файла
                # берем значение vlan в строке;сплитуем еще раз и в цикле составляем список чисел
                trunk_vlan = [int(item) for item in line.rstrip('\n').split()[-1].split(',')]
                trunk_ports[intf] = trunk_vlan  # полученная пара ключ:значение
    return access_ports, trunk_ports  # возвращаем кортеж


print(get_int_vlan_map('config_sw1.txt'))  # вывод кортежа
