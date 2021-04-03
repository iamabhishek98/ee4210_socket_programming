import socket
import threading

HOST = socket.gethostname()  # The server's hostname or IP address
PORT = 65432        # The port used by the server

def thread_fn(id):
    for i in range(1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        s.sendall(b'Hello, world')
        data = s.recv(1024)
        print(id,'Received', repr(data))

x = threading.Thread(target=thread_fn,args=(1,))
# y = threading.Thread(target=thread_fn,args=(2,))
# z = threading.Thread(target=thread_fn,args=(3,))
x.start()
# y.start()
# z.start()