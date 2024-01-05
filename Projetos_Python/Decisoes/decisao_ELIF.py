#Solicita ao usuário para inserir sua idade
idade = int(input("Digite sua idade: "))

#Classifica a pessoa com base na idade inserida
if idade < 13:
    print("Criança") #Imprime "Criança" se a idade for menor que 13
elif idade < 18:
    print("Adolescente") #Imprime "Adolescente" se a idade for maior ou igual a 13 e menor que 18
elif idade < 60:
    print("Adulto") #Imprime "Adulto" se a idade for maior ou igual a 18 e menor que 60
else:
    print("Idoso") #Imprime "Idoso" se a idade for maior ou igual a 60