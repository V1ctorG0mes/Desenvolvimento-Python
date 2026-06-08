#importando o módulo json
import json

#criando um dicionário para usarmos como exemplo
contatos = {
    "Clark Kent": #O valor dessa chave (Clark Kent) é um dicionário
        {"Celular":"123456",
        "Email":"super@krypton.com"},
    "Bruce Wayne":
        {"Celular":"654321",
        "Email":"bat@caverna.com.br"}
}

#convertendo o dicionário para uma string o formato json
conteudo_string = json.dumps(contatos, indent=4, ensure_ascii=False) #converte objetos python em json

#criando um arquivo
arquivo = open("C:\\arquivos\\agenda.json", "w", encoding="UTF-8") #cria agenda.json
arquivo.write(conteudo_string) #escreve o conteudo do dicionario contatos aqui

#fechando arquivo
arquivo.close()