from Framework import Framework
#Función que obtiene las coordenadas de inicio
def getCoordinatesS(array):
    countRS = 0
    countCS = 0

    for row in array:
        countCS = 0
        for element in row:
            if element == 3:
                return (countRS, countCS)
            countCS += 1   
        countRS += 1  
            
    return "Sin coincidencias"
#Función que obtiene las coordenadas de fin
def getCoordinatesE(array):
    countRE = 0
    countCE = 0
    Results = []
    
    for row in array:
        countCE = 0
        for element in row:
            if element == 2:
                Results.append((countRE, countCE))
            countCE += 1     
        countRE += 1
    
    if (len(Results) != 0):
        return Results 
    else:
        return "Sin coincidencias"
class DFS(Framework):
    def __init__(self,maze):
        self.maze = maze
        self.height = len(self.maze)
        self.width = len(self.maze[0])
        self.start = getCoordinatesS(maze)
        self.finish = getCoordinatesE(maze)
        self.path = []
        self.pixels = []
        self.visited = []
        self.line_manhattan = []
        self.objetive = False
        #Se llama a acciones
        self.actions()
    
    #Función que se encarga de realizar las acciones desde el punto en el que se encuentra con el algoritmo de búsqueda
    def actions(self):
        #Declaramos el punto de inicio de nuestra linea
        self.line_manhattan.append(self.start)
        
        #Se analiza que, mientras nuestra línea analizada tenga elementos, esta obtendrá el pixel actual
        while len(self.line_manhattan) > 0:
            #Se obtiene el pixel actual
            self.pixel = self.line_manhattan.pop()
            #Se agrega a la lista de pixeles visitados
            self.path.append(self.pixel)
            #Se analiza si el pixel actual es igual al pixel objetivo
            if self.pixel == self.finish:
                #Si es así, se termina el ciclo
                self.objetive = True
                break
            #Se analiza si el pixel actual no se encuentra en la lista de pixeles visitados
            if self.pixel not in self.pixels:
                #Si es así, se agrega a la lista de pixeles
                self.pixels.append(self.pixel)
                #Se llama a la función de búsqueda
                self.search(self.pixel)
        
 
    #Función que se encarga de devolver el costo del camino
    def pathCost(self):
        pass
    #Función que se encarga de devolver el costo del paso
    def stepCost(self):
        pass
    #Función que se encarga de evaluar si el punto actual es el objetivo
    def goalTest(self):
        if self.pixel in self.finish:
            self.objetive = True
            return True
        else:
            return False
    #Función que se encarga de devolver los resultados
    def results(self):
        pass
    #Función que se encarga de realizar la búsqueda con el algoritmo de DFS
    def search(self, state):
        #Se coloca el algoritmo de busqueda dfs
        acual_x = state[0]
        actual_y = state[1]
        #Comparamos si el punto en cada uno de sus 4 puntos no se encuentra en el camino resultante 
        #y si no es un muro
        if self.maze[actual_y - 1][acual_x] != 1 and (acual_x, actual_y - 1) not in self.path:
            self.pixels.append((acual_x, actual_y - 1))
            self.line_manhattan.append((acual_x, actual_y-1))
        if self.maze[actual_y + 1][acual_x] != 1 and (acual_x, actual_y + 1) not in self.path:
            self.pixels.append((acual_x, actual_y + 1))
            self.line_manhattan.append((acual_x, actual_y+1))
        if self.maze[actual_y][acual_x - 1] != 1 and (acual_x - 1, actual_y) not in self.path:
            self.pixels.append((acual_x - 1, actual_y))
            self.line_manhattan.append((acual_x-1, actual_y))
        if self.maze[actual_y][acual_x + 1] != 1 and (acual_x + 1, actual_y) not in self.path:
            self.pixels.append((acual_x + 1, actual_y))
            self.line_manhattan.append((acual_x+1, actual_y))
        
