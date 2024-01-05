#Importa o módulo socket
from socket import *

#Define o servidor e a porta para conexão
servidor = "localhost"
porta = 43210

#Cria um objeto de socket UDP
obj_socket = socket(AF_INET, SOCK_DGRAM)

#Conecta o socket ao servidor e porta especificados
obj_socket.connect((servidor, porta))

#Inicializa a variável de saída para uma string vazia
saida = ""

#Loop que continua enquanto a saída não for igual a "X"
while saida != "X":

    #Solicita ao usuário uma mensagem para enviar
    msg = input("Sua mensagem: ")

    #Envia a mensagem codificada para o servidor
    obj_socket.sendto(msg.encode(), (servidor, porta))

    #Recebe dados do servidor
    dados, origem = obj_socket.recvfrom(65535)

    #Imprime a resposta do servidor
    print("Resposta do Servidor: ", dados.decode())

    #Solicita ao usuário digitar "X" para sair
    saida = input("Digite <X> para sair: ").upper()

#Fecha o socket após o término das operações
obj_socket.close()
