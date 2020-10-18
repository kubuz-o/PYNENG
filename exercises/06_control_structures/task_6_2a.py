# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Сообщение должно выводиться только один раз.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
ip_addr = input('Введите IP-адрес: ')  # вводим данные
ip_addr_list = ip_addr.split('.')  # преобразуем в список

for i in ip_addr_list:
        if not i.isdigit() or int(i) > 255 or '.' not in ip_addr:
                    print('Неправильный IP-адрес')
                            break
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

