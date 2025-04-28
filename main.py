import socket
import sys
import ipaddress
import threading

# List of common top 100 ports
TOP_100_PORTS = [
    21, 22, 23, 25, 53, 80, 110, 119, 143, 443, 445, 465, 993, 995, 1080, 1433, 3306, 3389, 5432, 5900, 8080,
    8443, 8888, 12345, 31337, 51413, 10000, 27017, 50000
]

def validate_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def validate_port(port):
    return port.isdigit() and 0 <= int(port) <= 65535

def scan_port(ip, port, open_ports):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            result = s.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
    except socket.error:
        pass

def main():
    ip = input("Enter target IP address: ").strip()
    if not validate_ip(ip):
        print("Invalid IP address format.")
        sys.exit()

    mode = input("Do you want to scan a single port, multiple ports, all ports, or top 100 ports? (single/multiple/all/top100): ").strip().lower()

    ports = []
    if mode == "single":
        port = input("Enter the port number (0-65535): ").strip()
        if not validate_port(port):
            print("Invalid port number.")
            sys.exit()
        ports.append(int(port))
    elif mode == "multiple":
        port_list = input("Enter the port numbers separated by commas (e.g., 22,80,443): ").strip()
        port_strings = port_list.split(',')
        for p in port_strings:
            p = p.strip()
            if not validate_port(p):
                print(f"Invalid port number: {p}")
                sys.exit()
            ports.append(int(p))
    elif mode == "all":
        print("\nScanning all ports from 1 to 65535...\n")
        ports = range(1, 65536)
    elif mode == "top100":
        print("\nScanning the top 100 most common ports...\n")
        ports = TOP_100_PORTS
    else:
        print("Invalid selection. Choose 'single', 'multiple', 'all', or 'top100'.")
        sys.exit()

    open_ports = []
    threads = []

    print(f"\nScanning {ip} on port(s): {', '.join(str(p) for p in ports)}...\n")

    for port in ports:
        t = threading.Thread(target=scan_port, args=(ip, port, open_ports))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    if open_ports:
        print("\nOpen ports:")
        for port in sorted(open_ports):
            print(f"Port {port} is open.")
    else:
        print("\nNo open ports found.")

if __name__ == "__main__":
    main()
