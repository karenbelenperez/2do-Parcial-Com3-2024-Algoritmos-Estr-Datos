# Nuevo directorio
directorio = "directorio_alumnos"
if not os.path.exists(directorio):
    os.mkdir(directorio)
    
# Creación de lista y guardar

lista_alumnos = ListaDoblementeEnlazada()
lista_alumnos.lista_ejemplo()
archivo_alumnos = os.path.join(directorio, 'lista_alumnos.json')
guardar_lista_en_archivo(lista_alumnos, archivo_alumnos)

# Mover el directorio a una nueva ruta
nueva_ruta = 'nueva_ruta_alumnos'
mover_directorio(directorio, nueva_ruta)

# Borrar el archivo y el directorio en la nueva ruta
nuevo_archivo_alumnos = os.path.join(nueva_ruta, 'lista_alumnos.json')
borrar_archivo_y_directorio(nuevo_archivo_alumnos, nueva_ruta)

