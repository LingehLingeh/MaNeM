# MaNeM
A Simple Ethical Hacking Framework which Comprises Network Scanner, Mac-address Changer and a Packet Sniffer

# Installation
$ git clone https://github.com/LingehLingeh/MaNeM.git

$ git clone https://github.com/LeonardoNve/dns2proxy.git

$ sudo apt install sslstrip

$ sudo apt install python3-subprocess

$ sudo apt install python3-re

$ sudo apt install python3-colorama

$ sudo apt install python3-scapy

$ sudo apt install python3-pyfiglet


# Launch MaNeM


$ python3 MaNeM


# Steps to follow before using man in the middle tool

$ echo 1 /proc/sys/net/ipv4/ip_forward

$ iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 10000

$ iptables -t nat -A PREROUTING -p udp --destination-port 53 -j REDIRECT --to-port 53

$ sudo sslstrip

$ python dns2proxy

# Other

- If apt isntall python3-xyz doesn't work for you, use the normal pip or pip3 installer
- Run MaNeM framework in another window to use the packet listener when using the MITM tool
- How to use the rest of the tool are demonstrated as you engage with MaNeM framework
- Refere to the screenshots provided in the folder MaNeM
- You can still use wireshack as a listener or any other listener..
