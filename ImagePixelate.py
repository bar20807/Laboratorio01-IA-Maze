from PIL import Image
import numpy as np
from BFS import *
from colorsys import *
class ImagePixelate(object):
    def __init__(self):
        self.input_file = self.input_file
        self.file_name = self.file_name
        self.size = self.size
        self.matriz_laberinto = []
    def pixelate(input_file, file_name, size):
        image = Image.open(input_file)
        image = image.resize(
            (image.size[0] // size, image.size[1] // size),
            Image.NEAREST
        )
        image = image.convert("RGB")
        data_pixel= image.getdata()
        new_image = []
        for item in data_pixel:

            if item[0] in list(range(200, 256)) and item[1] in list(range(200, 256)) and item[2] in list(range(200, 256)):
                new_image.append((255, 255, 255))
            elif item[0] in list(range(0, 201)) and item[1] in list(range(0, 201)) and item[2] in list(range(0, 201)):
                new_image.append((0, 0, 0))
            else:
                new_image.append(item)

        image.putdata(new_image)

        image = image.resize(
            (image.size[0] * size, image.size[1] * size),
            Image.NEAREST
        )

        image.save(file_name)

    #Función que convertirá el archivo bmp a un array
    def bmp_to_array(input_file, size):
        #Declaramos el array que almacenará el bmp 
        bmp_array = []
        #Abrimos la imagen
        im = Image.open(input_file)
        #Obtenemos los datos de la imagen
        width = im.width
        height = im.height
        #Se recorre cada pixel en los datos obtenidos en el paso anterior y los compara con los valores específicos de R, G y B.
        for y in range(0,height,size):
            #Creamos una lista que servira cómo fila para la matriz
            fila = []
            for x in range(0,width,size):
                #Obtenemos el color del pixel
                color = int.from_bytes(im.getpixel((x,y)), byteorder='big')
                #Comparamos el color con los valores de R, G y B
                if color == 16777215:
                    fila.append(1)
                elif color == 0:
                    fila.append(0)
                elif color < 1000000:
                    fila.append(2)
                #Detectamos si el color es solamente rojo
                else:
                    fila.append(3)
                print("Obteniendo el pixel: " + str(im.getpixel((x,y))))
            #Agregamos la fila a la matriz
            bmp_array.append(fila)
        #Retornamos el ancho, alto y el array realizado
        return width, height, bmp_array[::-1]
    
                
    #Función que convertirá la matriz a un archivo bmp
    def array_to_bmp(width, height, bmp_array, file_name):
        #Declaramos el array que almacenará el bmp
        new_data = []
        #Calculamos el pixel ratio
        pixel_ratio = width/len(bmp_array)
        #Tamaño del array
        bmp_array_len = len(bmp_array)
        #Se recorre cada pixel en los datos obtenidos en el paso anterior y los compara con los valores específicos de R, G y B.
        for i in range(height):
            for j in range(width):
                #Obtenemos el valor del pixel
                pixel = bmp_array[int(i/pixel_ratio)][int(j/pixel_ratio)]
                #Comparamos el valor del pixel con los valores de R, G y B
                if pixel == 1:
                    new_data.append((255,255,255))
                elif pixel == 0:
                    new_data.append((0,0,0))
                elif pixel == 2:
                    new_data.append((0,255,0))
                elif pixel == 3:
                    new_data.append((255,0,0))
                elif pixel == 6:
                    new_data.append((0,0,205))
                elif pixel == 7:
                    new_data.append((150,70,205))
        #Se crea una nueva imagen con los datos obtenidos en el paso anterior.
        new_image = Image.new("RGB", (width, height))
        new_image.putdata(new_data)
        new_image.save(file_name)

            

        
        