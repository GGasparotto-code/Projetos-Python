#Importa o módulo socket, que permite realizar operações de rede, 
#como conversão de nomes de domínio em endereços IP
import socket

#Define a resposta inicial como "S", indicando que o programa deve continuar
resp = "S"

#Loop que continua enquanto a resposta for "S"
while(resp == "S"):

    #Solicita ao usuário que digite uma URL
    url = input("Digite uma url: ")

    #Usa a função gethostbyname do módulo socket para 
    #converter o nome de domínio em um endereço IP
    ip = socket.gethostbyname(url)

    #Imprime o endereço IP correspondente à URL fornecida
    print("O IP referente a url informada é: ", ip)

    #Solicita ao usuário que digite algo para continuar ou parar o loop
    resp = input("Digite <s> para continuar: ").upper()
    