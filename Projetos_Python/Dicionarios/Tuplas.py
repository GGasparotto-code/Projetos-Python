#Cria um dicionário vazio para armazenar os usuários
usuarios = {}

#Lista já preenchida de emails
emails = ["xpto@xyz.com", "xkcd@phd.com"]

#Cria uma lista enumerada dos emails
tupla = list(enumerate(emails))

#Comando for para cada item na lista enumerada
for chave in range(0, len(tupla)):

    #Imprime o email
    print("Email: ", tupla[chave][1])

    #Solicita ao usuário que insira o nome e o nível do usuário (ex: ADM)
    usuarios[tupla[chave][1]] = [input("Digite o nome: "), input("Digite o nível: ")]

#Comando for para cada usuário no dicionário
for chave, dado in usuarios.items():
    
    #Imprime as informações do usuário
    print("Usuario.:", chave)
    print("Email...:", chave)
    print("Nome....:", dado[0])
    print("Nível...:", dado[1])