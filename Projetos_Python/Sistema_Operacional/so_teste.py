#Importando os módulos necessários
import platform
import getpass
from datetime import datetime

#Imprimindo a data e hora atual
print("Data/Hora:.............", datetime.now())

#Obtendo o nome do usuário atual
print("Usuário:...............", getpass.getuser())

#Usando o módulo 'platform' para obter informações sobre a máquina e o sistema operacional
print("Nome máquina:..........", platform.node())
print("Arquitetura:...........", platform.architecture())
print("Sistema Operacional:...", platform.system())
print("Versão do SO:..........", platform.release())
print("Processador:...........", platform.processor())
print("Versão do Python:......", platform.python_version())
