import subprocess
import optparse
import re

# def get_input():
#     parse_object = optparse.OptionParser()
#     parse_object.add_option('-i', '--interface', dest='interface', help='enter your interface')
#     parse_object.add_option('-m', '--mac', dest='mac', help='enter your mac-addr')
#
#     return parse_object.parse_args()
interface = input('please input interface: ')
mac = input('please input macaddress: ')
def check_mac(interface):
    ifconfig = subprocess.check_output(['ifconfig', interface])
    new_mac = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', str(ifconfig))

    if new_mac:
        return new_mac.group(0)
    else:
        return None

def change_mac(interface, mac):
    subprocess.call(['ifconfig', interface, 'down'])
    subprocess.call(['ifconfig', interface, 'hw', 'ether', mac])
    subprocess.call(['ifconfig', interface, 'up'])


# (user_inputs, arguments) = get_input()
change_mac(interface, mac)
check_mac(interface)
final_mac = check_mac(interface)

if final_mac == mac:
    print('success')
else:
    print('error')