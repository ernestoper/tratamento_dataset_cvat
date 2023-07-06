import os
"""
retira todas as anotações diferentes da label anotada (numero de pasta)
    exemplo uma pasta 286-labels (um video dividio em curtos para cada label)
    
    286-labels
        -1
          -varias pastas de curtos com anotações da label 1
        
        -.
        -.
        -.
        -24 
           -varias pastas de curtos com anotações da label 24
        
          
    
     para um arquivo txt qualquer com dados:

    14 0.170313 0.547222 0.095833 0.359259
    21 0.125260 0.825463 0.154688 0.323148
    24 0.290380 0.370463 0.091562 0.326481
    14 0.202083 0.474537 0.088542 0.376852

    neste arquivo temos 4 anotações com 3 labels diferentes
    depois de usar este codigo a saida deve ser :

    14 0.170313 0.547222 0.095833 0.359259
    14 0.202083 0.474537 0.088542 0.376852

"""

# Função para processar um arquivo
def processar_arquivo(caminho_arquivo,label):
    linhas_novas = []
    with open(caminho_arquivo, 'r') as arquivo:
        for linha in arquivo:
            if linha.startswith(label):
                print(" Existe a label " + label)
                linhas_novas.append(linha)
    
    # Reescreve o arquivo apenas com as linhas que começam com '10'
    with open(caminho_arquivo, 'w') as arquivo:
        arquivo.writelines(linhas_novas)
        print(linhas_novas)

# Função para percorrer as pastas e arquivos
def percorrer_pastas(caminho_pasta,label):
    for diretorio, _, arquivos in os.walk(caminho_pasta):
        print(diretorio)
        for arquivo in arquivos:
            if arquivo.endswith('.txt'):
                print(arquivo)
                caminho_arquivo = os.path.join(diretorio, arquivo)
                processar_arquivo(caminho_arquivo,label)



# Caminho para a pasta contendo os arquivos TXT

video:str   =   "282-labels" #pasta onde encontra-se os curtos dividos em cada label
label:str   =   "23" #label 

pasta_raiz = "./"    +   video   +   "/"   +   label   +   "/" 
#caminho_pasta_principal = "caminho/da/pasta/principal"
# Chama a função para percorrer as pastas e arquivos
percorrer_pastas(pasta_raiz,label)
