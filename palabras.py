import random, config, os  # Importa los módulos necesarios: random para números aleatorios, config para configuraciones propias, y os para manipulación de rutas de archivos.

# ----------------- CARGAR PALABRAS DESDE ARCHIVO -----------------
def cargar_palabras():
    # Función que carga palabras desde un archivo de texto

    try:
        # Intenta abrir el archivo "palabras.txt" que debe estar dentro de la carpeta "recursos"
        with open(os.path.join(os.getcwd(), "recursos", "palabras.txt"), "r", encoding="utf-8") as f:
            palabras = f.readlines()  # Lee todas las líneas del archivo y las guarda en una lista
            return [palabra.strip() for palabra in palabras]  # Retorna la lista de palabras, eliminando los saltos de línea y espacios
    except IOError:
        print("No se cargo correctamente")  # Si ocurre un error (por ejemplo, el archivo no existe), se muestra un mensaje

# ----------------- ELEGIR PALABRA AL AZAR -----------------
def elegir_palabra(lista_palabras):
    # Función que elige una palabra aleatoria de la lista y la convierte a mayúsculas

    indice_random = random.randint(0, len(lista_palabras) - 1)  # Genera un número aleatorio entre 0 y la cantidad de palabras - 1
    return lista_palabras[indice_random].upper()  # Retorna la palabra en mayúsculas

# ----------------- VERIFICAR LETRA -----------------
def verificar_letra(letra, palabra, letras_adivinadas):
    # Función que verifica si la letra está en la palabra y si ya fue adivinada

    if letra in letras_adivinadas:  # Si la letra ya fue adivinada antes
        return False  # Se considera como un nuevo error
    
    letras_adivinadas.append(letra)  # Agrega la letra a la lista de letras adivinadas
    return letra in palabra  # Retorna True si la letra está en la palabra, False si no

# ----------------- VERIFICAR FINAL -----------------
def verificar_final(palabra, letras_adivinadas, errores):
    # Función que determina si el juego debe terminar

    if errores >= config.INTENTOS_MAXIMOS:  # Si la cantidad de errores alcanza el máximo permitido
        return True  # El juego termina
    
    for letra in palabra:  # Recorre cada letra de la palabra
        if not letra in letras_adivinadas:  # Si alguna letra aún no fue adivinada
            return False  # El juego continúa
    
    return True  # Si se adivinaron todas las letras, el juego termina
