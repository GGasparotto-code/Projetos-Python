#Solicitando ao usuário que digite as informações necessárias
nome = input("Digite seu nome: ")
email = input("Digite seu e-mail: ")
idade = int(input("Digite sua idade: "))
empresa = input("Digite a instituição: ")
altura = float(input("Digite sua altura (em metros): "))

#Imprimindo informações sobre o usuário e o tipo das váriaveis utilizadas
print(nome + " trabalha na empresa " + empresa)
print("E-mail cadastrado: " + email)
print("Tem: " + str(idade) + "anos de idade e possui" + str(altura) + "de altura")
print("==============Verifique os tipos de dados abaixo:==============")
print("O tipo de dado da variável [nome] é: ", type(nome))
print("O tipo de dado da variável [empresa] é: ", type(empresa))
print("O tipo de dado da variável [email] é: ", type(email))
print("O tipo de dado da variável [idade] é: ", type(idade))
print("O tipo de dado da variável [altura] é: ", type(altura))
