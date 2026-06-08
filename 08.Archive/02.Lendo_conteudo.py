#usando a função open para criar um objeto do tipo arquivo
arquivo = open("C:\\arquivos\\arquivo.txt", "r", encoding="UTF-8")

#printando o conteúdo do objeto arquivo
#print(arquivo.read())

#printando uma linha do arquivo
#print(arquivo.readline())

#printando outra linha do arquivo
#print(arquivo.readline())

#Passando o conteúdo do arquivo para uma lista
lista_linhas = arquivo.readlines() #retorna o conteudo em formato de uma lista

#comprovando o tipo do objeto linhas_do_arquivo
print(type(lista_linhas))
print(lista_linhas)
#colocando a lista em ordem alfabética
lista_linhas.sort()
print(lista_linhas)

#Exibindo uma linha por vez, utilizando o loop for e o método readlines()
for linha in lista_linhas:
    print(linha)

#fechando o arquivo
arquivo.close()