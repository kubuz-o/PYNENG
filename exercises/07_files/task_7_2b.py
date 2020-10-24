# -*- coding: utf-8 -*-
"""
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
from sys import argv

ignore = ["duplex", "alias", "Current configuration"]

filename = argv[1]

with open(filename, 'r') as file, open('config_sw1_cleared.txt', 'w') as new_file:
    for line in file:
        for word in ignore:
            if word in line:
                break
            else:
                new_file.write(line)

