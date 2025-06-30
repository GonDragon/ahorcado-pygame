import random, config

# ----------------- CARGAR PALABRAS DESDE ARCHIVO -----------------
def cargar_palabras():
    # Leer las palabras desde un archivo de texto y devolver una lista
    # Asegurate de tener un archivo llamado palabras.txt con una palabra por línea
    try:
        with open("palabras.txt", "r", encoding="utf-8")as f:
            palabras = f.readlines()
            return [palabra.strip() for palabra in palabras]
    except:
        print("No se cargo correctamente")

# ----------------- ELEGIR PALABRA AL AZAR -----------------
def elegir_palabra(lista_palabras):
    # Elegir una palabra aleatoria de la lista y convertirla a mayúsculas
    indice_random = random.randint(0, len(lista_palabras) - 1)
    return lista_palabras[indice_random]

# ----------------- VERIFICAR LETRA -----------------
def verificar_letra(letra, palabra, letras_adivinadas):
    # Agregar la letra a letras_adivinadas si no estaba
    # Retornar True si la letra está en la palabra, False si no
    if letra in letras_adivinadas:
        return False
    letras_adivinadas.append(letra)
    return letra in palabra

def verificar_final(palabra, letras_adivinadas, errores):
    # Retorna TRUE si hay que terminar el juego
    # Retorna FALSE si el juego continua
    # El juego termina cuando adivinamos todas las letras de la palabra, o cuando cometemos demasiados errores
    if errores >= config.INTENTOS_MAXIMOS:
        return True
    for letra in palabra:
        if not letra in letras_adivinadas:
            return False
    return True