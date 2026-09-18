# Количество адресов в сети зависит от количества нулей в маске сети
# Например, если в маске, например, 3 нуля, значит в сети 2³ = 8 адресов.


# У компьютера IP‑адрес 172.16.205.14, а адрес сети – 172.16.192.0.
# Найдите третий байт маски (считая слева, в десятичном виде). Запишите ответ одним числом.
# 205 = 11001101
# 192 = 11000000
# 11001101
# ???????? => 11000000 = 192 - третий бит в маске
# 11000000


# import ipaddress
# # Задаём IP-адрес и маску сети
# network = ipaddress.ip_network('150.25.199.18/255.255.224.0', False)
# # Выводим адрес сети
# print(network.network_address)

# from ipaddress import *
# count = 0
# for mask in range(33):
#     net = ip_network(f"111.91.200.28/{mask}", 0)
#     if (str(net))


# from ipaddress import *
# for mask in range(33):
#     net = ip_network(f"158.116.11.146/{mask}", 0)
#     if str(net.network_address) == "158.116.0.0":
#         print(32-mask)

#
# from ipaddress import *
#
# ip_add = ip_network("112.208.0.0/255.255.128.0", 0)
# count = 0
# for i in ip_add:
#     ip_bin = f"{i:b}"
#     if ip_bin.count("1") % 11 == 0:
#         count += 1
#
# print(count)

# from ipaddress import *
# ip_add = ip_address("20.24.110.42")
# for mask in range(31):
#     net = ip_network(f"{ip_add}/{mask}", 0)
#     if net[0] < ip_add < net[-1]:
#         print(net, net.netmask)

# from ipaddress import *
# count = 0
# ip_add = ip_network("172.16.160.0/255.255.240.0", 0) # ip-адрес и маска сети
# for i in ip_add:
#     ip_bin = f"{i:b}" #перевод в двоичку
#     if ip_bin.count("1") % 3 != 0: #сли кол-во единиц не кратко 3
#         count += 1
#
# print(count)

# from ipaddress import *
#
# ip1 = ip_address("134.181.67.112")
# ip2 = ip_address("134.181.94.117")
#
# for mask in range(1, 31):
#     net = ip_network(f"{ip1}/{mask}", 0)
#     if ip1 in net:
#         if net.network_address < ip1 < net.broadcast_address and net.network_address < ip2 < net.broadcast_address:
#             print(net)
# print(255 + 2**6 + 2**7 + 2**5)



# 1 Тип сравнение два узла
# for mask in range(1, 31):
#     net = ip_network(f'{ip1}/{mask}', 0)
#     if ip2 in net:
#         if net.network_address < ip1 < net.broadcast_address and \
#            net.network_address < ip2 < net.broadcast_address:
#             print(net)

# 2 Тип сравнение масок
# from ipaddress import ip_address, ip_network
#
# ip_add = ip_address('134.181.67.112')
#
# for mask in range(31):
#     net = ip_network(f'{ip_add}/{mask}', 0)
#     if net[0] < ip_add < net[-1]:
#         print(net, net.netmask)


# 3 Типология с проверкой на кратность айти адресов устройств
# from ipaddress import *
# ip_add = ip_network('112.208.0.0/255.255.128.0', 0)
# count = 0
# for i in ip_add:
#    ipbin = f'{i:b}'
#    if ipbin.count('1')%11==0:
#        count+=1
# print(count)


# from ipaddress import ip_address, ip_network
#
# min_1 = 32
# ip_add = ip_address("20.24.110.42")
# network = ip_address("20.24.96.0")
# for mask in range(33):
#     net = ip_network(f'{ip_add}/{mask}', 0)
#     if net.network_address == network:
#         bin_net = bin(int(net.netmask))
#         kol_1 = bin_net.count("1")
#         if kol_1 < min_1:
#             min_1 = kol_1
# print(min_1)

# print(bin(68)[2:])
# print(bin(249)[2:])
# print(68&248)
# print(249&0)
#
# 205.99.71.254

#
# print(bin(64)[2:])
# print(bin(248)[2:])
# print(int("01000111", 2))

# print(116&192)
# print(bin(172)[2:])
# print(bin(95)[2:])
# print(bin(116)[2:])
# print(bin(174)[2:])
# # 01100000
# # 11000000
# # 01000000
# #
# print(int("01000000", 2))
# print(172+95+64+1)
from ipaddress import *
ip_add = ip_network('172.95.116.174/255.255.192.0', 0)
count = 0
for i in ip_add:
   ipbin = f'{i:b}'
   if ipbin.count('1')%5==0:
       print(int(ipbin[0:8], 2),int(ipbin[8:16], 2), int(ipbin[16:24], 2), int(ipbin[24:], 2), 172+95 + 64 + 15 )

# from ipaddress import *
#
# count = 0
# ip_add = ip_network("112.160.0.0/255.240.0.0", 0)
# for i in ip_add:
#     ip_bin = f"{i:b}"
#     if ip_bin.count("1") % 5 == 0:
#         count += 1
# print(count)

# from ipaddress import *
#
# count = 0
# ip_add = ip_network("112.160.0.0/255.240.0.0", 0)
# for i in ip_add:
#     ip_bin= f"{i:b}"
#     if ip_bin.count("1") % 3 != 0:
#         count += 1
# print(count)

# from ipaddress import *
#
# ip_add = ip_network("73.148.145.65/255.224.0.0", 0)
# for i in ip_add:
#   ipbin = f"{i:b}"
#   print(int(ipbin[0:8], 2), int(ipbin[8:16], 2), int(ipbin[16:24], 2), int(ipbin[24:], 2))

from ipaddress import IPv4Network

#IPv4Networkэто умная коробка, в которую ты кладешь адрес любого устройства и маску, а она сама «понимает», в какой группе (сети) находится этот компьютер.

net = IPv4Network("10.15.179.18/255.255.254.0", 0)

# Список всех доступных адресов для компьютеров (кроме сети и широковещательного)
hosts = list(net.hosts())

# Берем последний адрес из списка [-1] и считаем сумму его байтов
last_ip = hosts[-1]
print(sum(last_ip.packed))