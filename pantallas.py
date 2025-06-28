import pygame
from config import VENTANA, BLANCO, FUENTE, VERDE, ROJO

# ----------------- DIBUJAR ESTRUCTURA DEL AHORCADO -----------------
def dibujar_estructura():
    # Dibuja la base, palo y cuerda del ahorcado (no cuenta como error)
    dibujar_rectangulo(50, 300, 130, 20) # Base de la estructura. El primer valor corresponde a la coordena x, el segundo la coordenada de la y, el tercero es el ancho y el cuarto es la altura.
    dibujar_rectangulo(105, 50, 20, 250) # Mastil de la estructura. El primer valor corresponde a la coordena x, el segundo la coordenada de la y, el tercero es el ancho y el cuarto es la altura.
    dibujar_rectangulo(105, 50, 120, 20) # Part alta de la esctructura. El primer valor corresponde a la coordena x, el segundo la coordenada de la y, el tercero es el ancho y el cuarto es la altura.
    dibujar_rectangulo(225, 50, 10, 50) # Soga que va a sostener el cuerpo. El primer valor corresponde a la coordena x, el segundo la coordenada de la y, el tercero es el ancho y el cuarto es la altura.


def dibujar_rectangulo(x, y, ancho, alto, color=BLANCO):
    """
    Propósito: dibujar un rectangulo en las coordenas x, y ingresadas de un alto y ancho que lo ingresa el usuario. Por defecto es de color blanco. 
    """
    pygame.draw.rect(VENTANA, color, (x, y, ancho, alto)) # El primer valor que recibe la superficie en donde se va a dibujar el rectangulo, el segundo el color que por defecto es blanco, el tercero contiene las coordenas donde se dibuja, el alto y el ancho del rectangulo.


def dibujar_circulo(x, y, radio, color=BLANCO):
    """
    Propósito: dibujar un circulo en las coordenadas dadas con un radio dado que por defecto será de color blanco.
    """
    pygame.draw.circle(VENTANA, color, (x, y), radio) # El primer valor que recibe la superficie en donde se va a dibujar el circulo, el segundo el color que por defecto es blanco, el tercero contiene las coordenas donde se dibuja y el cuarto el radio del circulo.


def dibujar_linea(x_inicio, y_inicio, x_fin, y_fin, grosor, color=BLANCO):
    """
    Propósito: dibujar una linea desde una posición dada hacia otro punto dado, de un cierto grosor que será de color blanco por defecto.
    """
    pygame.draw.line(VENTANA, color, (x_inicio, y_inicio), (x_fin, y_fin), grosor) # 


# ----------------- DIBUJAR PARTES DEL CUERPO -----------------
def dibujar_cuerpo(errores):
    # Dibujar cabeza, tronco, brazos y piernas en base a la cantidad de errores
    # se toma la cantidad de errores y se ejecuta el caso que coincida con la cantidad.
    if errores >= 1: # Cuando la cantidad de errores es igual o mayor a 1 dibuja la cabeza del personaje.
            dibujar_circulo(230, 100, 20) # cabeza del personaje.
    if errores >= 2: # Cuando la cantidad de errores es igual o mayor a 2 dibuja el torso del personaje.
            dibujar_rectangulo(225, 100, 10, 100) # torso del personaje.
    if errores >= 3: # Cuando la cantidad de errores es igual o mayor a 3 dibuja el brazo izquierdo del del personaje.
            dibujar_linea(200, 180, 225, 130, 10) # Brazo izquierdo
    if errores >= 4: # Cuando la cantidad de errores es igual o mayor a 4 dibuja el brazo derecho del personaje.
            dibujar_linea(260, 180, 235, 130, 10) # Brazo derecho
    if errores >= 5: # Cuando la cantidad de errores es igual o mayor a 5 dibuja la pierna izquierda del personaje.
            dibujar_linea(200, 250, 225, 200, 10) # Pierna izquierdo
    if errores >= 6: # Cuando la cantidad de errores es igual o mayor a 6 dibuja la pierna derecha del personaje.
            dibujar_linea(260, 250, 235, 200, 10) # Pierna derecha

