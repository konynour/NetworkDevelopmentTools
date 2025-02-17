NetworkTools/
├── ARP_Scanner/
│   ├── arp_scanner.py
│   ├── README.md
├── MAC_Changer/
│   ├── mac_changer.py
│   ├── README.md
└── README.md


# ARP Scanner

## Description
This tool scans a network for devices by sending ARP requests and collecting responses.

## Usage
```bash
python arp_scanner.py -t <IP Address or Range>

 # Example
 python arp_scanner.py -t 192.168.1.1/24