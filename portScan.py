import socket
import sys


host = str(sys.argv[1])

print(host)
ports = [22,23,80,443,3306,5512]

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.settimeout(10)

for port in ports:
    res = server.connect_ex((host, port))
    if res == 0:
        print("Porta", port, "aberta")
    elif res == 106:
        print("Porta",port,"aberta porem ja em uso pelo server")
    else:
        print("Porta", port, "fechada")
        print("Erro:", res)
