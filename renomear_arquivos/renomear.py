import os
import shutil
HOME = os.getcwd()
#print("HOME:", HOME)
root_dir = "data-gray-curtos/1/train-gray"
DIRECTORY = "imagens"
#nome_pasta = 'obj_train_data'
DIRECTORY_Labels = "labels"
path = os.path.join(HOME,DIRECTORY) 
#print(path)
path_l = os.path.join(HOME,DIRECTORY_Labels) 
os.makedirs(path, exist_ok=True) 
os.makedirs(path_l, exist_ok=True) 
# Função para percorrer as pastas, renomear e copiar os arquivos
# def renomear_e_copiar_arquivos(root_dir):
imagem_count = 0
label_count =0
for root, dirs, files in os.walk(root_dir):
    #print(dirs)
    for dir in dirs:
        print(dir)
        for file in dir:
            print(file)
            basename = os.path.basename(file)
            file_name = os.path.splitext(basename)[0]
            print(file_name)
            #print(HOME+'/'+root_dir+file_name+'.PNG')
            isExist=os.path.exists(root_dir+file_name+'.PNG')
            #print(isExist)
            if file.endswith('.PNG'):
                src_path = os.path.join(root, file)
                dst_filename = f"frame{imagem_count}.PNG"
                dst_path = os.path.join(path, dst_filename)
                shutil.copyfile(src_path, dst_path)
                imagem_count+=1
            elif file.endswith('.txt'):
                src_path = os.path.join(root, file)
                dst_filename = f"frame{imagem_count}.txt"
                dst_path = os.path.join(path_l, dst_filename)
                shutil.copyfile(src_path, dst_path)
                label_count += 1

