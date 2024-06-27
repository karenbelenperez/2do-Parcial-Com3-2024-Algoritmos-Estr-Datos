def guardar_lista_en_archivo(lista, archivo):
    with open(archivo, 'w') as file:
        json.dump([alumno.datos for alumno in lista], file, default=str)

def mover_directorio(origen, destino):
    try:
        os.rename(origen, destino)
    except Exception as e:
        print(f"Error al mover el directorio: {e}")

def borrar_archivo_y_directorio(archivo, directorio):
    try:
        if os.path.exists(archivo):
            os.remove(archivo)
        if os.path.exists(directorio):
            os.rmdir(directorio)
    except Exception as e:
        print(f"Error al borrar el archivo o directorio: {e}")

