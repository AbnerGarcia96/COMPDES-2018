import os
from PIL import Image

mainfolder = 'test'

for folder in os.listdir(mainfolder+'/'):
    print("Leyendo "+folder)
    contador = 0
    for file in os.listdir(mainfolder+'/'+folder):
        imagen = Image.open(mainfolder+'/'+folder+'/'+file)
        out = imagen.resize((80, 80))
        out.save(mainfolder+'/'+folder+'/'+folder+'-'+str(contador)+'.png')
        contador = contador + 1
    print(folder+" Completado")