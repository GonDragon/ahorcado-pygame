import pygame
from config import VENTANA, ANCHO, ALTO # Podes importar cualquier variable global de config
# import config # O comentar la linea de arriba y descomentar esta para importar todo el modulo

# Recomiendo guardar cualquier cosa que quieras que tenga el personaje en este diccionario
# Como la posicion, la imagen, velocidad o lo que quieras
# Asi podes acceder facilmente desde cualquier funcion del archivo
PERSONAJE = {} 
def init():
    PERSONAJE.update({
        "velocidad_x": 6,  # Velocidad de movimiento horizontal
        "velocidad_y": 6,  # Velocidad de movimiento vertical
        "ancho": 60,  # Ancho del personaje
        "alto": 60,  # Alto del personaje
        "imagen": pygame.image.load("assets/img/capibara.png")  # Carga la imagen del personaje
    })
    PERSONAJE["imagen"] = pygame.transform.scale(PERSONAJE["imagen"], (PERSONAJE["ancho"], PERSONAJE["alto"]))
# ----------------- Eventos del personaje -----------------
def procesar_evento(personaje):
    # Recibe todos los eventos de pygame.event.get()
    # Asi que lo podes usar para detectar teclas precionadas con evento.type == pygame.KEYDOWN, por ejemplo
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and personaje.left > 0:
        personaje.x -= PERSONAJE["velocidad_x"]
    if teclas[pygame.K_RIGHT] and personaje.right < ANCHO:
        personaje.x += PERSONAJE["velocidad_x"]
    if teclas[pygame.K_UP] and personaje.top > ALTO - (ALTO / 3):
        personaje.y -= PERSONAJE["velocidad_y"]
    if teclas[pygame.K_DOWN] and personaje.bottom < ALTO:
        personaje.y += PERSONAJE["velocidad_y"]

# ----------------- Creando al personaje -----------------
def procesar_personaje():
    x = ANCHO - (ANCHO / 2)  # Posición inicial en el centro de la pantalla
    y = ALTO - (ALTO / 5) # Posición inicial en la parte inferior de la pantalla
    ubicacion = pygame.Rect(x, y, PERSONAJE["ancho"], PERSONAJE["alto"])
    return ubicacion  # Devuelve el rectángulo que representa al personaje

# ----------------- Dibujando al personaje -----------------
def dibujar_personaje(personaje):
    if PERSONAJE["imagen"]: # Verifica si la imagen del personaje está cargada
        VENTANA.blit(PERSONAJE["imagen"], personaje.topleft) # Dibuja la imagen del personaje en la ventana