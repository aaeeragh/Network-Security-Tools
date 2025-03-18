import socket

def check_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((ip, port))
    if result == 0:
        print(f"Port {port} is open")
    else:
        print(f"Port {port} is closed")
    sock.close()

if __name__ == "__main__":
    ip = input("Enter IP address: ")
    ports = input("Enter ports to check (comma-separated): ").split(',')
    for port in ports:
        check_port(ip, int(port.strip()))