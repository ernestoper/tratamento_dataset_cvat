import os
import shutil

HOME = os.getcwd()
#print("HOME:", HOME)
nome_label="4"
pasta_train= "train-gray"
pasta_principal_data="data-gray-curtos"
dir_path = pasta_principal_data+"/"+nome_label+ "/"+pasta_train+"/"
#DIRECTORY = ""+"imagens"
dir_name_ssd= "/media/ernesto/ANTONIETTA/"
DIRECTORY = dir_name_ssd+ pasta_principal_data+ "/"+"/imagens" +"/train"
#DIRECTORY = "imagens"
DIRECTORY_Labels = dir_name_ssd+pasta_principal_data+ "/"+"/labels" + "/train"
path = os.path.join(HOME,DIRECTORY) 
#print(path)
path_l = os.path.join(HOME,DIRECTORY_Labels) 
os.makedirs(path, exist_ok=True) 
os.makedirs(path_l, exist_ok=True) 
imagem_count = 14587
imagem_count_txt = 0
for (dirpath, dirnames, filenames) in os.walk(dir_path): # obtendo caminho atual, diretorios e ficheiros respetivamente
    #print(dirnames)
    for dir  in dirnames:
            print(dir)
            
            dir_pat = dir_path +dir
            #print(dir_pat)
            for file in os.listdir(dir_pat): # percorrer ficheiros em cada diretorio (dirpath)
                #print(file)
                if file.endswith('.PNG') :
                        basename_txt = os.path.basename(file)
                        file_name = os.path.splitext(basename_txt)[0]
                        print(file_name)
                        file_name_txt=file_name+'.txt' #para chamare o mesmo nome do png 
                        src_path = os.path.join(dir_pat, file)
                        dst_filename = f"frame{imagem_count}.PNG"
                        dst_path = os.path.join(path, dst_filename)
                        #print(dst_path)
                        shutil.copyfile(src_path, dst_path)
                     
                        src_path_txt = os.path.join(dir_pat, file_name_txt)
                        dst_filename_txt = f"frame{imagem_count}.txt" #substituiu o txt 
                        dst_path = os.path.join(path_l, dst_filename_txt)
                        shutil.copyfile(src_path_txt, dst_path)
                        imagem_count += 1

print(imagem_count)