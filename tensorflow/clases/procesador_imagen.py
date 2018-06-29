import os
from PIL import Image
import scipy.misc as smp
import numpy as np

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
        print('================================= Redimensionando imagenes =================================')
        for folder in os.listdir(self.directorio+'/'):
            print('Leyendo '+folder+'...')
            contador = 0
            for archivo in os.listdir(self.directorio+'/'+folder):
                imagen = Image.open(self.directorio+'/'+folder+'/'+archivo)
                out = imagen.resize((80, 80))
                out.save(self.directorio+'/'+folder+'/'+folder+'-'+str(contador)+'.png')
                contador = contador + 1
            print(folder+' Completado \n')

    def procesarImagen(self):
        print('================================= Procesando imagenes =================================')
        data = []
        for folder in os.listdir(self.directorio+'/'):
            print('Leyendo '+folder+'...')
            for archivo in os.listdir(self.directorio+'/'+folder):
                # print('Leyendo '+archivo+'...')
                imgData = []
                img = Image.open(self.directorio+'/'+folder+'/'+archivo)
                pixeles = np.array(img.getdata())
                imgGris = list(self.escalaDeGrises(pixel) for pixel in pixeles)
                img.putdata(imgGris)
                for _pixel in imgGris:
                    imgData.append(self.getValorRGB(_pixel))
                data.append(imgData)
        data = np.array(data)
        print(data.shape)

    def escalaDeGrises(self, rgb):
        valor = int((rgb[0]+rgb[1]+rgb[2])/3)
        return (valor, valor, valor)

    def getValorRGB(self, rgb):
        valor = int(abs(((rgb[0]+rgb[1]+rgb[2])/765 - 1)))
        return valor