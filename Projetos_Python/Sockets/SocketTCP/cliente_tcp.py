#Importa o módulo socket
from socket import *

#Define o servidor e a porta
servidor = "localhost"
porta = 43210

#Solicita ao usuário que digite uma mensagem
msg = bytes(input("Digite algo: "), "utf-8")

#Cria um objeto socket
obj_socket = socket(AF_INET, SOCK_STREAM)

#Conecta o objeto socket ao servidor e porta especificados
obj_socket.connect((servidor, porta))

#Envia a mensagem digitada pelo usuário para o servidor
obj_socket.send(msg)

#Recebe a resposta do servidor
resposta = obj_socket.recv(1024)

#Imprime a resposta recebida
print("Recebemos: ", resposta)

#Fecha a conexão
obj_socket.close()
