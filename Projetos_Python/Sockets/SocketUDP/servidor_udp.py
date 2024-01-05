#Importa o módulo socket
from socket import *

#Define o servidor e a porta
servidor = "localhost"
porta = 43210

#Cria um objeto de socket usando a família de endereços 
#AF_INET e o tipo de socket SOCK_DGRAM
obj_socket = socket(AF_INET, SOCK_DGRAM)

#Associa o socket à porta e ao servidor especificados
obj_socket.bind((servidor, porta))

#Imprime uma mensagem indicando que o servidor está pronto
print("Servidor pronto....")

#Loop infinito para receber e enviar dados
while True:

    #Recebe dados do cliente junto com o endereço de origem
    dados, origem = obj_socket.recvfrom(65535)

    #Imprime o endereço de origem e os dados recebidos
    print("Origem..........: ", origem)
    print("Dados recebidos.: ", dados.decode())

    #Solicita ao usuário que digite uma resposta
    resposta = input("Digite a resposta: ")

    #Envia a resposta de volta para o cliente
    obj_socket.sendto(resposta.encode(), origem)

#Fecha o socket quando terminar
obj_socket.close()
