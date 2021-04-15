import socket, os, sys, urllib.parse

try:
    HOST = socket.gethostname()
except:
    print('Hostname could not be resolved! Exiting...')
    sys.exit()

PORT = 0 # 54321

def createHTTPResponse(addr,body):
    HTTPResponse = ("HTTP/1.1 200 OK\r\n"
                + "Host: {}:{}\r\n".format(addr[0],addr[1])
                + "Accept-Ranges: bytes\r\n"
                + "Content-Length: {}\r\n".format(len(body))
                + "Content-Type: text/html\r\n"
                + "\r\n" + body)
    return bytes(HTTPResponse, 'utf-8')

def onNewClient(conn,addr):
    data = conn.recv(1024).decode('utf-8')
    if "GET / HTTP/1.1" in data:
        print('Sent empty form to {}:{}'.format(addr[0],addr[1]))
        body = "<html><body><form method='post'>Enter text here:<br/><input type='text' name='entered_text' value=''><input type='submit' value='Submit'></form></body></html>\n"
        conn.sendall(createHTTPResponse(addr,body))
    elif "POST / HTTP/1.1" in data and "entered_text=" in data:
        try:
            entered_text = urllib.parse.unquote(data.split('entered_text=')[1].replace("+","&nbsp"))
            print('Sent updated webpage to {}:{}'.format(addr[0],addr[1]))
            body = "<html><body><b>You typed:</b> \"" + entered_text + "\"</body></html>\n"
            conn.sendall(createHTTPResponse(addr,body))
        except:
            print('Invalid format!')

if __name__ == '__main__':
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except:
        print('Failed to create socket! Exiting...')
        sys.exit()
    
    s.bind((HOST, PORT))
    s.listen()
    print('Listening on {}:{}'.format(socket.gethostbyname(HOST),s.getsockname()[1]))

    while True:
        try:
            conn = None
            conn, addr = s.accept()
            pid = os.fork()
            if pid == 0:
                s.close() # close listen port
                s = None
                onNewClient(conn,addr)
                conn.close()
                conn = None
                sys.exit()
            conn.close()
            conn = None
        except KeyboardInterrupt:
            if conn: conn.close()
            break
    
    if s: 
        print('Listen process on {}:{} stopped'.format(socket.gethostbyname(HOST),s.getsockname()[1]))
        s.close()
    sys.exit()
