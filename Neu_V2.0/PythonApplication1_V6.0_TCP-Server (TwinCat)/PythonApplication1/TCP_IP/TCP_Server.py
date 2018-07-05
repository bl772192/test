
import socket
import sys
import threading
import time
exitflag=0;


class TCP_Server():
    # Initialization
    def __init__(self, server_address):
        self.server_address=server_address

    # Creating TCP/IP Listener Socket
    def run(self):
                
        # Create and bind socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(self.server_address)

        # Listen for incoming connections
        sock.listen(1)
        while True:
            # Wait for a connection
            connection, client_address = sock.accept()
            try:
                while True:
                    scan_value = connection.recv(128)
                    if scan_value:
                        connection.sendall(scan_value)
                        print (scan_value)
                    else:
                        print >>sys.stderr, 'No more data from', client_address
                        break          
            finally:
                # Clean up the connection
                connection.close()