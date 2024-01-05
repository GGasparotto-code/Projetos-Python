#Inicializa listas vazias para armazenar detalhes do equipamento
equipamentos = []
valores = []
seriais = []
departamentos = []

#Define o valor inicial para a variável de controle do loop
resposta = "S"

#Loop para coletar detalhes do equipamento
while resposta == "S":
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Número Serial: ")))
    departamentos.append(input("Departamento: "))
    resposta = input("Digite \"S\" para continuar: ").upper()

#Solicita ao usuário o nome do equipamento que deseja pesquisar
busca = input("\nDigite o nome do equipamento que deseja buscar: ")

#Comando for para percorrer a lista de equipamentos
for indice in range(0, len(equipamentos)):

    #Comando if caso o equipamento pesquisado corresponde ao equipamento atual na lista
    if busca == equipamentos[indice]:

        #Imprime o valor e número de série do equipamento correspondente
        print("Valor..: ", valores[indice])
        print("Serial..: ", seriais[indice])
        