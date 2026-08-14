import sys
from scapy.IP import IP
from scapy.ICMP import ICMP
from scapy.layers.inet import sr1

if len(sys.argv) < 2:
    sys.exit("[!] Usage: python main.py <target-ip>")

ip = sys.argv[1]
icmp = IP(dst=ip) / ICMP()
resp = sr1(icmp, timeout=10)

if resp is None:
    print("[!] The host seems to be down")
else:
    print("The host is up")
