# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip_addr = input('Введите IP-адрес: ')  # вводим данные
ip_addr_list = ip_addr.split('.')  # преобразуем в список

ip_addr_correct = False
while not ip_addr_correct:
    for i in ip_addr_list:
        if not i.isdigit() or int(i) > 255 or '.' not in ip_addr:
            print('Неправильный IP-адрес')
            ip_addr = input('Введите IP-адрес: ')
            ip_addr_list = ip_addr.split('.')
            break
        else:
            ip_addr_correct = True
    else:
        if ip_addr == '0.0.0.0':
            print('unassigned')
        elif ip_addr == '255.255.255.255':
            print('local broadcast')
        elif int(ip_addr_list[0]) > 0 and not int(ip_addr_list[0]) >= 224:
            print('unicast')
        elif int(ip_addr_list[0]) > 223 and not int(ip_addr_list[0]) >= 240:
            print('multicast')
        else:
            print('unused')
                                                    
