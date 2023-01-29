from Framework import Framework
#Método para obtener coordenadas del inicio
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

#Método para obtener coordenadas del final/finales
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

# Clase principal del algoritmo BFS que implementa el framework problem
class BFS(Framework):
    def __init__(self, matrix):
        self.matrix = matrix
        self.height = len(self.matrix)
        self.width = len(self.matrix[0])
        self.start = getCoordinatesS(matrix)        
        self.finish = getCoordinatesE(matrix)   
        # Frontier = Lista de fronteras
        self.frontier = [self.start] 
        # Visited = Puntos visitados
        self.visited = []  
        # Path = Camino final
        self.path = []
        
        # Se llama al algoritmo principal
        self.search()
    
    # Se determina si el estado actual es una pared o una parte "accesible"
    def actions(self, state):
        if self.matrix[state[0]][state[1]] == 0:
            return "wall"
        else:
            return "path"
    
    # Dependiendo de la acción se modifican las listas que almacenan los puntos visitados, fronteras, etc
    def results(self, action, state=None):
        if action == "add":
            if state not in self.visited:
                self.visited.append(state)
                self.frontier.append(state)
        if action == 'upd':
            if state not in self.visited:
                self.visited.append(state)
                self.frontier.append(state)
                self.backtracing[state] = self.actualState
        if action == 'back':
            self.path.append(state)
            self.actualState = self.backtracing[state]

    # Se verifica si se llegó a la meta
    def goalTest(self, state):
        return state in self.finish
    
    # No se utiliza debido a que el costo es uniforme 
    def stepCost(self):
        pass
    
    def pathCost(self, states):
        #No se toma en cuenta el inicio
        states.pop(0)
        return len(states)
    
    # Se verifica si todavía hay elementos en la frontera
    def frontier_is_Empty(self):
        return True if (len(self.frontier) == 0) else False
    
    # Se obtienen los vecinos de un punto específico y se realiza una acción con los mismos
    def get_neighbors(self, state, type):
        actual_x = state[0]
        actual_y = state[1]
        #print("Este es actual_x" + str(actual_x))
        #print("Este es actual_y" + str(actual_y)
        
        #Una vez obteniendo el valor actual de x, se analizará los posibles 4 caminos disponibles
        #Caso 1: Arriba
        if (actual_x - 1) >= 0:
            if self.actions((actual_x - 1, actual_y)) == "path":
                if type == "allPath":
                    self.results("add", (actual_x - 1, actual_y))
                elif type == "shortestPath":
                    self.results("upd", (actual_x - 1, actual_y))
        #Caso 2: Abajo
        if (actual_x + 1) < self.height:
            if self.actions((actual_x + 1, actual_y)) == "path":
                if type == "allPath":
                    self.results("add", (actual_x + 1, actual_y))
                elif type == "shortestPath":
                    self.results("upd", (actual_x + 1, actual_y))
        #Caso 3: Izquierda
        if (actual_y - 1) >= 0:
            if self.actions((actual_x, actual_y - 1)) == "path":
                if type == "allPath":
                    self.results("add", (actual_x, actual_y - 1))
                elif type == "shortestPath":
                    self.results("upd", (actual_x, actual_y - 1))
        #Caso 4: Derecha
        if (actual_y + 1) < self.width:
            if self.actions((actual_x, actual_y + 1)) == "path":
                if type == "allPath":
                    self.results("add", (actual_x, actual_y + 1))
                elif type == "shortestPath":
                    self.results("upd", (actual_x, actual_y + 1))
    
    # Algoritmo principal
    def search(self):
        # Mientras haya fronteras evalua cada "nodo" del grafo (arreglo de arreglos)
        while not self.frontier_is_Empty():
            
            # Se agrega el punto actual al camino final
            actual_state = self.frontier.pop(0)
            self.path.append(actual_state)    
            
            # Se evalua si se llegó a la meta
            if self.goalTest(actual_state):
                return self.path
            
            # Se obtienen los vecinos en caso de que no sea la meta
            self.get_neighbors(actual_state, "allPath")
            
        return "No tiene solucion"
    
    # Función que se encarga de devolver cuál es el camino más corto
    def shortestPath(self):
        #Se vuelve a instanciar la lista de frontera y de los valores visitados
        self.frontier = [self.start]
        self.visited = []
        #Se crea un diccionario para con un valor de start para construir el camino
        self.backtracing = {self.start: None}
        
        #Mientras haya frontera, se analizará el nodo del grafo 
        while not self.frontier_is_Empty():
            #Se obtiene el primer valor de la frontera
            self.actualState = self.frontier.pop(0)
            #Se verifica si se llegó a la meta
            if self.goalTest(self.actualState):
                #Se obtiene el camino
                self.path = [self.start]
                while self.actualState != self.start:
                    self.results('back', self.actualState)
                self.path.reverse()
                #Se regresa el camino
                return self.path
            #Se obtienen los vecinos
            self.get_neighbors(self.actualState, "shortestPath")
        return "No tiene solucion"
        
        
        
        
        
        