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

done = False

def receive_messages():
    while not done:
        try:
            MENSAGEM = cliente.recv(TAMANHO_BUFFER).decode('utf-8')

            if MENSAGEM == "@username":
                cliente.send(username.encode('utf-8'))
            
            elif MENSAGEM == "QUIT":
                cliente.close 
                done = True       
            
            else:
                print(MENSAGEM)
        except:
            print("Ocorreu um erro")
            cliente.close
            done = True

def write_messages():
    while True:
        MENSAGEM = f"{username}: {input('')}"
        cliente.send(MENSAGEM.encode('utf-8'))

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

write_thread = threading.Thread(target=write_messages)
write_thread.start()

















# # envia mensagem para servidor 
# cliente.send(MENSAGEM.encode('UTF-8'))

# # recebe dados do servidor 
# data, addr = cliente.recvfrom(1024)

# # fecha conexão com servidor
# cliente.close()

# print ("received data:", data)
