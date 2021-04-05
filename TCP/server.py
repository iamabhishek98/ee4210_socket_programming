import socket, os, sys, urllib.parse

try:
    HOST = socket.gethostname()
except:
    print('Hostname could not be resolved! Exiting...')
    sys.exit()

PORT = 54321

def onNewClient(conn,addr):
    print('Connected by', addr)
    data = conn.recv(1024).decode('utf-8')
    if "GET / HTTP/1.1" in data:
        print('Sent empty form to', addr)
        conn.sendall(
            b"HTTP/1.1 200 OK\n"
            + b"Content-Type: text/html\n"
            + b"\n"
            + b"<html><body><form method='post'><input type='text' name='entered_text' value='Enter Text Here'><input type='submit' value='Submit'></form></body></html>\n")
    elif "POST / HTTP/1.1" in data and "entered_text=" in data:
        try:
            entered_text = urllib.parse.unquote(data.split('entered_text=')[1].replace("+","&nbsp"))
            print('Sent updated webpage to', addr)
            conn.sendall(
                b"HTTP/1.1 200 OK\n"
                + b"Content-Type: text/html\n"
                + b"\n"
                + b"<html><body><b>Entered text:</b> \""
                + bytes(entered_text,'utf-8')
                + b"\"</body></html>\n")
        except:
            print('Invalid format!')

    conn.close()

if __name__ == '__main__':
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except:
        print('Failed to create socket! Exiting...')
        sys.exit()
    
    s.bind((HOST, PORT))
    s.listen()
    print('Listening on '+str(socket.gethostbyname(HOST))+':'+str(PORT))

    while True:
        conn, addr = s.accept()
        child_pid = os.fork()
        if child_pid == 0:
            onNewClient(conn,addr)
            conn.close()
            sys.exit()
        conn.close()
    s.close()