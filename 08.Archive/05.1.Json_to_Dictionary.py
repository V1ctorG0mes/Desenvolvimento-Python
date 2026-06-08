#importando o módulo json
import json

#usando a função open para criar um objeto do tipo arquivo
arquivo = open("C:\\arquivos\\agenda.json", "r", encoding="UTF-8")

#colocando o conteúdo do arquivo em uma variável do tipo string
print(type(json.loads(arquivo.read()))) #json.loads gera um dicionario

#fechando o arquivo
arquivo.close()

#usando o método loads para converter uma string no formato json em um dicionário

#comprovando que o objeto agenda é do tipo dicionário