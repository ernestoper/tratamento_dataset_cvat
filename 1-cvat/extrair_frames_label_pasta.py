"""
Lembre-se de substituir "caminho/para/a/pasta_de_origem" pelo caminho real da pasta onde estão localizados os arquivos originais e "caminho/para/a/pasta_de_destino" pelo caminho onde você deseja criar a nova pasta e copiar os arquivos.

Este código criará uma nova pasta de destino (se ainda não existir) e copiará os arquivos frame_000100.txt até frame_000150.txt e frame_000100.PNG até frame_000150.PNG da pasta de origem para a pasta de destino. Certifique-se de ajustar o número inicial e final de acordo com sua necessidade.
"""

import os
import shutil

# dados do video contendo os frames

video:str   =   "282"
label:str   =   "23" #valor muda com variação da label
video_curto:str =   "4296-4414" #valor muda, intervalo de frames

# Pasta de origem dos arquivos
pasta_origem = "./"+video

# Pasta de destino para os arquivos copiados
pasta_destino = "./"+video+"-labels"+"/"+label+"/"+video_curto
print(pasta_destino)
# Criar a nova pasta de destino
if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)

# Número inicial e final dos arquivos que deseja extrair
frame_inicial:int = 4296
frame_final:int = 4414

# Percorrer os números dos arquivos que deseja extrair
for numero in range(frame_inicial, frame_final + 1):
    # Nome do arquivo .txt
    nome_arquivo_txt = "frame_{:06d}.txt".format(numero)
    
    caminho_arquivo_txt = os.path.join(pasta_origem, nome_arquivo_txt)
    # se o arquivo existe :
    nome_arquivo_txt_total = pasta_origem   +   "/" + nome_arquivo_txt
    #print(nome_arquivo_txt_total)
    # se o arquivo existe fazer:
    if os.path.exists(nome_arquivo_txt_total):
        # Nome do arquivo .PNG
        print("extraindo o arquivo:")
        print(caminho_arquivo_txt)
        nome_arquivo_png = "frame_{:06d}.PNG".format(numero)
        caminho_arquivo_png = os.path.join(pasta_origem, nome_arquivo_png)
        #print("extraindo o arquivo:")
        print(caminho_arquivo_png)
        # Copiar o arquivo .txt para a pasta de destino
        caminho_destino_txt = os.path.join(pasta_destino, nome_arquivo_txt)
        shutil.copy(caminho_arquivo_txt, caminho_destino_txt)

        # Copiar o arquivo .PNG para a pasta de destino
        caminho_destino_png = os.path.join(pasta_destino, nome_arquivo_png)
        shutil.copy(caminho_arquivo_png, caminho_destino_png)
    # se não existe procura outro:
    else:
        continue
