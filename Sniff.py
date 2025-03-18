from scapy.all import sniff, IP, TCP, UDP, Ether
import platform

def process_packet(packet):
    """Process each captured packet and extract basic information"""
    try:
        # Extract Ethernet layer information
        if Ether in packet:
            src_mac = packet[Ether].src
            dst_mac = packet[Ether].dst
        else:
            src_mac = "N/A"
            dst_mac = "N/A"

        # Extract IP layer information
        if IP in packet:
            ip_layer = packet[IP]
            src_ip = ip_layer.src
            dst_ip = ip_layer.dst
            protocol = ip_layer.proto

            # Protocol name mapping
            protocol_map = {1: "ICMP", 6: "TCP", 17: "UDP"}
            protocol_name = protocol_map.get(protocol, "Unknown")

            # Initialize port information
            src_port = None
            dst_port = None

            # Extract TCP/UDP information
            if TCP in packet:
                src_port = packet[TCP].sport
                dst_port = packet[TCP].dport
            elif UDP in packet:
                src_port = packet[UDP].sport
                dst_port = packet[UDP].dport

            # Print information
            print(f"[*] MAC: {src_mac} -> {dst_mac}")
            print(f"    IP: {src_ip} -> {dst_ip}")
            print(f"    Protocol: {protocol_name} ({protocol})")
            if src_port and dst_port:
                print(f"    Ports: {src_port} -> {dst_port}")
            print("-" * 50)
            
    except Exception as e:
        print(f"Error processing packet: {e}")

def main():
    """Main function to start packet sniffing"""
    print("Starting packet sniffer...")
    print("Press CTRL+C to stop\n")
    
    # Set platform-specific parameters
    if platform.system().lower() == "windows":
        # Windows doesn't support interface parameter the same way
        sniff(prn=process_packet, store=0)
    else:
        # Linux/macOS can use default interface
        sniff(prn=process_packet, store=0, iface=None)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nSniffer stopped by user")