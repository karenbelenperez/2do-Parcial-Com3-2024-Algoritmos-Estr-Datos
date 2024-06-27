class alumno:
  def __init__(self, nombre, dni, fecha_ingreso, carrera):
     self.nombre = nombre
     self.dni = dni
     self.fecha_ingreso = fecha_ingreso
     self.carrera = carrera

    
 def cambiar_datos(self, nuevos_datos):
    for key. value in nuevo_datos.items():
      if key in self.datos:
        self.datos[key] = value
        
def antiguedad(self):
    fecha_ingreso = self.dato[fecha_ingreso]
    fecha_ingreso_dt = datetime(fecha_ingreso.año, fecha_ingreso.mes, fecha_ingreso.día)
    hoy = datetime.today()
    dif = hoy-fecha_ingreso_dt
    return dif.days

def __str__(self):
    return (f"nombre: [self.datos["nombre"]]/n"
            f"dni:  [self.datos["dni"]]/n"
            f"fecha_ingreso: [self.datos["fecha_ingreso"]]/n"
            f"carrera: [self.datos["carrera"]]/n")

 def __eq__(self, otro_alumno):
   return self.datos["dni"] == otr_alumno.datos["dni"]

