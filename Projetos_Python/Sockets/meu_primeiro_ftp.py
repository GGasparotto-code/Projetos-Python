#Importa o módulo ftplib
from ftplib import *

#Cria uma nova instância da classe FTP e se conecta ao servidor FTP especificado
ftp = FTP('ftp.ibiblio.org')

#Imprime a mensagem de boas-vindas do servidor FTP
print(ftp.getwelcome())

#Encerra a sessão FTP
ftp.quit()
