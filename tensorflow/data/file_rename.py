import os

for folder in os.listdir('train/'):
    print("Leyendo "+folder)
    file_counter = 0
    for file in os.listdir('train/'+folder):
        os.rename('train/'+folder+'/'+file, 'train/'+folder+'/'+folder+'-'+str(file_counter)+'.png')
        file_counter = file_counter + 1
    print(folder+" Completado")