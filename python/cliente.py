import socket
import struct
import sys
import _thread

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255',1))
        IP = s.getsockname()[0]
    except socket.error:
        print(socket.error)
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def sendHttpRequest(addr):
    resp = (
        'GET https://slmm.com.br/ws/exe1/index2.php?id=3&tipo=json HTTP/1.1\r\n'
        'HOST: '+addr+'\r\n'
        '\r\n'
    )
    return resp

slmm = '185.201.11.211' 
addr = '192.168.15.163'
port = 80

print("iniciando cliente")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect((slmm, port))
except socket.error:
    print('Erro ao conectar')    
    
msg = sendHttpRequest(addr)
print(msg)
sock.send(msg.encode())
data = sock.recv(1024)
print(data.decode())
sock.close()

'''
print("Para sair digite CRTL+X\n")
msg = input() 
while msg != '\x18':    
    sock.send(msg.encode())
    data = sock.recv(1024)
    print("From " + str(addr) + 'dados \n'+ data.decode())
    msg = input()
    

msg = 'fim'
sock.send(msg.encode())
'''

sock.close()