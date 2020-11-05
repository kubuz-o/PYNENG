# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12': 10,
                       'FastEthernet0/14': 11,
                       'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


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
            elif 'access' in line and not 'access vlan' in line:  # ищем access-порты без vlan
                access_ports[intf] = 1  # полученная пара ключ:значение
            elif 'trunk allowed vlan' in line:  # ищем trunk allowed vlan в строке файла
                # берем значение vlan в строке;сплитуем еще раз и в цикле составляем список чисел
                trunk_vlan = [int(item) for item in line.rstrip('\n').split()[-1].split(',')]
                trunk_ports[intf] = trunk_vlan  # полученная пара ключ:значение
    return access_ports, trunk_ports  # возвращаем кортеж


print(get_int_vlan_map('config_sw2.txt'))  # вывод кортежа
