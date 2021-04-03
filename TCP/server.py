import socket, threading, sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except:
    print('Failed to create socket! Exiting...')
    sys.exit()

try:
    HOST = socket.gethostname()  # Standard loopback interface address (localhost)
except:
    print('Hostname could not be resolved! Exiting...')
    sys.exit()

PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

s.bind((HOST, PORT))
s.listen()
print('Listening on '+str(socket.gethostbyname(HOST))+':'+str(PORT)+'...')

def onNewClient(conn,addr):
    print('Connected by', addr)
    data = conn.recv(1024)
    req = data.decode('utf-8').split(' ')
    if len(req):
        req_type = req[0]
        if req_type == "GET":
            print (data)
            print('Sent empty form to', addr)
            conn.sendall(
                b"HTTP/1.1 200 OK\n"
                + b"Content-Type: text/html\n"
                + b"\n"
                + b"<html><body><form method='post'><input type='text' name='entered_text' value='Enter Text Here'><input type='submit' value='Submit'></form></body></html>\n");
        else:
            try:
                entered_text = str(" ".join(req[-1].split('entered_text=')[1].split("+")))
                print (data)
                print('Sent updated webpage to', addr)
                conn.sendall(
                    b"HTTP/1.1 200 OK\n"
                    + b"Content-Type: text/html\n"
                    + b"\n"
                    + b"<html><body><b>Entered text:</b> \""
                    + bytes(entered_text,'utf-8')
                    + b"\"</body></html>\n");
            except:
                print('Invalid format!')

    conn.close()

while True:
    conn, addr = s.accept()
    threading.Thread(target=onNewClient,args=(conn,addr)).start()

s.close()