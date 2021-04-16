import socket, os, sys, urllib.parse

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

# serves new clients which attempt to connect to the server
def onNewClient(conn,addr):
    # receives data from client and decodes the bytes
    data = conn.recv(1024).decode('utf-8')
    # checks for valid GET request
    if "GET / HTTP/1.1" in data:
        # html webpage with an empty form
        body = "<html><body><form method='post'>Enter text here:<br/><input type='text' name='entered_text' value=''><input type='submit' value='Submit'></form></body></html>\n"
        # sends webpage to the client
        conn.sendall(createHTTPResponse(addr,body))
        print('Sent empty form to {}:{}'.format(addr[0],addr[1]))
    # checks for valid POST request
    elif "POST / HTTP/1.1" in data and "entered_text=" in data:
        try:
            # parses entered form input
            entered_text = urllib.parse.unquote(data.split('entered_text=')[1].replace("+","&nbsp"))
            # html webpage with entered form input
            body = "<html><body><b>You typed:</b> \"{}\"</body></html>\n".format(entered_text)
            # sends updated webpage to the client
            conn.sendall(createHTTPResponse(addr,body))
            print('Sent updated webpage to {}:{}'.format(addr[0],addr[1]))
        except:
            print('Invalid format!')

if __name__ == '__main__':
    try:
        # obtains default host address
        HOST = socket.gethostname()
    except:
        print('Hostname could not be resolved! Exiting...')
        sys.exit()
    
    try:
        # creates TCP socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except:
        print('Failed to create socket! Exiting...')
        sys.exit()

    # binds TCP socket and starts listening on the specified port
    s.bind((HOST, PORT))
    s.listen()
    print('Listening on {}:{}'.format(socket.gethostbyname(HOST),s.getsockname()[1]))

    while True:
        try:
            # accepts connection
            conn, addr = s.accept()
            # forks the process
            pid = os.fork()
            # checks if fork operation was successful
            if pid == 0:
                # closes listen port
                s.close()
                onNewClient(conn,addr)
                # closes connection to client
                conn.close()
                sys.exit()
            conn.close()
        except KeyboardInterrupt:
            if conn: conn.close()
            break
    
    if s: 
        s.close()
