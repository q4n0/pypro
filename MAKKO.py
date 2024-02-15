#!/usr/bin/env python3
import subprocess

print("Hello there im MAKKO a MacAddress changer")
name =input("Whats yours friend?\n Mine is: ")
interface =input("What device interface would you like to change?\n Interface to change: ")
mac =input("What MAC ADDRESS would you like to change the interface for "+interface+ " ?\n Mac to change: ")
print("\nHey "+name+" The interface "+interface+" MAC ADDRESS will change to "+mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", mac])
subprocess.call(["ifconfig", interface, "up"])

print(["\n[+] The program has successfully completed running..", name])
