#Solicita ao usuário que insira um número inteiro
numero = int(input("Digite um número: "))

#Entrando em um loop que continuará a contagem enquanto o número for menor que 101
while numero < 101:

    #Imprime o número atual
    print("\t" + str(numero))

    #Aumenta o número em 1
    numero = numero + 1

#Imprime uma mensagem avisando quando o laço foi finalizado
print("Laço encerrado....")