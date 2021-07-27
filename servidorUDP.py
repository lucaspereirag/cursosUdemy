import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(f'Socket criado com sucesso.')

host = 'localhost'
port = 5432

s.bind(host, port)  #Bind: Faz ligação entre cliente x servidor
mensagem = 'Servidor: Oi, cliente!'

while 1:
    dados, endereco = s.recvfrom(4096)

    if dados:
        print(f'Servidor enviado mensagem...')
        s.sendto(dados + mensagem.ecode(), endereco)