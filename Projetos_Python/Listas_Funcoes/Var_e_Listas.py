#Inicializa uma lista vazia 
inventario = []

#Define o valor inicial para a variável de controle do loop
resposta = "S"

#Loop para enquanto a resposta for igual a "S"
while resposta == "S":
    inventario.append(input("Equipamento: "))
    inventario.append(float(input("Valor: ")))
    inventario.append(int(input("Número Serial: ")))
    inventario.append(input("Departamento: "))
    resposta = input("Digite \"S\" para continuar: ").upper()

#Comando for para imprimir cada item no inventário
for elemento in inventario:
    print(elemento)