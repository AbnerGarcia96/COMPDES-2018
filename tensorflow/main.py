import sys
from clases.procesador_imagen import ProcesadorImagen

def main():
    if(len(sys.argv) == 2):
        directorio = sys.argv[1]
        img = ProcesadorImagen(directorio, False, False)
        img.procesarImagen()
    else:
        print("Faltan argumentos: python3 main.py [directorio]")
    

if __name__ == "__main__":
    main()