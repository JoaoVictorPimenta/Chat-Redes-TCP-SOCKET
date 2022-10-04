#Claudia Fiorentino Andrade - 42005302
#João Victor Pimenta - 42005876
import socket
import threading #importa modulo socket

TCP_IP = '127.0.0.1' # endereço IP do servidor 
TCP_PORTA = 42005      # porta disponibilizada pelo servidor
TAMANHO_BUFFER = 1024

username = input("Insira seu username: ")

# Criação de socket TCP do cliente
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Conecta ao servidor em IP e porta especifica 
cliente.connect((TCP_IP, TCP_PORTA))

def receber_mensagens():
    while True:
        try:
            MENSAGEM = cliente.recv(TAMANHO_BUFFER).decode('utf-8')

            if MENSAGEM == "@username":
                cliente.send(username.encode('utf-8'))   
            
            else:
                print(MENSAGEM)
        except:
            print("Ocorreu um erro")
            cliente.close
            break

def escrever_mensagens():
    while True:
        MENSAGEM = f"{username}: {input('')}"
        cliente.send(MENSAGEM.encode('utf-8'))

receber_thread = threading.Thread(target=receber_mensagens)
receber_thread.start()

escrever_thread = threading.Thread(target=escrever_mensagens)
escrever_thread.start()

















# # envia mensagem para servidor 
# cliente.send(MENSAGEM.encode('UTF-8'))

# # recebe dados do servidor 
# data, addr = cliente.recvfrom(1024)

# # fecha conexão com servidor
# cliente.close()

# print ("received data:", data)
