def ler (nome_arquivo):
    arquivo = open (nome_arquivo, 'r') #abre aruivo de texto no mesmo diretório    
    for linha in arquivo: #para cada linha do arquivi imprima o nome
        print (linha)
    arquivo.close() #fecha o arquivo na memóri da maquina
#informar o nome do arquivo para complementar a função, diretamente no terminal do mac
