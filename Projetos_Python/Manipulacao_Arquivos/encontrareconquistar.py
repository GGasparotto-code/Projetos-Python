#Encontrando caracter específico
texto = "Majora"

print(texto.find("o"))

#Dividindo uma String
game = "Legend of Zelda: Majora's Mask"

print(game.split(" "))

#Encontra o índice da segunda ocorrência do caractere "a" na string
fairy = "Tatl e Tael"

print(fairy[fairy.find("a")+1:].find("a"))
