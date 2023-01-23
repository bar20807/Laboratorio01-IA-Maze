"""
    Laboratorio 1 - Inteligencia Artificial
    José Rodrigo Barrera García
    Resolver un laberinto
    Universidad del Valle de Guatemala
"""
# Importar las librerías necesarias
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import a_estrella
import BFS

#Creamos la función que se encargará de leer la imagen
def ReadImage(image):
    # Abrir imagen y convertirla en un array de numpy
    imagen = Image.open(image)
    return imagen

#Función que se encargará de analizar los colores de la imagen
def ImageColors(image):
    
    #Convertimos a array la imagen recibida
    imagen_array = np.array(ReadImage(image))
    #Analizamos cada uno de los colores que contiene la imagen
    red = (imagen_array[:,:,0] == 255) & (imagen_array[:,:,1] == 0) & (imagen_array[:,:,2] == 0)
    green = (imagen_array[:,:,0] == 0) & (imagen_array[:,:,1] == 255) & (imagen_array[:,:,2] == 0)
    white = (imagen_array[:,:,0] == 255) & (imagen_array[:,:,1] == 255) & (imagen_array[:,:,2] == 255)
    black = (imagen_array[:,:,0] == 0) & (imagen_array[:,:,1] == 0) & (imagen_array[:,:,2] == 0)
    #Se detecta el punto de inicio
    start = np.where(red)
    #Se detecta el punto final
    finish = list(zip(np.where(green)[0], np.where(green)[1]))
    
    #Matriz discreta del laberinto
    matrixZeros= np.zeros_like(white, dtype=int)
    matrixZeros[white] = 1
    
    return finish


                    
        
#Probando la matriz discreta
print(ImageColors("./lab1.bmp"))    


    
  
    
    




    

