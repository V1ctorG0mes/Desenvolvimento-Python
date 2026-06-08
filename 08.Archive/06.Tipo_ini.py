import configparser
import os 

config = configparser.ConfigParser() #config tem a capacidade de um ConfigParser
config_file = "c:\\arquivos\\config.ini"

if not os.path.exists(config_file):
    raise FileNotFoundError(f"The configuration file {config_file} does not exist")

#Lê o arquivo de configuração
config.read(config_file)

#Exibindo o c tipo do objeto config
print(type(config))

#acesando as configurações
print(config["general"]["app_name"])

#Exibindo todas as config.sections e as config.items(section) com loop
for secao in config.sections():
    print(secao)
    for chave, valor in config.items(secao):
        print(f"{chave} - {valor}")