import socket

HOST = "HOST" # '192.168.43.82'
PORT = "PORTA" # 2222
server = socket.socket()
server.bind((HOST, PORT))
print('[+] Iniciando Server')
print('[+] Ouvindo cliente')
server.listen(1)
client, client_addr = server.accept()
print(f'[+] {client_addr} Cliente conectado no servidor')

while True:
    command = input("Digite o comando")
    command = command.encode()
    client.send(command)
    print('[+] Enviando comando')
    output = client.recv(1024)
    output = output.decode()
    print(f"Output: {output}")