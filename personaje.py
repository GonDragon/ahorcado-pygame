from config import VENTANA # Podes importar cualquier variable global de config
# import config # O comentar la linea de arriba y descomentar esta para importar todo el modulo

# Recomiendo guardar cualquier cosa que quieras que tenga el personaje en este diccionario
# Como la posicion, la imagen, velocidad o lo que quieras
# Asi podes acceder facilmente desde cualquier funcion del archivo
PERSONAJE = {} 

# ----------------- DIBUJAR ESTRUCTURA DEL AHORCADO -----------------
def procesar_evento(evento):
    # Recibe todos los eventos de pygame.event.get()
    # Asi que lo podes usar para detectar teclas precionadas con evento.type == pygame.KEYDOWN, por ejemplo
    pass

# ----------------- DIBUJAR PARTES DEL CUERPO -----------------
def procesar_personaje():
    # Todos los cambios que sucedan en el personaje frame por frame. Por ejemplo, cambiar su posicion acorde a su velocidad.
    pass

# ----------------- DIBUJAR PARTES DEL CUERPO -----------------
def dibujar_personaje():
    # Dibujar todo lo que tengas que dibujar del personaje. Aca no se modifica nada del personaje, solo se dibuja.
    pass