#Importa a biblioteca time para controlar o tempo de execução do programa
import time

#Imprime uma mensagem na tela sobre o lançamento de um foguete
print("Lançamento de foguete em:")

#Inicializa uma variável de contagem com o valor 10
contagem = 10

#Loop que mantém a contagem enquanto o número for maior que 0
while contagem > 0:

   #Imprime o valor atual da contagem
   print(contagem) 

   #Pausa o programa por 1 segundo
   time.sleep(1) 

   #Diminui o valor da contagem
   contagem -= 1 

#Quando a contagem chega a 0, imprime uma mensagem indicando que o foguete foi lançado
print("Foguete lançado!")