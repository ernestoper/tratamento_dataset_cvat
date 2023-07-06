
import cv2
import os

def getnewfilename(filename):
    testfile = filename
    i = 0
    while os.path.exists(testfile+".mp4"):
        i += 1
        testfile = "%s_%s" % (testfile, i) 
        if i>1:
            testfile = "%s_%s" % (filename, i) 
        
    return testfile

label=[
'limpeza_lona_carregadora',
'descarte_biscoitos',
'limpeza_gaveta',
'retirada_bobina',
'reposicao_bobina',
'filme_partindo_desalinhando',
'potenciometro_regulagem',
'organizacao_embalagens_unitarias',
'analize_mezanino',
'troca_teflon',
'umedecimento_correias_mageadoras',
'troca_correias_mageadoras',
'alinhamento_correias_mageadoras',
'ajuste_posicao_bags',
'interacao_mesa',
'ihm_bosch_vertical',
'ihm_mezanino',
'ihm_pak_mak',
'limpeza_piso',
'limpeza_caixa',
'desenrosco_biscoito',
'idle',
'encaixotamento',
'despejo_bandeja',
'limpeza_bag_vazio',
'ajuste_bobina',
'retirada_embalagens_unitarias',
'limpeza_pistola',
'limpeza_alcool',
'limpeza_mordente'
]
if __name__ == '__main__': 

    label_unit=label[3]
    
    video_name='video2000'
    cap = cv2.VideoCapture(video_name+".mp4")
    fps = cap.get(cv2.CAP_PROP_FPS)
    #print(fps)
    #print((cap.shape))
    start_frame = 11*fps# segundos*fps
    end_frame = 13*fps#segundos*fps
    image_lst = []
    i = 0
    #cap=cv2.VideoCapture('vid.mp4')
    while True:
        ret, frame = cap.read()
        if ret == False:
            break
        # Rotate frame 
        frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
        # Rezise frame
        
        height, width, layers = frame.shape
        size = (width,height)

        if (i>=start_frame and i<=end_frame):
            #frame_rgb = cv2.cvtColor(frame)
            image_lst.append(frame)
    
            cv2.imshow('output', frame)
            key = cv2.waitKey(1)
            if key == ord('q'):
                break

        i +=1
    HOME = os.getcwd()
    #print("HOME:", HOME)
    DIRECTORY = label_unit
    path = os.path.join(HOME,DIRECTORY) 
    os.makedirs(path, exist_ok=True) # cria DIRECTORIO, se o directorio existir não sera criado
    os.chdir(path) # ACCESA AO DIRECTORIO PARA SALVAR O CURTO
    #print(path)

    video_name_new = getnewfilename(video_name) # da o nome do video
   
    print(video_name_new)
    out = cv2.VideoWriter(video_name_new+'.mp4',cv2.VideoWriter_fourcc(*'m', 'p', '4', 'v'), fps , size)
    
    for i in range(len(image_lst)):
        out.write(image_lst[i])
    out.release()