# ----------------- DIBUJAR JUEGO EN PANTALLA -----------------
def dibujar_juego(palabra, letras_adivinadas, errores):
    # Mostrar palabra oculta, letras ingresadas y dibujar estructura y cuerpo
    # Usa las dos funciones anteriores dentro de esta
    dibujar_estructura()
    dibujar_cuerpo(errores)
    mostrar_texto("Palabra a adivinar: ", 50, 350) # Mostrar texto de la palabra a adivinar.
    palabra_prueba = pasar_letras_a_guiones_si(palabra, letras_adivinadas)
    mostrar_texto(palabra_prueba, 350, 350) # Muestra el contenido de la variable palabra_prueva en las coordenas dadas. El segundo valor corresponde al eje de las x y el segundo al de las y. 
    mostrar_texto("Letras ingresadas: " + " ".join(letras_adivinadas), 50, 400) # Muestas las letras ingresadas por el usuario en las coordenadas dadas.



def mostrar_texto(texto, x, y, color=BLANCO):
    """
    Propósito: mostrar texto en la pantalla en las coordenadas dadas, en color blanco por defecto.
    """
    texto_modificado = FUENTE.render(texto, True, color) 
    VENTANA.blit(texto_modificado, (x, y))


def pasar_letras_a_guiones_si(palabra, letras_adivinadas):
    """
    Propósito: poner guiones en lugar de letras en la palabra ingresada si las letras no estan en las lista de letras adivinadas.
    """
    palabra_en_guiones = "" # Inicializo la variable con un str vacío.
    for i in palabra: # Para cada letra en palabra, realiza lo siguiente:
        if i.upper() in letras_adivinadas: # Si la letra en mayúscula esta en la lista de letras_adivinadas:
            palabra_en_guiones += i.upper() # Le concatena a la variable la letra en mayúscula.
        else: # si no se cumple la condición:
            palabra_en_guiones += "_ " # Se le concatena un guión y un espacio en blanco a la variable.
    return palabra_en_guiones # Retorna palabra_en guiones.


# ----------------- DIBUJAR PANTALLA DE VICTORIA -----------------
def dibujar_victoria(palabra, letras_adivinadas, errores):
    # Mostrar pantalla de victoria, no hace falta que uses todos los argumentos
    cantidad_de_intentos = len(letras_adivinadas) # le asigno la cantidad de intentos ingresados por el usuario a la variable para luego mostrarla.
    victoria_primer_mensaje = f"¡Haz Ganado! La palabra era {palabra}." # Le asigno a la variable el primer mensaje que va a mostrar en la pantalla de victoria.
    victoria_segundo_mensaje = f"Lo sacaste en {cantidad_de_intentos} intentos." # le asigno a la varible el segundo mensaje que se va a mostrar en pantalla.
    mostrar_texto(victoria_primer_mensaje, 100, 250, color=VERDE) # muestro el primer mensajes en pantalla.
    mostrar_texto(victoria_segundo_mensaje, 200, 300, color=VERDE) # muestro el segundo mensaje en pantalla.

# ----------------- DIBUJAR PANTALLA DE DERROTA -----------------
def dibujar_derrota(palabra, letras_adivinadas):
    # Mostrar pantalla de derrota.
    cantidad_de_intentos = len(letras_adivinadas)
    derrota_primer_mensaje = f"¡Haz Perdio! La palabra era {palabra}." # le asigno a la variable el primer mensaje de derrota que se va a mostrar en la pantalla.
    derrota_segundo_mensaje = f"No lo pudiste sacaste en {cantidad_de_intentos} intentos." # le asigno a la viable el segundo mensaje que se va a mostrar en pantalla.
    mostrar_texto(derrota_primer_mensaje, 120, 250, color=ROJO) # muestro el primer mensaje de derrota en pantalla
    mostrar_texto(derrota_segundo_mensaje, 130, 300, color=ROJO) # muestro el segundo mensaje de derrota en pantalla.