
# ARP Spoofing Attack

## 📌 Overview
This project is a Python script that performs an **ARP Spoofing Attack** using the `scapy` library. The attack manipulates the ARP tables of a victim and a router, allowing the attacker to intercept network traffic. This script is designed for educational and ethical hacking purposes only.

## ⚠️ Disclaimer
**This tool is for educational purposes only. Unauthorized use of ARP spoofing is illegal and unethical. The author does not take responsibility for any misuse of this script.**

## 🚀 Features
- Retrieves MAC addresses using ARP requests.
- Spoofs ARP tables to intercept traffic.
- Restores the ARP tables after attack termination.
- Runs continuously until manually stopped.

## 📂 Requirements
- Python 3.x
- `scapy` library

## 🔧 Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/konynour/NetworkDevelopmentTools.git
Navigate to the project folder:
shCopy
cd NetworkDevelopmentTools/arp-spoofing
Install dependencies:
shCopy
pip install scapy
⚙️ Usage
Edit the script to set the target IP and gateway IP:
 ## Python
shCopy    
target_ip = "192.168.1.X"  # Replace with victim's IP
gateway_ip = "192.168.1.1"  # Replace with router's IP

scCopy
Run the script with:
 
python arp_spoof.py
Stop the attack using CTRL + C, which restores the ARP tables.


📜 License
This project is licensed under the MIT License.

.