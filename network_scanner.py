import scapy.all as scapy
# import optparse

# def get_input():
#     object_parser = optparse.OptionParser()
#     object_parser.add_option('-i', '--ip_address', dest='ip_address', help='please enter your ip subnet')
#     (user_input,arguments) = object_parser.parse_args()
#
#     if not user_input.ip_address:
#         print("enter user ip")
#
#     return user_input

ip_range = input('please enter your ip range: ')
def scan_network(ip_range):
    arp_request = scapy.ARP(pdst = ip_range)
    broadcast_request = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combine_request = broadcast_request/arp_request
    (answered_request,unanswered_request) = scapy.srp(combine_request, timeout=1)
    answered_request.summary()

# user_ipadd = get_input()
scan_network(ip_range)