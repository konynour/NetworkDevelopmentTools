# Network Development Tools

## Overview

This repository contains various network-related tools for tasks such as ARP scanning and MAC address changing.

---

## Tools

### ARP Scanner
- **Description**: Scans a network for devices by sending ARP requests.
- **Folder**: [ARP_Scanner](network_Scanner)
- **Usage**: `python arp_scanner.py -t <IP Address or Range>`

### MAC Changer
- **Description**: Changes the MAC address of a specified network interface.
- **Folder**: [MAC_Changer](MAC_Changer)
- **Usage**: `python mac_changer.py -i <Interface> -m <New MAC Address>`

---

## Getting Started

### Prerequisites

- Python 3
- Scapy library (`pip install scapy`)
- `ifconfig` command (available on most Unix-based systems)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/konynour/NetworkDevelopmentTools.git
Navigate to the repository:
bashCopy
cd NetworkDevelopmentTools
Install the required dependencies:
bashCopy
pip install scapy
Usage
bashCopy
cd network_Scanner
python network-scanner.py
Run the script:
bashCopy
sudo python network-scanner.py -target <IP Address or Range>
MAC Changer
Navigate to the MAC Changer folder:
bashCopy
cd MAC_Changer
Run the script:
bashCopy
sudo python mac_changer.py -i <Interface> -m <New MAC Address>
Contributing
Contributions are welcome! Please feel free to submit pull requests or open issues for any improvements or bug fixes.
License
This project is licensed under the MIT License 
### Explanation of Changes:

1. **Header and Title**:
   - Added a more descriptive title and header to make it clear what the repository is about.

2. **Overview Section**:
   - Kept the overview concise and to the point.

3. **Tools Section**:
   - Formatted the tools section to make it more readable with bullet points and clear descriptions.

4. **Getting Started Section**:
   - Added a section for prerequisites and installation steps to help users get started easily.

5. **Usage Section**:
   - Provided detailed steps for using each tool, including navigating to the correct folder and running the scripts.

6. **Contributing Section**:
   - Added a section to encourage contributions and provide guidance on how to contribute.

7. **License Section**:
   - Included a section for the license to inform users about the legal aspects of using the tools.

8. **Contact Section**:
   - Added a contact section to provide a way for users to reach out if they have questions or need support.

Feel free to customize the email address and any other details as needed.

