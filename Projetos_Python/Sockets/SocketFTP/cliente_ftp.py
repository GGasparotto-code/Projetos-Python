#Importa a biblioteca ftplib que permite a conexão e interação com servidores FTP
from ftplib import *

#Cria uma nova instância da classe FTP para o servidor 'ftp.ibiblio.org'
ftp = FTP('ftp.ibiblio.org')

#Imprime a mensagem de boas-vindas do servidor FTP
print(ftp.getwelcome())

#Solicita ao usuário que digite o nome de usuário para autenticação no servidor FTP
usuario = input("Digite o usuário: ")

#Solicita ao usuário que digite a senha para autenticação no servidor FTP
senha = input("Digite a senha: ")

#Realiza login no servidor FTP usando o nome de usuário e senha fornecidos
ftp.login(usuario, senha)

#Imprime o diretório atual de trabalho no servidor FTP
print("Diretório atual de trabalho: ", ftp.pwd())

#Muda para o diretório 'pub' no servidor FTP
ftp.cwd('pub')

#Imprime o diretório atual após a mudança
print("Diretório corrente: ", ftp.pwd())

#Lista todos os arquivos e diretórios no diretório atual
print(ftp.retrlines('LIST'))

#Encerra a sessão com o servidor FTP
ftp.quit()
