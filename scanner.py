'''
Created on Jan 22, 2015

@author: pauli
'''
import socket
import argparse

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
            try:
                s = socket.socket()
                s.connect((IP, PORT))
                print "[+] Open port: ", PORT
                openPorts.append(PORT)
                PORT += 1
        
            except:
                PORT += 1
                continue
        
    
    print "\nOpen ports: ", openPorts

if __name__ == '__main__':
    Main()