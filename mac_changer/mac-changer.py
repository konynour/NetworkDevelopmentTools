#!/usr/bin/env python

import subprocess
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("[-] Please specify a MAC address, use --help for more info.")
    return options


def mac_change(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)

    # Disable the interface
    subprocess.call(["ifconfig", interface, "down"])
    # Change the MAC address
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    # Enable the interface
    subprocess.call(["ifconfig", interface, "up"])


def verify_mac_change(interface, expected_mac):
    # Get the current MAC address
    output = subprocess.check_output(["ifconfig", interface])
    if expected_mac in str(output):
        print(f"[+] MAC address successfully changed to {expected_mac}")
    else:
        print("[-] Failed to change MAC address.")


options = get_arguments()
mac_change(options.interface, options.new_mac)
verify_mac_change(options.interface, options.new_mac)