from subprocess import call
from colorama import Fore, init
import pyfiglet
import time

# Initialize colorama
init(autoreset=True)


def hacking_tool_banner(tool_name, producer_name):
    # Title Bar
    print(Fore.GREEN + "=" * 60)
    print(Fore.CYAN + "                     :: MaNeM v 1.0 TOOL ::")
    print(Fore.MAGENTA + f"                  Developed by: {producer_name}")
    print(Fore.GREEN + "=" * 60)

    # Use a larger and clearer font
    try:

        banner = pyfiglet.figlet_format(tool_name, font="smmono12")
    except Exception as e:
        print(Fore.RED + f"Error: {e}. Using default font.")
        banner = pyfiglet.figlet_format(tool_name)  # Fallback to default font

    # Print the banner with a different color
    print(Fore.YELLOW + banner)

    # Tool loading messages
    print(Fore.GREEN + "-" * 60)
    print(Fore.YELLOW + "[*] Initializing tool...")
    time.sleep(1)
    print(Fore.YELLOW + "[*] Setting up environment...")
    time.sleep(1)
    print(Fore.GREEN + "[*] Tool ready for use!")
    print(Fore.GREEN + "-" * 60)


# Run the banner with "MaNeM" as the tool name and "Sheriff at the Conner" as the producer
hacking_tool_banner("MaNeM", "Sheriff")

def execute_macChanger():
    call(['python3', 'macChanger.py'])


def execute_network_scanner():
    call(['python3', 'network_scanner.py'])


def execute_MITM():
    call(['python3', 'MITM.py'])

def execute_Listener():
    call(['python3', 'Listener.py'])

GOLD = "\033[38;5;220m"  # Bright yellow
RESET = "\033[0m"        # Reset to default
print(GOLD + '\n1. change my mac address')
print(GOLD + '2. Scan a network')
print(GOLD + '3. Use the man in the middle tool(lunch this tool again and choose the listener option to see captured traffics)')
print(GOLD + '4. Listener\n')
print(GOLD + '++ press crtl + c to exit\n')

input_number= int(input('>:: '))

try:
    if input_number == 1:
        execute_macChanger()

    elif input_number == 2:
        execute_network_scanner()

    elif input_number == 3:
        execute_MITM()

    elif input_number == 4:
        execute_Listener()

except KeyboardInterrupt:
    print('done')

