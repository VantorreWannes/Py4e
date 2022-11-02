import socket
import re

url = input("URL -")
try:
    url = re.search(r'(\w+\.\w+(\.\w+)?)', url)[0]
except:
    print("Wrong URL format.")
    exit()

#data.pr4e.org
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((url, 80))
cmd = f'GET http://{url}/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')
mysock.close()

# Code: http://www.py4e.com/code3/socket1.py