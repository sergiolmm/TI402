
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

addr = get_ip()
port = 8080
print("Iniciando servidor no ip "+ addr + " na porta ->" + str(port))


def on_new_client(clientSocket, addr):
    print("Tratando dados de um conexao")
    while True:
        msgBruta = clientSocket.recv(1024)
        msgBase = msgBruta.decode()
        print('From -> '+ str(addr) + '\r\n Msg recebida : \r\n'+ msgBase )
        if (msgBase == 'fim'):
            break
        msg = "dados recebidos ok"
        clientSocket.send(msg.encode())

    print("conexão encerrada")
    clientSocket.close()    


def socketServer(addr,port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.bind((addr, port))
    except socket.error:
        sock.bind(('', port))
    
    sock.listen(1)

    while True:
        c, addr2 = sock.accept()
        _thread.start_new_thread(on_new_client, (c,addr2))

    sock.close()


print("inicando thread")
_thread.start_new_thread(socketServer, (addr,port))
while True:
    f = 10