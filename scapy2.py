from scapy.all import *

# Create and send an ICMP packet
pkt = IP(dst="8.8.8.8")/ICMP()
response = sr1(pkt)

# Display the response
if response:
    response.show()

