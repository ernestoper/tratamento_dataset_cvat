import os
import shutil
from PIL import Image
HOME = os.getcwd()
#nome do dataset com pastas de videos
name_dataset = "/home/ernesto/Downloads/novos-intelbras/rodada-5"
dir_path = name_dataset+"/"
dir_path_gray = name_dataset+"-gray/"
print(dir_path_gray)
path_gray_todo = os.path.join(HOME,dir_path_gray) 
os.makedirs(path_gray_todo , exist_ok=True)

for (dirpath, dirnames, filenames) in os.walk(dir_path): # obtendo caminho atual, diretorios e ficheiros respetivamente
    #print(dirnames)
    for dir  in dirnames:
            print(dir)
            #DIRECTORY_GRAY = dir_path+dir+'-gray' #cria novas pastas para as imagens gray
            DIRECTORY_GRAY = path_gray_todo+dir#+'-gray' #cria novas pastas para as imagens gray

            path_GRAY = os.path.join(HOME,DIRECTORY_GRAY) 
            os.makedirs(path_GRAY, exist_ok=True) #cria as pastas gray no directorio atual
            dir_pat = dir_path +dir
            #print(dir_pat)
            for file in os.listdir(dir_pat): # percorrer ficheiros em cada diretorio (dirpath)
                #print(file)
                if file.endswith('.PNG') :
                        #print(file)
                        basename_txt = os.path.basename(file)
                        print(basename_txt)
                        file_name = os.path.splitext(basename_txt)[0]
                        #print(file_name)
                        file_name_txt=file_name+'.txt' #para chamare o mesmo nome do png 
                        src_path = os.path.join(dir_pat, file)
                        
                        #dst_path = os.path.join(path, file)
                        GRAY_path = os.path.join(path_GRAY, file)
                        img = Image.open(src_path).convert('L')
                        #print(img)
                        img.save(GRAY_path)# salva a imagem no novo directoreio gray
                        src_path_txt = os.path.join(dir_pat, file_name_txt)
                        dst_path = os.path.join(path_GRAY, file_name_txt)
                        shutil.copyfile(src_path_txt, dst_path)


