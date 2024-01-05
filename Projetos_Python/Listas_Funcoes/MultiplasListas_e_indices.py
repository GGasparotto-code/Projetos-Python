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

#Comando for para imprimir as informações dos equipamentos
for indice in range(0 ,len(equipamentos)):
    print("\nEquipamento..: ", (indice + 1))
    print("Nome.........: ", equipamentos[indice])
    print("Valor........: ", valores[indice])
    print("Serial.......: ", seriais[indice])
    print("Departamento.: ", departamentos[indice])