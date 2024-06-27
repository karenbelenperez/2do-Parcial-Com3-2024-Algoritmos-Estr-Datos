class Nodo:
  def __init__(self, dato):
      self.dato = dato
      self.siguiente = None
      self.anterior = None

class lista_doblemente_enlazada: 
   def __init__(self):
      self.cabeza = None
      self.cola = None 
  
def agregar(self, dato):
    nuevo_nodo = Nodo(dato)
    if self.cabeza is None:
       self.cabeza = nuevo_nodo
       self.cola = nuevo_nodo
    else: 
       self.cola.siguiente = nuevo_nodo
       nuevo_nodo.anterior = self.cola
       self.cola = nuevo_nodo
def __iter__(self):
    self.actual = self.cabeza
    return self
def __next__(self):
   if self.actual is None:
      raise stopiteracion
       return dato
