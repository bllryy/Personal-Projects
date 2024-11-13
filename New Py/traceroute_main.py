"""
Name: 
Section: 275-02
Desc: Project 1

"""

"""
Approach:
Get the empty arrays for hops and max hops
    also ttl if it dosent work
Spawn a send socket that sends the initial ping 
ping comes back and hits the recieve socket
print what we get back in the format
also web version in a website to get the line limit


while loop goes over and prints first location, second location, third, etc...
while ttl <= max_hops do while
"""


import socket
import struct
import time
#from scapy.all import *
import argparse
import string
import sys



def tracroute(destination, max_hops=30, timeout=5):
    destination = input("Enter the IP address or domain name of the destination: ")
    tracroute(destination)

    # hops
    hops = []
    ttl = 5

    #get ip
    dest_ip = socket.gethostbyname(destination)
    print(f"Traceroute to {destination} ({dest_ip}), max {max_hops} hops:")    



    while ttl <= max_hops:



        # create send/recieve socket
        recv_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
        send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

        # Set the ttl of the socket/options?????
        send_socket.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)
        recv_socket.settimeout(timeout)

        # send packet
        print(f"Sending packet with TTL = {ttl}...")
        start_time = time.time()
        send_socket.sendto(b'', (dest_ip), 33434) # port is common??????



if __name__ == "__main__":
    tracroute()
