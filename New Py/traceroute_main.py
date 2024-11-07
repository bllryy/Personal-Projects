"""
ADD name and stuff


"""

"""
Approach:
Get the empty arrays for hops and max hops
    also ttl if it dosent work
Spawn a send socket that sends the initial ping 
ping comes back and hits the recieve socket
print what we get back in the format
also web version in a website to get the line limit ( ͡° ͜ʖ ͡°) 

"""






import socket
import struct
import time
from scapy.all import *
import argparse
import string
import sys



def tracroute(destination, max_jumps=30, callout=5):    # callout is for timeout
    # hops
    hops = []
    # max hops
    max_hops = 30
    # TTL
    ttl = 5

    # create socket
    receivesocket = socket.socket() # NEED STUFF IN HERE
    sendsocket = socket.socket()    # ^^^^

    # Set the ttl of the socket
    sendsocket.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)


