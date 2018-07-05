
if __name__ == "__main__":

    from TCP_IP import TCP_Server

    server_address = ('localhost', 9877)
    New_Server=TCP_Server.TCP_Server(server_address)
    New_Server.run()