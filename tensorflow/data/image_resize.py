import os
from PIL import Image

for folder in os.listdir('test/'):
    print("Leyendo "+folder)
    file_counter = 0
    for file in os.listdir('test/'+folder):
        #resize
        image = Image.open('test/'+folder+'/'+file)
        out = image.resize((80, 80))
        out.save('test/'+folder+'/'+folder+'-'+str(file_counter)+'.png')
        file_counter = file_counter + 1

    print(folder+" Completado")