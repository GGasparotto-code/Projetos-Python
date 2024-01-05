# Declaração inicial da lista vazia 'usuarios'
usuarios = []

# Declaração inicial da lista vazia 'usuarios' a partir de chaves. Cada chave possui uma lista associada com informações dos usuários.
usuarios = {"sonic" : ["Sonic the Hedgehog", "09/12/2017", "Green Hill"],
            "tails" : ["Miles Tails Prower", "20/12/2017", "Emerald Hill"]
            }

# Adiciona uma nova chave ao dicionário 'usuarios' com a respectiva lista de informações do usuário
usuarios["knuckles"] = ["Knuckles the Echidna", "24/12/2017", "Angel Island"]

# Imprime o dicionário 'usuarios' atualizado no console
print(usuarios)

# Imprime uma string de separação no console
print("####----####")

# Utiliza o método 'get' para buscar uma chave específica no dicionário 'usuarios' e imprimir as informações associadas a esta chave no console
print(usuarios.get("tails"))