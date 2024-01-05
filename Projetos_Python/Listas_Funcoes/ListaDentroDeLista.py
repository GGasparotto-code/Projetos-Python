#Inicializa a lista de inventário e a variável de resposta
inventario = []
resposta = "S"

#Loop para adicionar equipamentos ao inventário
while resposta == "S":

    #Solicita ao usuário que insira detalhes do equipamento
    equipamento = [input("Equipamento: "),
                   float(input("Valor: ")),
                   int(input("Número Serial: ")),
                   input("Departamento: ")]
    
    #Adiciona o equipamento ao inventário
    inventario.append(equipamento)

    #Pergunta ao usuário se deseja continuar
    resposta = input("Digite \"S\" para continuar: ").upper()

#Imprime todos os equipamentos no inventário
for elemento in inventario:
    print("Nome.........: ", elemento[0])
    print("Valor........: ", elemento[1])
    print("Serial.......: ", elemento[2])
    print("Departamento.: ", elemento[3])

#Solicita ao usuário que digite o nome do equipamento que deseja buscar
busca = input("\nDigite o nome do equipamento que deseja buscar: ")

#Busca o equipamento no inventário
for elemento in inventario:
    if busca == elemento[0]:
        print("Valor..: ", elemento[1])
        print("Serial.: ", elemento[2])

#Solicita ao usuário que digite o nome do equipamento que será depreciado
depreciacao = input("\nDigite o nome do equipamento que será depreciado: ")

#Deprecia o equipamento no inventário
for elemento in inventario:
    if busca == elemento[0]:
        print("Valor antigo: ", elemento[1])
        elemento[1] = elemento[1] * 0.9
        print("Novo valor: ", elemento[1])

#Solicita ao usuário que digite o serial do equipamento que será excluído
serial = int(input("\nDigite o serial do equipamento que será excluido: "))

#Exclui o equipamento do inventário
for elemento in inventario:
    if elemento[2] == serial:
        inventario.remove(elemento)

#Imprime todos os equipamentos restantes no inventário após a exclusão
for elemento in inventario:
    print("Nome.........: ", elemento[0])
    print("Valor........: ", elemento[1])
    print("Serial.......: ", elemento[2])
    print("Departamento.: ", elemento[3])

#Calcula e imprime o valor do equipamento mais caro, o mais barato 
#e o total de equipamentos no inventário
valores = []
for elemento in inventario:
    valores.append(elemento[1])
if len(valores) > 0:
    print("O equipamento mais caro custa: ", max(valores))
    print("O equipamento mais barato custa: ", min(valores))
    print("O total de equipamento é de: ", sum(valores))
    