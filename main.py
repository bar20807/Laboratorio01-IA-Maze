"""
    Nombre: José Rodrigo Barrera García
    Universidad del Valle de Guatemala
    Laboratorio 1 - Inteligencia Artificial
    Maze resolve using IA

"""
import ImagePixelate
from BFS import *
from PIL import Image
from DFS import *

#Función que lee la imagen del maze con algoritmo BFS
def readImageBFS(ima):
    #Se llama al método pixelate para que se realice la pixelación de la imagen.
    ImagePixelate.ImagePixelate.pixelate(ima, "PixelLab.bmp", 20)
    #Se llama al método bmp_to_array para que se realice la conversión de la imagen a un array.
    width, height, bmp_array = ImagePixelate.ImagePixelate.bmp_to_array("./PixelLab.bmp", 20)
    print("bmp_array: " + str(bmp_array))
    print(width)
    print(height)
    #Se crea un objeto de la clase BFS y se le pasa el array de la imagen.
    bfs = BFS(bmp_array)
    #Se realiza la pixelación 
    vet = bfs.search()
    for s in vet[:-2]:
        i,j = s
        bmp_array[i][j] = 7
    #Se llama al método search_shortest_path para que se realice la búsqueda del camino más corto.
    road = bfs.shortestPath()
    
    print("Esto es road: " + str(road))
    algoritmo = 1
    for p in road[:-2]: 
        i,j = p
        if algoritmo == 1:
            bmp_array[i][j] = 6
        else:
            bmp_array[i][j] = 6
    #Se llama al método array_to_bmp para que se realice la conversión del array a una imagen.
    ImagePixelate.ImagePixelate.array_to_bmp(width, height, bmp_array, "ResultadoBFS.bmp")

def readImageDFS(ima):
    #Se llama al método pixelate para que se realice la pixelación de la imagen.
    ImagePixelate.ImagePixelate.pixelate(ima, "PixelLabDFS.bmp", 20)
    #Se llama al método bmp_to_array para que se realice la conversión de la imagen a un array.
    width, height, bmp_array = ImagePixelate.ImagePixelate.bmp_to_array("./PixelLabDFS.bmp", 20)
    print("bmp_array: " + str(bmp_array))
    print(width)
    print(height)
    #Se crea un objeto de la clase BFS y se le pasa el array de la imagen.
    dfs = DFS(bmp_array)
    #Se realiza la pixelación 
    #Primero del camino más corto 
    for pixel in dfs.path:
        i,j = pixel
        if pixel != dfs.start and pixel not in dfs.finish:
            bmp_array[i][j] = 6
    #Luego todo el camino
    for pixels in dfs.pixels:
        i,j = pixels
        if pixels != dfs.start and pixels not in dfs.finish:
            bmp_array[i][j] = 7
    #Se llama al método array_to_bmp para que se realice la conversión del array a una imagen.
    ImagePixelate.ImagePixelate.array_to_bmp(width, height, bmp_array, "ResultadoDFS.bmp")

#Probamos la función
#readImageBFS("./lab1.bmp")
readImageDFS('./lab1.bmp')