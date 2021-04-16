import socket, os, sys

# chooses an available port
PORT = 0

# creates a HTTP response string
def createHTTPResponse(addr,body):
    HTTPResponse = ("HTTP/1.1 200 OK\r\n"
                + "Host: {}:{}\r\n".format(addr[0],addr[1])
                + "Accept-Ranges: bytes\r\n"
                + "Content-Length: {}\r\n".format(len(body))
                + "Content-Type: text/html\r\n"
                + "\r\n" + body)
    
    # converts HTTP response string to bytes
    return bytes(HTTPResponse, 'utf-8')

def onNewClent(conn, addr):
    # receives data from client and decodes the bytes
    data = conn.decode('utf8')
    # checks for valid GET request
    if "GET / HTTP/1.1" in data:
        # html webpage with an empty form
        body = "<html><body>EE-4210:Continuous assessment</body></html>\n"
        # sends webpage to the client
        s.sendto(createHTTPResponse(addr,body),addr)
        print('Sent webpage to {}:{}'.format(addr[0],addr[1]))

if __name__ == '__main__':
    try:
        # obtains default host address
        HOST = socket.gethostname()
    except:
        print('Hostname could not be resolved! Exiting...')
        sys.exit()

    try:
        # creates UDP socket
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except:
        print('Failed to create socket! Exiting...')
        sys.exit()
    
    # binds UDP socket to the specified port
    s.bind((HOST, PORT))
    print('Socket binded to '+str(socket.gethostbyname(HOST))+':'+str(s.getsockname()[1]))
    
    while True:
        try:
            # receives data from clients
            conn, addr = s.recvfrom(1024)
            # forks the process
            pid = os.fork()
            # checks if fork operation was successful
            if pid == 0:
                onNewClent(conn, addr)
                sys.exit()
        except KeyboardInterrupt:
            break
    
    if s: 
        s.close()