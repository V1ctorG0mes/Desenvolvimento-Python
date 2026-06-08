#usando a função open para criar um objeto do tipo arquivo
arquivo = open("C:\\arquivos\\arquivo.txt", "r", encoding="UTF-8")

#verificando o tipo do objeto arquivo
print(type(arquivo))

#printando o objeto arquivo
print(arquivo)

#printando o conteúdo do objeto arquivo
print(arquivo.read())

#fechando o arquivo
arquivo.close()