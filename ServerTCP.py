import socket
import threading #importa modulo socket
 
TCP_IP = '127.0.0.1' # endereço IP do servidor 
TCP_PORTA = 42005       # porta disponibilizada pelo servidor
TAMANHO_BUFFER = 1024     # definição do tamanho do buffer
 
# Criação de socket TCP
# SOCK_STREAM, indica que será TCP.
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# IP e porta que o servidor deve aguardar a conexão
servidor.bind((TCP_IP, TCP_PORTA))

#Define o limite de conexões. 
servidor.listen()

print(f"Servidor {TCP_IP} dispoivel na porta {TCP_PORTA} e escutando.....") 

clientes = []
usernames = []

def broadcast(MENSAGEM, _cliente):
    for cliente in clientes:
        if cliente != _cliente:
            cliente.send(MENSAGEM)

def handle_messages(cliente):
    while True:
        try:
            MENSAGEM = cliente.recv(TAMANHO_BUFFER)
            broadcast(MENSAGEM,cliente)

        except:
            index = clientes.index(cliente)
            clientes.remove(cliente)
            cliente.close()
            username = usernames[index]
            broadcast(f"Chatbot: {username} desconectado".encode('utf-8'), cliente)
            
            usernames.remove(username)
            
            break

def receive_connections():
    while True:
        cliente, address = servidor.accept()
        cliente.send("@username".encode('utf-8'))
        username = cliente.recv(TAMANHO_BUFFER).decode('utf-8')
        clientes.append(cliente)
        usernames.append(username)
        print(f"{username} esta conectado com {str(address)}")
        MENSAGEM = f"ChatBot: {username} entrou no chat!".encode('utf-8')
        broadcast(MENSAGEM,cliente)
        cliente.send("Conectado ao server".encode('utf-8'))
        
        thread = threading.Thread(target=handle_messages, args=(cliente,))
        thread.start()

receive_connections()






# # Aceita conexão 
# conn, addr = servidor.accept()
# print ('Endereço conectado:', addr)
# while 1:
#     #dados retidados da mensagem recebida
#     data = conn.recv(TAMANHO_BUFFER)
#     if data: 
#         print ("Mensagem recebida:", data)  
#         conn.send(data.upper())  # envia dados recebidos em letra maiuscula 

