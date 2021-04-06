import socket, os, sys, urllib.parse

try:
    HOST = socket.gethostname()
except:
    print('Hostname could not be resolved! Exiting...')
    sys.exit()

PORT = 0 # 54321

def onNewClient(conn,addr):
    data = conn.recv(1024).decode('utf-8')
    if "GET / HTTP/1.1" in data:
        print('Sent empty form to', addr)
        conn.sendall(
            b"HTTP/1.1 200 OK\r\n"
            + b"Connection: keep-alive\r\n"
            + b"Content-Type: text/html\r\n"
            + b"\r\n"
            + b"<html><body><form method='post'>Enter text here:<br/><input type='text' name='entered_text' value=''><input type='submit' value='Submit'></form></body></html>\n")
    elif "POST / HTTP/1.1" in data and "entered_text=" in data:
        try:
            entered_text = urllib.parse.unquote(data.split('entered_text=')[1].replace("+","&nbsp"))
            print('Sent updated webpage to', addr)
            conn.sendall(
                b"HTTP/1.1 200 OK\r\n"
                + b"Connection: keep-alive\r\n"
                + b"Content-Type: text/html\r\n"
                + b"\r\n"
                + b"<html><body><b>You typed:</b> \"" + bytes(entered_text,'utf-8') + b"\"</body></html>\n")
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
                print('Connection with socket {} started'.format(addr[1]))    
                onNewClient(conn,addr)
                conn.close()
                conn = None
                print('Connection with socket {} closed'.format(addr[1]))
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
