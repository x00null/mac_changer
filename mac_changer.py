#!/usr/bin/python

import subprocess

interface = input("interface > ")
new_mac = input("New MAC > ")

print ("[+] Changing MAC address for " + interface + " to " + new_mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])

#subprocess.call("ifconfig " + interface + " down ", shell=True)
#subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
#subprocess.call("ifconfig " + interface + " up ", shell=True)
# This code its unefective cuz anyone can use this to hijack our script and make use of
# another commands.