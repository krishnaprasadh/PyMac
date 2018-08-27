#!/usr/bin/python3

import subprocess
import re

interface = raw_input("Enter interface: ")

try:
    data = subprocess.check_output(["ifconfig", interface])
    current_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",data)
except subprocess.CalledProcessError:
    print("[ERROR] Interface not found!\n")
    exit()

new_mac = raw_input("Enter new MAC: ")

if current_mac:
        current_mac = current_mac.group(0)
else:
        print("[ERROR] Unable to read current MAC!\n")
        exit()

print("[INFO] Changing MAC address of "+interface+" from "+str(current_mac)+" to "+str(new_mac))
print("Current MAC = "+str(current_mac))
print("New MAC = "+str(new_mac))

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])
data=subprocess.check_output(["ifconfig", interface])
current_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",data)

if current_mac:
    current_mac = current_mac.group(0)
else:
    print("[ERROR] Unable to read new MAC!\n")
    exit()

if current_mac == new_mac:
    print("[OK] MAC address changed successfully!\n")
else:
    print("[ERROR] MAC address != xx:xx:xx:xx:xx:xx / MAC address not fully changed!\n")