import os
from PIL import Image

class ProcesadorImagen:
    directorio = ''
    renombrar = False
    redimensionar = False

    def __init__(self, directorio, renombrar, redimensionar):
        self.directorio = directorio
        self.renombrar = renombrar
        self.redimensionar = redimensionar
        if(self.renombrar):
            self.renombrarImagenes()
        if(self.redimensionar):
            self.redimensionarImagenes()

    def renombrarImagenes(self):
        print('================================= Renombrando imagenes ================================= \n')
        for folder in os.listdir(self.directorio):
            print('Leyendo '+folder+'...')
            contador = 0
            for archivo in os.listdir(self.directorio+'/'+folder):
                os.rename(self.directorio+'/'+folder+'/'+archivo, self.directorio+'/'+folder+'/'+folder+'-'+str(contador)+'.png')
                contador = contador + 1
            print(folder+' Completado \n')

    def redimensionarImagenes(self):
        print('=================================Redimensionando imagenes=================================')
        for folder in os.listdir(self.directorio+'/'):
            print('Leyendo '+folder+'...')
            contador = 0
            for archivo in os.listdir(self.directorio+'/'+folder):
                imagen = Image.open(self.directorio+'/'+folder+'/'+archivo)
                out = imagen.resize((80, 80))
                out.save(self.directorio+'/'+folder+'/'+folder+'-'+str(contador)+'.png')
                contador = contador + 1
            print(folder+' Completado \n')