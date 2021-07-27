import socket
import sys


def main():
    #Tenta conectar com TCP/IP
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        # Se der erro ao tentar estabelecer conexão:
    except socket.error as e:
        print(f'A conexão falhou.')
        print(f'Erro: {e}')
        sys.exit()
    else:
        print("Socket criado com sucesso.")

    #Host a ser conectado
    HostAlvo = input('Digite o Host ou IP a ser conectado: ')
    PortaAlvo = input('Digite a Porta do Host: ')

    #Tenta conexão:
    try:
        s.connect((HostAlvo, int(PortaAlvo)))
        print(f'Cliente TCP conectado com sucesso no Host: {HostAlvo} '
              f'e na Porta {PortaAlvo}')
        s.shutdown(2)
    except socket.error as e:
        print(f'Tentativa de conexão com Host: {HostAlvo} e Porta {PortaAlvo}, falhou.')
        print(f'Erro: {e}')
        sys.exit() #  sair da aplicação


if __name__ == "__main__":
    main()