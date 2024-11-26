import socket

def port_scanner(target_ip, ports):
    print(f"Scanning {target_ip} for open ports...\n")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set timeout for each connection attempt
        result = sock.connect_ex((target_ip, port))  # 0 means port is open
        if result == 0:
            print(f"Port {port}: Open")
        else:
            print(f"Port {port}: Closed")
        sock.close()

# Example usage
target_ip = input("Enter the target IP address: ")
ports = [21, 22, 23, 80, 443, 3389]  # Common ports to check
port_scanner(target_ip, ports)
