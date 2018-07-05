if __name__ == "__main__":
    
    import TCP_IP
    import os
    import sys
    
    ws = TCP_IP.PyWSock()
    ws.start_server(9876)