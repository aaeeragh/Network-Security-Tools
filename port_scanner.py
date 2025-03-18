import socket
import sys

def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout to skip unresponsive ports
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()
    except (socket.timeout, ConnectionRefusedError):
        pass  # Silently ignore closed ports/timeouts
    except Exception as e:
        print(f"Error checking port {port}: {e}")

def scan_ports(host, start_port, end_port):
    print(f"Scanning {host} for open ports ({start_port}-{end_port})...")
    open_ports = []
    for port in range(start_port, end_port + 1):
        if scan_port(host, port):
            open_ports.append(port)
    if not open_ports:
        print("No open ports found.")
    else:
        print(f"Open ports: {open_ports}")

if __name__ == "__main__":
    # Command-line or interactive input
    if len(sys.argv) == 4:
        target_host = sys.argv[1]
        start = int(sys.argv[2])
        end = int(sys.argv[3])
    else:
        target_host = input("Enter target host (e.g., 127.0.0.1): ").strip()
        start = int(input("Start port: "))
        end = int(input("End port: "))

    scan_ports(target_host, start, end)