import socket, os, sys

try:
    HOST = socket.gethostname()
except:
    print('Hostname could not be resolved! Exiting...')
    sys.exit()

PORT = 12345

def createHTTPResponse(addr,body):
    HTTPResponse = ("HTTP/1.1 200 OK\r\n"
                + "Host: {}:{}\r\n".format(addr[0],addr[1])
                + "Accept-Ranges: bytes\r\n"
                + "Content-Length: {}\r\n".format(len(body))
                + "Content-Type: text/html\r\n"
                + "\r\n" + body)
    return bytes(HTTPResponse, 'utf-8')

def onNewClent(conn, addr):
    data = conn.decode('utf8')
    if "GET / HTTP/1.1" in data:
        body = "<html><body>EE-4210:Continuous assessment</body></html>\n"
        s.sendto(createHTTPResponse(addr,body),addr)
        print('Sent webpage to {}:{}'.format(addr[0],addr[1]))

if __name__ == '__main__':
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except:
        print('Failed to create socket! Exiting...')
        sys.exit()
    
    s.bind((HOST, PORT))
    print('Socket binded to '+str(socket.gethostbyname(HOST))+':'+str(PORT))
    
    while True:
        conn, addr = s.recvfrom(1024)
        pid = os.fork()
        if pid == 0:
            onNewClent(conn, addr)
            sys.exit()