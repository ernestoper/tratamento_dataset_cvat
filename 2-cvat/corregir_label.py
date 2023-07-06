"""
Um arquivo txt com anotações do tipo:
21 0.180232 0.322435 0.084422 0.280556

vamos substituir por:

17 0.180232 0.322435 0.084422 0.280556

"""

import os

# Caminho para a pasta contendo os arquivos .txt

video:str   =   "271-labels"
label:str   =   "20" #label nova 
video_curto:str =   "5338-5408" #frames para mudar a label
label_escrita:str   =   "1" #label antiga

pasta = "./"+video+"/"+label+"/"+video_curto #pasta com os frames

# Percorrer todos os arquivos na pasta
for nome_arquivo in os.listdir(pasta):
    if nome_arquivo.endswith(".txt"):
        caminho_arquivo = os.path.join(pasta, nome_arquivo)

        # Abrir o arquivo para leitura
        with open(caminho_arquivo, "r") as arquivo:
            linhas = arquivo.readlines()

        # Abrir o arquivo para escrita
        with open(caminho_arquivo, "w") as arquivo:
            for linha in linhas:
                # Substituir a linha que começa com "21" por "17"
                if linha.startswith(label_escrita):
                    print("Substituindo label "+label_escrita+" por "+label)
                    #linha = label + linha[2:] 
                    #adicionar espaço se for de 1 para 20, 1 digito para 2 digitos:
                    linha = label +" "+ linha[2:]
                # Escrever a linha no arquivo
                arquivo.write(linha)
