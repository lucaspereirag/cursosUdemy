import socket

#Objeto de conexão
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Verifica se foi criado:
print(f'Cliente Socket criado com sucesso {s}')

host = 'localhost'
porta = 5433
msg = 'Olá, servidor. Recebendo mensagem?'

try:
    print(f'Cliente: {msg}')
    #espera resposta do servidor:
    s.sendto(msg.encode(), (host, 5432)) #encode: empacotamento da mensagem

    dados, servidor = s.recvfrom(4096)
    dados = dados.decode() #desempacota dados
    print(f'Cliente: {dados}')
finally:
    print(f'Cliente: Fechando a conexão')
    s.close()