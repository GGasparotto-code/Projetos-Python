#Importa todas as funções do módulo IdentificacaoDeFuncoes
from IdentificacaoDeFuncoes import *

#Cria uma lista vazia para armazenar o inventário
minhaLista = []

# Chamada da função preeencherInventario para adicionar 
#itens à minhaLista e impressão do progresso
print("Preenchendo")
preeencherInventario(minhaLista)
print("Exibindo")
exibirInventario(minhaLista)

# Chamada da função localizaPorNome pesquisar 
#itens na minhaLista e impressão do progresso
print("Pesquisando")
localizaPorNome(minhaLista)
print("Alterando")
depreciarPorNome(minhaLista, 20)

#Chamada da função excluirPorSerial para remover 
#um item específico da minhaLista
print("Excluindo")
print(excluirPorSerial(minhaLista))
exibirInventario(minhaLista)

#Chamada da função resumirValores para calcular 
#e exibir o valor total dos itens na minhaLista
print("Resumindo")
resumirValores(minhaLista)
