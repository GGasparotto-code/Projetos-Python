#Solicita que o usuário insira um nome
nome = input("Digite o nome: ")

#Solicita que o usuário insira a idade
idade = int(input("Digite a idade: "))

#Condição que verifica se a idade é maior ou igual a 65
if idade >= 65:

    #Se a idade for maior ou igual a 65, imprime uma mensagem indicando que o usuário possui atendimento prioritário
    print("O paciente " + nome + " POSSUI atendimento prioritário!")
else:
    #Se a idade for menor que 65, imprime uma mensagem indicando que o usuário NÃO possui atendimento prioritário
    print("O paciente " + nome + " NÃO POSSUI atendimento prioritário!")