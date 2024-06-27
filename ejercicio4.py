#ordenamiento de burbuja
def ordenar_por_fecha_ingreso (self):
   if not self.cabeza or not self.cabeza.siguiente:
     return
      cambio = true
     while cambio: 
      cambio = false
      actual = self.cabeza
      while actual.siguiente:
        if actual.dato.datos["fechaingreso"] > actual.siguiente.dato.datos["fechaingreso"]:
 
 #se procede a intercambiar los datos de los nodos.
 actual.dato, actual.siguiente.dato = actual.siguiente.dato, actual.dato
 cambio = true
 actual = actual.siguiente
          





               

