from os import error
import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print('A conexão falhou')
        print('Erro: {}'.format(e))
        sys.exit()

    print('Socket criado com sucesso')

    hostAlvo = input('Digite o host ou IP a ser conectado: ')
    portaAlvo = input('Digita a porta a ser conectada: ')

    try:
        s.connect((hostAlvo, int(portaAlvo)))
        print('Cliente TPC conectado com sucesso no Host ' + hostAlvo + ' e Porta ' + portaAlvo)
        s.shutdown(2)
    except socket.error as e:
        print('A conexão falhou')
        print('Erro: {}'.format(e))
        sys.exit()

if __name__ == '__main__':
    main()