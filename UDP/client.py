import socket, threading

NO_OF_CLIENTS = 10

HOST = socket.gethostname()
PORT = 12345

def execute(id):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    req = b'GET / HTTP/1.1\r\nHost: 192.168.56.1:65432\r\nConnection: keep-alive\r\nDNT: 1\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nAccept-Encoding: gzip, deflate\r\nAccept-Language: en-US,en;q=0.9\r\n\r\n'
    s.sendto(req,(HOST,PORT))
    data, addr = s.recvfrom(1024)
    print ('Data Received by Client '+str(id)+':',str(data))
    s.close()

for i in range(1,NO_OF_CLIENTS+1):
    threading.Thread(target=execute,args=(i,)).start()