import os
import numpy as np
HOME = os.getcwd()
print("HOME:", HOME)
dir_path = "/media/ernesto/ANTONIETTA/data-vita-saci-rgb/desenrosco/615/"
files = os.listdir(dir_path)
pesos=np.array([0,0])


#for (dirpath, dirnames, filenames) in os.walk(dir_path): # obtendo caminho atual, diretorios e ficheiros respetivamente
for f in os.listdir(dir_path): # percorrer ficheiros em cada diretorio (dirpath)
        basename = os.path.basename(f)
        file_name = os.path.splitext(basename)[0]
        #print(file_name)
        f_path = os.path.join(dir_path, f)
        print(f_path)
        f_size = os.path.getsize(f_path)
        f_size_kb = f_size/1024 # obter resultado em kB
        print(f_size)
        if f_size_kb==0:
            file_img=dir_path+file_name+ ".PNG"
            file_text=dir_path+file_name+ ".txt"
            
            os.remove(file_text)
            os.remove(file_img)