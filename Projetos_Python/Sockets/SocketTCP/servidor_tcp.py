#Importa o módulo socket
from socket import *

#Define o servidor e a porta
servidor = "localhost"
porta = 43210

#Cria um objeto socket
obj_socket = socket(AF_INET, SOCK_STREAM)

#Vincula o objeto socket ao endereço IP e à porta especificados
obj_socket.bind((servidor,porta))

#Coloca o objeto socket em modo de escuta, aceitando até 2 conexões pendentes
obj_socket.listen(2)

#Imprime uma mensagem indicando que está aguardando um cliente
print("Aguardando cliente....")

#Loop infinito para aceitar várias conexões
while True:

    #Aceita uma nova conexão
    con, cliente = obj_socket.accept()

    #Imprime o endereço do cliente
    print("Conectando com: ", cliente)

    #Loop para receber e responder às mensagens do cliente
    while True:

        #Recebe uma mensagem do cliente
        msg_recebida = str(con.recv(1024))

        #Imprime a mensagem recebida
        print("Recebemos: ", msg_recebida)

        #Envia uma mensagem de resposta ao cliente
        msg_enviada = b"Olah cliente"
        con.send(msg_enviada)

        #Interrompe o loop interno após enviar uma mensagem
        break

    #Fecha a conexão com o cliente
    con.close()
    