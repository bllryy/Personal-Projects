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

    # create socket
    

