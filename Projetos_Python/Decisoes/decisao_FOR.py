#Solicita ao usuário que insira um número para exibir a tabuada
tabuada = int(input("Digite um número para exibir a tabuada: "))

#Imprime o título da tabuada
print("tabuada do número ", tabuada)

#Loop que vai de 1 até 10
for valor in range (1, 11, 1):
    
    #Concatena e imprime cada linha da tabuada
    print(str(tabuada) + " x " + str(valor) + " = " + str((tabuada*valor)))