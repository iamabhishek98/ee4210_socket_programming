import socket

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except:
    print('Failed to create socket. Exiting...')
    sys.exit()
print('Successfully created socket')

try:
    HOST = socket.gethostname()  # Standard loopback interface address (localhost)
except:
    print('Hostname could not be resolved. Exiting...')
    sys.exit()

PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

s.bind((HOST, PORT))
s.listen()
print('Listening on '+str(socket.gethostbyname(HOST))+':'+str(PORT)+'...')
while True:
    conn, addr = s.accept()
    print('Connected by', addr)
    data = conn.recv(1024)
    if not data:
        break
    # conn.sendall(data)
    conn.sendall(
        b"HTTP/1.1 200 OK\n"
        + b"Content-Type: text/html\n"
        + b"\n"
        + b"<html><body>Hello World</body></html>\n");
    conn.close()