'''
Created on Jan 22, 2015
@author: pauli
'''
import argparse
import socket
import time
import sys


def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("Ip", help='Target ip address', type=str)
    parser.add_argument("Start_port", help='Starting port', type=int)
    parser.add_argument("End_port", help='Ending port', type=int)
    args = parser.parse_args()
    
    IP = args.Ip
    PORT = args.Start_port
    END_PORT = args.End_port
    openPorts = []
    socket.setdefaulttimeout(2)
    
    while PORT <= END_PORT:
        percentage = (float(PORT)) / (float(END_PORT)) * 100
        time.sleep(0.005)
        
        
        try:
                s = socket.socket()
                s.connect((IP, PORT))
                openPorts.append(PORT)
                sys.stdout.write("\rCompleted: " + '#' * (int(percentage) / 5) + " %d%%" % percentage)
                sys.stdout.flush()
                PORT += 1
                
        except:
                sys.stdout.write("\rCompleted: " + '#' * (int(percentage) / 5) + " %d%%" % percentage)
                sys.stdout.flush()
                PORT += 1
    
    print "\nOpen ports found: ",openPorts             
        
    

if __name__ == '__main__':
    Main()