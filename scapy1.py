from scapy.all import *

pkts = sniff(count=5)
pkts.show()
