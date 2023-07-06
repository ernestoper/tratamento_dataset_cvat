""" Este codigo retira a label com coordenadas que não serão usadas
    exemplo para um arquivo txt qualquer com dados:

    14 0.170313 0.547222 0.095833 0.359259
    21 0.125260 0.825463 0.154688 0.323148
    24 0.290380 0.370463 0.091562 0.326481
    14 0.202083 0.474537 0.088542 0.376852

    neste arquivo temos 4 anotações com 3 labels diferentes
    depois de usar este codigo a saida deve ser :

    14 0.170313 0.547222 0.095833 0.359259
    14 0.202083 0.474537 0.088542 0.376852

"""

import glob
import fileinput

# Caminho para a pasta contendo os arquivos TXT

video:str   =   "153-labels"
label:str   =   "21"
video_curto:str =   "3807-5566"

caminho_pasta = "./"    +   video   +   "/"   +   label   +   "/"   +   video_curto

# Padrão para encontrar os arquivos TXT
padrao_arquivos = caminho_pasta + "/*.txt"

# Obtém a lista de arquivos na pasta com base no padrão
arquivos = glob.glob(padrao_arquivos)

# Percorre cada arquivo encontrado
for arquivo in arquivos:
    # Abre o arquivo para leitura e escrita
    with fileinput.FileInput(arquivo, inplace=True) as arquivo_input:
        # Percorre cada linha do arquivo
        for linha in arquivo_input:
            # Verifica se a linha começa com "label"
            if linha.startswith(label):
                # Imprime a linha no arquivo (sem quebra de linha)
                print(linha, end="")

