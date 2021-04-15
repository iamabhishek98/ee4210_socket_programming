import socket, threading

NO_OF_CLIENTS = 10

HOST = socket.gethostname()
PORT = 54321

def execute(id):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    req = 'POST / HTTP/1.1\r\nHost: {HOST_IP}:{PORT}\r\nConnection: keep-alive\r\nContent-Length: 36\r\nCache-Control: max-age=0\r\nOrigin: http://{HOST_IP}:{PORT}\r\nUpgrade-Insecure-Requests: 1\r\nDNT: 1\r\nContent-Type: application/x-www-form-urlencoded\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nReferer: http://{HOST_IP}:{PORT}/\r\nAccept-Encoding: gzip, deflate\r\nAccept-Language: en-US,en;q=0.9\r\n\r\nentered_text=test+client'.format(HOST_IP = socket.gethostbyname(HOST), PORT = PORT)
    s.sendall(bytes(req,'utf-8'))
    print('Request Sent by Client',id)
    data = s.recv(1024)
    print('Updated Webpage Received by Client '+str(id)+':', data)
    s.close()

for i in range(1,NO_OF_CLIENTS+1):
    threading.Thread(target=execute,args=(i,)).start()

# b'GET / HTTP/1.1\r\nHost: 192.168.56.1:65432\r\nConnection: keep-alive\r\nDNT: 1\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nAccept-Encoding: gzip, deflate\r\nAccept-Language: en-US,en;q=0.9\r\n\r\n'


# GET /favicon.ico HTTP/1.1
# Host: 127.0.1.1:44103
# Connection: keep-alive
# User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36
# DNT: 1
# Accept: image/avif,image/webp,image/apng,image/*,*/*;q=0.8
# Sec-Fetch-Site: same-origin
# Sec-Fetch-Mode: no-cors
# Sec-Fetch-Dest: image
# Referer: http://127.0.1.1:44103/
# Accept-Encoding: gzip, deflate, br
# Accept-Language: en-US,en;q=0.9
