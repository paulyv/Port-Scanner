'''
Created on Jan 22, 2015
@author: pauli
'''
import argparse
import socket
import time


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
       
        time.sleep(0.005)
        print(chr(27) + "[2J")
        percentage = (float(PORT)) / (float(END_PORT)) * 100
        
        try:
                s = socket.socket()
                s.connect((IP, PORT))
                print "[+] Open port: ", PORT
                openPorts.append(PORT)
                print percentage, "% Completed"
                print "\nOpen ports: ", openPorts
                PORT += 1
                
        except:
                print percentage, "% Completed"
                print "\nOpen ports: ", openPorts
                PORT += 1
             
        
    

if __name__ == '__main__':
    Main()