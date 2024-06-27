# Nuevo directorio

directorio = "directorio_alumnos"
if not os.path.exists(directorio):
    os.mkdir(directorio)

def guardar_lista_en_archivo(lista,archivo):
    with open(archivo, "w") as file: 
         json.dump([alumno.datos for alumno in lista], file, default=str)
       
def mover_directorio(origen, destino):
   try: 
       os.rename(origen, destino)
   exceot exception as e:
       print(f"error al mover el directorio: [e]")
def borrar_archivo_y_directorio(archivo, directorio):
    try
        if os.path.exists(archivo):
            os.remove(archivo)
        if os.path.exists(directorio):
            os.rmdir(directorio)
    except exception as e:
        print(f"error al borrar el archivo o directorio: [e]")
       
