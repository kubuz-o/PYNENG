# -*- coding: utf-8 -*-
"""
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

subnet_template = '''
Network:
    {0}
    {1:<8}  {2:<8}  {3:<8}  {4:<8} 
    {1:08b}  {2:08b}  {3:08b}  {4:08b} 
    Mask:
        /{5} 
        {6:<8}  {7:<8}  {8:<8}  {9:<8} 
        {10}  {11}  {12}  {13} 
        '''

        data = data = argv[1]
        data_network = data.split('/')[0]  # адрес хоста
        mask = data.split('/')[1]  # маска
        mask_bin = '1' * int(mask) + '0' * (32 - int(mask))  # маска в двоичном формате

        data_network_bin = '{0:08b}{1:08b}{2:08b}{3:08b}'.format(int(data_network.split('.')[0]), int(data_network.split('.')[1]),
                                                                                                                          int(data_network.split('.')[2]), int(data_network.split('.')[3]))

        network_addr_bin = data_network_bin[0:mask_bin.count('1')] + '0' * (32 - mask_bin.count('1'))  # адрес подсети в двоичном формате

        # адрес подсети в десятичном формате

        network_addr_dec = str(int(network_addr_bin[0:8], 2)) + '.' + str(int(network_addr_bin[8:16], 2)) + "." + \
                                   str(int(network_addr_bin[16:24], 2)) + '.' + str(int(network_addr_bin[24:], 2))

        print(subnet_template.format(network_addr_dec,
                                                                  int(network_addr_dec.split('.')[0]),
                                                                  int(network_addr_dec.split('.')[1]),
                                                                  int(network_addr_dec.split('.')[2]),
                                                                  int(network_addr_dec.split('.')[3]),
                                                                  mask,
                                                                  int(mask_bin[0:8], 2),
                                                                  int(mask_bin[8:16], 2),
                                                                  int(mask_bin[16:24], 2),
                                                                  int(mask_bin[24:], 2),
                                                                  mask_bin[0:8],
                                                                  mask_bin[8:16],
                                                                  mask_bin[16:24],
                                                                  mask_bin[24:]))

