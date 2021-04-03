import socket, threading

NO_OF_CLIENTS = 10

HOST = socket.gethostname()
PORT = 12345

def execute(id):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto("Request".encode('utf-8'),(HOST,PORT))
    data, addr = s.recvfrom(1024)
    print ('Data Received by Client '+str(id)+':',str(data))
    s.close()

for i in range(1,NO_OF_CLIENTS+1):
    threading.Thread(target=execute,args=(i,)).start()