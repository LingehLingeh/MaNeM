import scapy.all as scapy
from scapy.layers.http import HTTPRequest

def packet_analyser(packet):
    # packet.show()
    # referer = packet[HTTPRequest].Referer.decode()

    # if packet[HTTPRequest].Referer:
    #      print('referer: {referer}')
    # print(f'you are visiting this {packet[HTTPRequest].Referer}')
    if packet.haslayer(HTTPRequest):
        if packet.haslayer(scapy.Raw):
            print(packet[scapy.Raw].load)


def packet_listener(interface):
    scapy.sniff(iface=interface, store=False, prn=packet_analyser)

interface = input('enter listening interface(eth0,wlan0...): ')
packet_listener(interface)