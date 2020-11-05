# -*- coding: utf-8 -*-
"""
Задание 9.2a

Сделать копию функции generate_trunk_config из задания 9.2

Изменить функцию таким образом, чтобы она возвращала не список команд, а словарь:
    - ключи: имена интерфейсов, вида 'FastEthernet0/1'
    - значения: список команд, который надо выполнить на этом интерфейсе

Проверить работу функции на примере словаря trunk_config и шаблона trunk_mode_template.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""


trunk_mode_template = [
    "switchport mode trunk",
    "switchport trunk native vlan 999",
    "switchport trunk allowed vlan",
]

trunk_config = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17],
}

def generate_trunk_config(intf_vlan_mapping, trunk_template):
    """
    intf_vlan_mapping - словарь с соответствием интерфейс-VLAN такого вида:
    {'FastEthernet0/1': [10, 20],
     'FastEthernet0/2': [11, 30],
     'FastEthernet0/4': [17]}
    trunk_template - список команд для порта в режиме access
    Возвращает словарь:
    - ключи: имена интерфейсов, вида 'FastEthernet0/1'
    - значения: список команд, который надо выполнить на этом интерфейсе
    """
    intf_command = {}  # создаем пустой словарь
    for intf, vlan in intf_vlan_mapping.items():  # проходим в цикле по словарю interface-vlan
        config_template = []  # пустой список
        # config_template.append('interface ' + intf)  # заполняем список по каждому интерфейсу
        for command in trunk_template:  # проходим в цикле по списку команд
            if command.endswith('vlan'):  # условие для добавления номера vlan
                vlan_list = str(vlan).strip('[]')  # превращем список чисел в строку vlan
                config_template.append(f'{command} {vlan_list}')  # добавляем команды в конфиг
            else:
                config_template.append(f'{command}')  # добавляем команды в конфиг
                intf_command[intf] = config_template
    return intf_command  # возвращаем список команд


print(generate_trunk_config(trunk_config, trunk_mode_template))  # выводим список
