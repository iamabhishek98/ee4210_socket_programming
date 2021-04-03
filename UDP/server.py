import socket, threading

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except:
    print('Failed to create socket! Exiting...')
    sys.exit()

try:
    HOST = socket.gethostname()
except:
    print('Hostname could not be resolved! Exiting...')
    sys.exit()

PORT = 12345

s.bind((HOST, PORT))
print('Socket binded to '+str(socket.gethostbyname(HOST))+':'+str(PORT))


while True:
    conn, addr = s.recvfrom(1024)
    s.sendto(
        b"HTTP/1.1 200 OK\n"
        + b"Content-Type: text/html\n"
        + b"\n"
        + b"<html><body>EE-4210:Continuous assessment</body></html>\n",addr)
    print('Data sent to', addr)

s.close()