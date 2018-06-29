import os

for folder in os.listdir('test/'):
    print("Leyendo "+folder)
    file_counter = 0
    for file in os.listdir('test/'+folder):
        os.rename('test/'+folder+'/'+file, 'test/'+folder+'/'+folder+'-'+str(file_counter)+'.png')
        file_counter = file_counter + 1
    print(folder+" Completado")