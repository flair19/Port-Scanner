Port Scanner
This is a simple Python-based Port Scanner that allows you to scan specific ports on a given target IP address. The script supports different modes of scanning, including scanning a single port, multiple ports, all ports (1-65535), or the top 100 most common ports.

Features
Scan a single port.

Scan multiple ports (by entering port numbers separated by commas).

Scan all ports (from port 1 to 65535).

Scan the top 100 most common ports.

Multithreading support for faster scanning.

Requirements
Python 3.x

socket module (built-in)

ipaddress module (built-in)

Usage
Clone or download the repository to your local machine.

Ensure you have Python 3.x installed on your system.

Run the script by executing the following command:

bash
Copy code
python port_scanner.py
Follow the prompts:

Enter the target IP address.

Choose the scanning mode (single, multiple, all, or top100).

For "multiple" mode, enter port numbers separated by commas (e.g., 22, 80, 443).

Example:
bash
Copy code
Enter target IP address: 192.168.1.1
Do you want to scan a single port, multiple ports, all ports, or top 100 ports? (single/multiple/all/top100): top100

Scanning the top 100 most common ports...

Open ports:
Port 22 is open.
Port 80 is open.
Port 443 is open.
Modes of Scanning
1. Single Port:
Scan a specific port by entering a port number (0-65535).

2. Multiple Ports:
Scan multiple ports by entering a list of port numbers separated by commas (e.g., 22, 80, 443).

3. All Ports:
Scan all ports from 1 to 65535.

4. Top 100 Ports:
Scan the 100 most common ports (from a predefined list).

License
This project is licensed under the MIT License - see the LICENSE file for details.

