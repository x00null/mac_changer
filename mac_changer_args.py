#!/usr/bin/env python

import subprocess
import optparse
import re


def get_arguments():

    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC Address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address you want to use")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info")
    elif not options.new_mac:
        parser.error("[-] Please specify a new MAC, use --help for more info")
    return options


def change_mac(interface, new_mac):

    print ("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):

    if_config_result = subprocess.check_output(["ifconfig", interface])
    mac_a_search = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", if_config_result)
    if mac_a_search:
        return mac_a_search.group(0)
    else:
        print ("[-] Could not read MAC address")


options = get_arguments()

current_mac = get_current_mac(options.interface)
print ("Current MAC is: " + str(current_mac))

change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)
if current_mac == options.interface:
    print ("[+] MAC address was succesfully changed to " + current_mac)
else:
    print ("[-] MAC address did not get changed")





