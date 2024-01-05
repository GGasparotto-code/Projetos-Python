#Função para preencher o inventário
def preeencherInventario(lista):

    #Inicializa a resposta para continuar preenchendo o inventário
    resp = "S"

    #Loop que continua enquanto a resposta for "S"
    while resp == "S":

        #Solicita ao usuário que insira os detalhes do equipamento
        equipamento = [input("Equipamento: "),
                   float(input("Valor: ")),
                   int(input("Número Serial: ")),
                   input("Departamento: ")]
    
    # Adiciona o equipamento à lista
    lista.append(equipamento)

    #Solicita ao usuário se deseja continuar inserindo equipamentos
    resp = input("Digite \"S\" para continuar: ").upper()

#Função para exibir o inventário
def exibirInventario(lista):

    #Loop que percorre cada equipamento na lista
    for elemento in lista:

        #Imprime os detalhes do equipamento
        print("Nome.........: ", elemento[0])
        print("Valor........: ", elemento[1])
        print("Serial.......: ", elemento[2])
        print("Departamento.: ", elemento[3])

#Função para localizar um equipamento pelo nome
def localizaPorNome(lista):

    #Solicita ao usuário o nome do equipamento que deseja buscar
    busca = input("\nDigite o nome do equipamento que deseja buscar: ")

    #Loop que percorre cada equipamento na lista
    for elemento in lista:

        #Condição para que se o nome do equipamento corresponder à busca, imprime os detalhes
        if busca == elemento[0]:
            print("Valor..: ", elemento[1])
            print("Serial.: ", elemento[2])

#Função para depreciar um equipamento pelo nome
def depreciarPorNome(lista, porc):

    #Solicita ao usuário o nome do equipamento que será depreciado
    depreciacao = input("\nDigite o nome do equipamento que será depreciado: ")

    #Loop que percorre cada equipamento na lista
    for elemento in lista:

        #Se o nome do equipamento corresponder à depreciação, 
        #calcula o novo valor e imprime os detalhes
        if depreciacao == elemento[0]:
            print("Valor antigo: ", elemento[1])
            elemento[1] = elemento[1] * (1 - porc/100)
            print("Novo valor: ", elemento[1])

#Função para excluir um equipamento pelo número de série
def excluirPorSerial(lista):

    #Solicita ao usuário o número de série do equipamento que será excluído
    serial = int(input("\nDigite o serial do equipamento que será excluido: "))

    #Loop que percorre cada equipamento na lista
    for elemento in lista:

        # Se o número de série do equipamento corresponder ao solicitado, 
        #remove o equipamento da lista
        if elemento[2] == serial:
            lista.remove(elemento)
    
    #Retorna uma mensagem indicando que os itens foram excluídos
    return "Itens excluídos."

#Função para resumir os valores dos equipamentos no inventário
def resumirValores(lista):

    #Cria uma lista para armazenar os valores dos equipamentos
    valores = []

    #Loop que percorre cada equipamento na lista
    for elemento in lista:

        #Adiciona o valor do equipamento à lista de valores
        valores.append(elemento[1])
    
    #Condição se caso houver valores na lista
    if len(valores) > 0:

        #Imprime o equipamento mais caro, o mais barato e o total
        print("O equipamento mais caro custa: ", max(valores))
        print("O equipamento mais barato custa: ", min(valores))
        print("O total de equipamento é de: ", sum(valores))
            