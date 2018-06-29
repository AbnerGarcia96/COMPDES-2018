import os
from PIL import Image

for folder in os.listdir('train/'):
    print("Leyendo "+folder)
    file_counter = 0
    for file in os.listdir('train/'+folder):
        #resize
        image = Image.open('train/'+folder+'/'+file)
        out = image.resize((80, 80))
        out.save('train/'+folder+'/'+folder+'-'+str(file_counter)+'.png')
        file_counter = file_counter + 1

    print(folder+" Completado")