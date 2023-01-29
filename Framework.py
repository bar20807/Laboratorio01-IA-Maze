"""
    Laboratorio 1 - Inteligencia Artificial
    José Rodrigo Barrera García
    Resolver un laberinto
    Universidad del Valle de Guatemala
"""
# Importar las librerías necesarias
from PIL import Image
from abc import ABC,abstractmethod

class Framework(ABC):
    @abstractmethod
    def __init__(self, matrix):
        pass
    @abstractmethod
    def actions(self):
        pass
    @abstractmethod
    def results(self):
        pass
    @abstractmethod
    def goalTest(self):
        pass
    @abstractmethod
    def stepCost(self,paths):
        pass
    @abstractmethod
    def pathCost(self,position):
        pass
    
        
        


    
  
    
    




    

