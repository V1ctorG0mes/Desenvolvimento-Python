#'r' abrir para leitura (modo padrão). (read)
#'w' abrir para a escrita, sobrescrevendo o conteúdo. (write)
#'x' abrir para a criação de arquivo, gerando uma falha se existir um arquivo de mesmo nome no caminho especificado.
#'a' abrindo para escrita, anexando o novo conteúdo ao final do conteúdo já existente. (append)
#'b' abrir em modo binário.
#'t' abrir em modo de texto (modo padrão).
#'+' abrir para atualização (escrita e leitura).

#criando uma variável de texto
conteudo = "Há muito tempo atrás, em uma galáxia muito, muito distante..."

#usando a função open para criar um objeto do tipo arquivo
#arquivo = open("C://arquivos//arquivo_texto.txt", "w", encoding="UTF-8")

#Escrevendo o conteúdo da variável conteudo dentro do arquivo w
#arquivo.write(conteudo)

#Abrindo aquivo e escrevendo nele
arquivo = open("C:\\arquivos\\arquivo_texto.txt", "a", encoding="UTF-8")
arquivo.write("\nTeste novo")

#fechando o arquivo
arquivo.close()